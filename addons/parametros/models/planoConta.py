# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

from odoo.exceptions import ValidationError


class planconta(models.Model):
     _name = 'planconta.planconta'
     _description = 'Plano Conta'
     _rec_name = 'cod_plan_cont'
     _order = "id"
     nome = fields.Char('Descrição')
     cod_plan_cont = fields.Char(string="Conta", size=11)#, required=True
     grupo = fields.Boolean(string='Grupo', readonly=True)
     leva_terce = fields.Boolean(string='Leva Terceiro')
     leva_moeda_estrangeira = fields.Boolean(string='Leva Moeda Estrangeira')
     gestao_credito = fields.Boolean(string='Gestão Credito')
     leva_centro_custo = fields.Boolean(string='Leva Centro Custo')
     fluxo_caixa = fields.Boolean(string='Fluxo Caixa')
     control_IVA = fields.Boolean(string='Control IVA')
     IVA_id = fields.Many2one('iva.iva', string='IVA')
     estruturas_Contas = fields.Char(string='Estruturas de Contas')#, required=True
     control_imputa_centro_custo = fields.Boolean(string='Control Imputações - Centro de Custo')
     natureza_conta = fields.Selection([('0', 'Neutro'), ('1', 'Devedor'), ('2', 'Criador')], 'Natureza de Conta', default='0')#, required=True
     natureza_saldo = fields.Selection([('0', 'Neutro'), ('2', 'Creador'), ('1', 'Devedor')], 'Natureza de Saldo', default='0')#, required=True
     contabilidade_analitica = fields.Boolean(string="Contabilidadeanalitica")

     conta = fields.Char(string="Conta Unic", store=True)#este campo serve para verificar se esiste outra conta
     estrutura = fields.Boolean(string='Estrutura',store=True) # compute='ver_estru',
     _sql_constraints = [('conta_unique', 'unique(conta)', 'Conta ja existe!')]
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)
     mud_id = fields.Boolean(string="Mudar ID", default=True)
     pronto = fields.Boolean(string='Pronto', store=True)                                #, compute='con_exist'
     no_exist_mae = fields.Boolean(string='Existe mae', store=True)



     #============Campos de controlo========================================================================
     control_cod_comp = fields.Char(string="Control Código",)                            #, compute='control_cod',  required=True
     filho_de = fields.Char(string='Filho de',  store=True)                              #compute='chekStrutur',
     sub_filho = fields.Char(string='Sub Filho',  store=True)                            #compute='ver_conta',
     tama_estru = fields.Integer(string='Tamanho estrutura', store=True)                 #, compute='chekStrutur'
     esnumerico = fields.Boolean(string='Estrutura', store=True)                         #, compute='ver_conta'
     eliment_estr = fields.Boolean(string='Eliment Estrutura', store=True)               #, compute='ver_eliment_strutuConta'
     novo_plan = fields.Boolean(string="Plano Novo")                                     #se é o novo plano de conta torna-se True
     mae = fields.Boolean(string="Mae")                                                        #este campo muda constantemente
     conta_mae = fields.Char(compute="valida_estrot_cont")
     #=======================================================================================================#


     @api.model
     def create(self, vals):
         res = super(planconta, self).create(vals)
         res.torn_grup()
         return res

     @api.multi
     def write(self, vals):
         self.torn_grup()
         cont_dif = self.cod_plan_cont
         cod_con = str(cont_dif)
         c = cod_con[0]
         val = {}
         self.env['ir.rule'].clear_cache()
         raza = self.env['lancamento_diario.lancamento_diario'].search([('codigo_conta', '=', self.cod_plan_cont)])
         if raza:
             raise ValidationError('Esta conta ja foi movimentado.')
         else:
             if 'estruturas_Contas' in vals: val['estruturas_Contas'] = vals['estruturas_Contas']
             campo = self.env['conta.pae'].search([('cod_plan_cont', '=', c)])
             campo.write(val)
         obg = super(planconta, self).write(vals)
         return obg

     @api.constrains('cod_plan_cont')
     def cont_exist(self):
          exsist_cont = self.search([['id', '!=', self.id]]).mapped('cod_plan_cont')
          if self.cod_plan_cont and self.cod_plan_cont in exsist_cont:
              raise ValidationError('Já Existe...')
          if self.no_exist_mae == True:
             raise ValidationError('Esta conta ainda não pode ser criado.')

     @api.onchange('estruturas_Contas')
     def up_estrut(self):
         if self.estruturas_Contas:
             val_up = str(self.estruturas_Contas)
             self.estruturas_Contas = val_up.upper()
             estr = self.estruturas_Contas
             est = str(estr)
             for c in est:
                 if c == '..':
                     raise ValidationError('A estrutura está mal definido! ".."')
             estrutur = estr.split('.')
             pon = max(enumerate(estr))
             p = pon[1]
             pont = str(p)
             if pont != '.':
                raise ValidationError('Adiciona um ponto no final da estrutura! "."')



     @api.onchange('cod_plan_cont')
     def valida_estrot_cont(self):

         if self.cod_plan_cont:
             cod = self.cod_plan_cont
             codig = str(cod)
             lista = [] #esta lista serve para ver plano de conta Novo ou velho
             for c in codig:
                 lista.append(c)
             if len(lista) > 1:
                if lista[1] == '0' and len(lista) == 2:
                    self.novo_plan = True #No plano de conta novo comessa com o 10 mas des não e uma conta inicial quando e asim não valida ese conta
             if self.novo_plan == False:

                 cont_dif = self.cod_plan_cont
                 try:
                     val = int(cont_dif)
                     self.esnumerico = True  # Se a conta é numerico
                 except ValueError:
                     if cont_dif:
                         warning = {
                             'title': _('ERRO!'),
                             'message': _('Esta conta não é um numero!' ' ' + str(cont_dif)),
                         }
                         return {'warning': warning}
                     else:
                         pass

                 len_cod_ccont = []
                 len_estrot = []
                 sep_cod_con = []
                 cod_separ = []
                 estrut_sep = []
                 sep_estrut = []
                 lista_dados = list()
                 dados = list()
                 cont_dif = self.cod_plan_cont
                 cod_con = str(cont_dif)
                 item = 0
                 c = cod_con[0]
                 for i in cod_con:
                     len_cod_ccont.append(i)
                     item += 1
                 if item == 1:
                     self.exist_mae = True  # e a conta mae
                     self.mae = True
                     self.conta_mae = self.cod_plan_cont
                 nun = max(enumerate(len_cod_ccont))
                 n = nun[0]
                 nume = int(n)
                 if item > 1:

                    #pl = self.env['planconta.planconta'].search([('mae', '=', True)])
                    p = self.env['conta.pae'].search([('cod_plan_cont', '=', c)])
                    pestr = p.estruturas_Contas
                    c_cod_c = p.cod_plan_cont
                    c_cod_cont = str(c_cod_c)
                    estrot = str(pestr)
                    p_estrutur = estrot.split('.')
                    p_estrutur.pop()
                    for k, v in enumerate(p_estrutur):
                        len_estrot.append(v)
                    cont = 0 #conta o digitos de campo estrutura
                    for ke, ve in enumerate(p_estrutur):
                        for e, l in enumerate(p_estrutur[ke]):
                             if cont <= nume:
                                sep_estrut.append(l)
                                co = len_cod_ccont[cont]
                                sep_cod_con.append(co)
                                dados.append(co)
                                cont += 1
                        lista_dados.clear()
                        estrut_sep.append((sep_estrut[:]))
                        cod_separ.append((sep_cod_con[:]))
                        lista_dados.append((dados[:]))
                        sep_cod_con.clear()
                        sep_estrut.clear()
                        if len(cod_separ) != len(estrut_sep):
                            raise ValidationError('Esta conta esta mal estruturada.')
                        #dados.clear()
                        cd = ''.join(lista_dados[0])
                        cod_cont = str(cd)
                        self.control_cod_comp = cod_cont
                        if len(len_cod_ccont) > cont:
                           pl = self.env['planconta.planconta'].search(
                               [('cod_plan_cont', '=', self.control_cod_comp)])
                           if not pl:
                               warning = {
                                   'title': _('Atenção!'),
                                   'message': _(
                                       'Esta conta ainda não pode ser criada!\n' + 'Conta ' + str(
                                           cod_cont) + ' não existe na tabela de acordo com a estrutura.')}
                               self.estruturas_Contas = ''
                               self.no_exist_mae = True
                               return {'warning': warning}

                           else:
                               if pl.mae == False:
                                  if len(len_estrot) < len(len_cod_ccont):
                                      raise ValidationError('Esta conta ainda não pode ser criada, não existe na tabela de acordo com a estrutura.')
                        if cod_con[0] == c_cod_cont[0]:
                            self.estruturas_Contas = p.estruturas_Contas
                        if nume == 1:
                            self.estruturas_Contas = p.estruturas_Contas
                            break


     def torn_grup(self):
         self.ensure_one()
         len_cod_ccont = []
         sep_cod_con = []
         cod_separ = []
         estrut_sep = []
         sep_estrut = []
         lista_dados = list()
         dados = list()
         cont_dif = self.cod_plan_cont
         cod_con = str(cont_dif)
         c = cod_con[0]
         item = 0
         for i in cod_con:
             len_cod_ccont.append(i)
             item += 1
         nun = max(enumerate(len_cod_ccont))
         n = nun[0]
         nume = int(n)
         p = self.env['conta.pae'].search([('cod_plan_cont', '=', c)])
         pestr = p.estruturas_Contas
         estrot = str(pestr)
         pestrutur = estrot.split('.')
         pestrutur.pop()
         cod = p.cod_plan_cont
         if item == 1:
             if not p:
                conta_pae = self.env['conta.pae']
                pae = conta_pae.create(
                    {'name': self.nome, 'cod_plan_cont': self.cod_plan_cont,
                     'estruturas_Contas': self.estruturas_Contas, 'plano_conta_id': self.id})
         if item > 1:
             if p:
                   if cod[0] == cod_con[0] and self.estruturas_Contas != p.estruturas_Contas:
                      pla = self.env['planconta.planconta'].search([('id', '=', p.plano_conta_id)])
                      pla.mae = False
                      self.mae = True
                      pla.grupo = True
                      name = pla.nome
                      nome = name.upper()
                      pla.nome = nome
             cont = 0  # conta o digitos de campo estrutura
             for ke, ve in enumerate(pestrutur):
                    for e, l in enumerate(pestrutur[ke]):
                        if cont <= nume:
                           sep_estrut.append(l)
                           co = len_cod_ccont[cont]
                           sep_cod_con.append(co)
                           dados.append(co)
                           cont += 1
                    lista_dados.clear()
                    estrut_sep.append((sep_estrut[:]))
                    cod_separ.append((sep_cod_con[:]))
                    lista_dados.append((dados[:]))
                    sep_cod_con.clear()
                    sep_estrut.clear()
                    #dados.clear()
                    cd = ''.join(lista_dados[0])
                    cod_cont = str(cd)
                    if len(len_cod_ccont) > cont:
                        pl = self.env['planconta.planconta'].search([('cod_plan_cont', '=', cod_cont)])
                        if pl.grupo == False:
                           pl.grupo = True
                           name = pl.nome
                           nom = name.upper()
                           pl.nome = nom



class contaPae(models.Model):
    _name = 'conta.pae'
    _description = 'Conta pae'
    name = fields.Char()
    cod_plan_cont = fields.Char()
    estruturas_Contas = fields.Char()
    plano_conta_id = fields.Integer(string="Id plano")
    _sql_constraints = [('cod_plan_cont_unique', 'unique(cod_plan_cont)', 'Conta ja existe!')]

