# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

from odoo.exceptions import ValidationError


class planconta(models.Model):
     _name = 'planconta.planconta'
     _description = 'Plano Conta'
     _rec_name = 'cod_plan_cont'
     _order = "filho_de asc"
     nome = fields.Char('Descrição')
     cod_plan_cont = fields.Char(string="Conta", size=11)#, required=True
     grupo = fields.Boolean(string='Grupo')
     leva_terce = fields.Boolean(string='Leva Terceiro')
     leva_moeda_estrangeira = fields.Boolean(string='Leva Moeda Estrangeira')
     gestao_credito = fields.Boolean(string='Gestão Credito')
     leva_centro_custo = fields.Boolean(string='Leva Centro Custo')
     fluxo_caixa = fields.Boolean(string='Fluxo Caixa')
     control_IVA = fields.Boolean(string='Control IVA')
     IVA_id = fields.Many2one('iva.iva', string='IVA')
     estruturas_Contas = fields.Char(string='Estruturas de Contas', size=11)#, required=True
     control_imputa_centro_custo = fields.Boolean(string='Control Imputações - Centro de Custo')
     natureza_conta = fields.Selection([('0', 'Neutro'), ('1', 'Devedor'), ('2', 'Criador')], 'Natureza de Conta')#, required=True
     natureza_saldo = fields.Selection([('0', 'Neutro'), ('2', 'Creador'), ('1', 'Devedor')], 'Natureza de Saldo')#, required=True
     contabilidade_analitica = fields.Boolean(string="Contabilidadeanalitica")

     conta = fields.Char(string="Conta Unic", store=True)#este campo serve para verificar se esiste outra conta
     estrutura = fields.Boolean(string='Estrutura',store=True) # compute='ver_estru',
     _sql_constraints = [('conta_unique', 'unique(conta)', 'Conta ja existe!')]
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)
     mud_id = fields.Boolean(string="Mudar ID", default=True)

     #============Campos de controlo========================================================================
     control_cod_comp = fields.Char(string="Control Código",)                            #, compute='control_cod',  required=True
     filho_de = fields.Char(string='Filho de',  store=True)                              #compute='chekStrutur',
     sub_filho = fields.Char(string='Sub Filho',  store=True)                            #compute='ver_conta',
     tama_estru = fields.Integer(string='Tamanho estrutura', store=True)                 #, compute='chekStrutur'
     esnumerico = fields.Boolean(string='Estrutura', store=True)                         #, compute='ver_conta'
     exist_mae = fields.Boolean(string='Existe mae', store=True)                         #, compute='ver_conta'
     eliment_estr = fields.Boolean(string='Eliment Estrutura', store=True)               #, compute='ver_eliment_strutuConta'
     pronto = fields.Boolean(string='Pronto', store=True)                                #, compute='con_exist'
     novo_plan = fields.Boolean(string="Plano Novo")                                     #se é o novo plano de conta torna-se True
     #=======================================================================================================#


     @api.model
     def create(self, vals):
         res = super(planconta, self).create(vals)
         res.con_exist()
         return res


     @api.multi
     def write(self, vals):
         obg = super(planconta, self).write(vals)
         return obg

     @api.constrains('estrutura', 'eliment_estr', 'esnumerico', 'exist_mae')#verificação final
     def cont_exist(self):
         if self.novo_plan == False:
              if self.exist_mae == True:
                  pass
              else:
                  raise ValidationError("Esta conta ainda não pode ser criada!")

              if self.estrutura == True and self.eliment_estr == True:
                  pass
              else:
                  raise ValidationError("Conta tem deferente estrutura da conta mãe!")

              if self.esnumerico == True:
                  pass
              else:
                  raise ValidationError("Esta conta não é um numero!")

     @api.onchange("cod_plan_cont")
     def control_cod(self):
         if self.novo_plan == False:
               self.control_cod_comp = self.cod_plan_cont
               #self.chekStrutur()

     @api.onchange("cod_plan_cont")
     def chekStrutur(self):#identifica se a estrutura se e mae ou filho
         if self.novo_plan == False:
              cod_def = self.cod_plan_cont
              cod_def_str = str(cod_def)
              list_mae = []

              count = 0
              for item in cod_def_str:
                  list_mae.append(item)
                  count += 1
              if count == 1: #estrutura mae     "Se o campo cod_plan_cont tem um digito"
                  self.filho_de = self.cod_plan_cont

              if count > 1:#estrutura Filho      "Se o campo cod_plan_cont tem mais de que um digito"
                  self.filho_de = cod_def_str[0]
                  plano = self.env['planconta.planconta'].search([('cod_plan_cont', '=', self.filho_de)])
                  if plano:
                     self.estruturas_Contas = plano.estruturas_Contas #preenche o campo estrutura
                  else:
                      self.estruturas_Contas = ''

     @api.onchange('cod_plan_cont')
     def ver_estru(self):#ver se a estrutura filha e igual a estrutura mae
         cod = self.cod_plan_cont
         codig = str(cod)
         lista = []
         for c in codig:
             lista.append(c)
         if lista[1] == '0' and len(lista) == 2:
             self.novo_plan = True
         if self.novo_plan == False:
              conta = str(self.cod_plan_cont)
              list_fatias = []
              cont_item = 0
              for w in conta:
                  list_fatias.append(w)
                  cont_item += 1
              if cont_item > 1:
                  if (conta.isnumeric()) == True:
                      plano = self.env['planconta.planconta'].search([('cod_plan_cont', '=', self.filho_de)])
                      if plano:
                          for rec in plano:
                              if self.tama_estru < rec.tama_estru:
                                  warning = {
                                      'title': _('ERRO!'),
                                      'message': _('Conta tem deferente estrutura da conta mãe'),
                                  }
                                  return {'warning': warning}
                                  #raise ValidationError("Conta tem deferente estrutura da conta mae")
                              else:
                                  #pass
                                  #estrutura verdadeiro
                                  if (conta.isnumeric()) == True:
                                     self.estrutura = True
                      #else:
                      #       warning = {
                      #                'title': _('ERRO!'),
                      #                'message': _('Esta conta ainda não tem Conta mãe! (Mal estruturada)'),
                      #            }
                      #       return {'warning': warning}
                             #raise ValidationError("Esta conta ainda não pode ser criada! (Mal estruturada)")
              else:
                  if (conta.isnumeric()) == True:
                     self.estrutura = True


     @api.onchange('estruturas_Contas', 'natureza_saldo')#Torna a estrutura maiúscula
     def upStrutuConta(self):
         if self.novo_plan == False:
            val_up = str(self.estruturas_Contas)
            self.estruturas_Contas = val_up.upper()


     @api.onchange('natureza_conta')#Verifica a estrutura se tem elemento deferente de x.
     def ver_eliment_strutuConta(self):
         if self.novo_plan == False:
            estrutura = ['X', '.', 'X', '.', 'X', '.', 'X', '.', 'X', '.', 'XX', '.', 'XX', '.', 'XX', '.']
            iten_list = []
            conta = str(self.cod_plan_cont)
            estrot_dif = self.estruturas_Contas
            val = str(estrot_dif)
            estrot_dif = val.split('.')
            count = 0
            for iten in estrot_dif:
                iten_list.append(iten)
                for eliment in iten_list:
                    if eliment not in 'X.XX':
                        warning = {
                            'title': _('ERRO!'),
                            'message': _('Erro na estrutura de conta!, elimento ivalido na estrutura'),
                        }
                        return {'warning': warning}
                    else:
                        if (conta.isnumeric()) == True:
                           self.eliment_estr = True #se elimento e x ou .
                        #pass
                count += 1
            self.tama_estru = count  #O tamanho da estrutura

     #@api.one
     @api.onchange('nome')  # Verifica a conta
     def ver_conta(self):
         if self.novo_plan == False:
            list_fatias = []
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
                    #self.esnumerico = True #Se a conta é numerico
                #raise ValidationError('Esta conta não é um numero!')
            element = str(cont_dif)
            cont_item = 0
            for w in element:
                #print(*w)
                list_fatias.append(w)
                cont_item += 1
            #print(list_fatias)


            if cont_item == 1:
                self.exist_mae = True  # se existe conta mae

            elif cont_item == 2:
                n = 1
                del list_fatias[n:]
                sub = ''.join(map(str, list_fatias))
                self.sub_filho = sub
                plano = self.env['planconta.planconta'].search([('cod_plan_cont', '=', self.sub_filho)])
                if not plano:
                    if (sub.isnumeric()) == True:
                        warning = {
                            'title': _('Aviso!'),
                            'message': _('Esta conta ainda não pode ser criada!\n' + 'Conta ' + str(sub) + ' não existe na tabela de acordo com a estrutura.'),
                        }
                        return {'warning': warning}
                    else:
                       pass
                else:
                    self.exist_mae = True  # se existe conta mae

            elif cont_item == 3:
                n = 2
                del list_fatias[n:]
                sub = ''.join(map(str, list_fatias))
                self.sub_filho = sub
                plano = self.env['planconta.planconta'].search([('cod_plan_cont', '=', self.sub_filho)])
                if not plano:
                    if (sub.isnumeric()) == True:
                        warning = {
                            'title': _('Aviso!'),
                            'message': _('Esta conta ainda não pode ser criada!\n' + 'Conta ' + str(
                                sub) + ' não existe na tabela de acordo com a estrutura.'),
                        }
                        return {'warning': warning}
                    else:
                        pass

                else:
                     self.exist_mae = True  # se existe conta mae

            elif cont_item == 4:
                n = 3
                del list_fatias[n:]
                sub = ''.join(map(str, list_fatias))
                self.sub_filho = sub
                plano = self.env['planconta.planconta'].search([('cod_plan_cont', '=', self.sub_filho)])
                if not plano:
                    if (sub.isnumeric()) == True:
                        warning = {
                            'title': _('Aviso!'),
                            'message': _('Esta conta ainda não pode ser criada!\n' + 'Conta ' + str(
                                sub) + ' não existe na tabela de acordo com a estrutura.'),
                        }
                        return {'warning': warning}
                    else:
                        pass
                else:
                    self.exist_mae = True  # se existe conta mae
            elif cont_item == 5:
                n = 4
                del list_fatias[n:]
                sub = ''.join(map(str, list_fatias))
                self.sub_filho = sub
                plano = self.env['planconta.planconta'].search([('cod_plan_cont', '=', self.sub_filho)])
                if not plano:
                    if (sub.isnumeric()) == True:
                        warning = {
                            'title': _('Aviso!'),
                            'message': _('Esta conta ainda não pode ser criada!\n' + 'Conta ' + str(
                                sub) + ' não existe na tabela de acordo com a estrutura.'),
                        }
                        return {'warning': warning}
                    else:
                        pass
                else:
                    self.exist_mae = True  # se existe conta mae
            elif cont_item >= 6:
                n = 5
                del list_fatias[n:]
                sub = ''.join(map(str, list_fatias))
                self.sub_filho = sub
                plano = self.env['planconta.planconta'].search([('cod_plan_cont', '=', self.sub_filho)])
                if not plano:
                    if (sub.isnumeric()) == True:
                        warning = {
                            'title': _('Aviso!'),
                            'message': _('Esta conta ainda não pode ser criada!\n' + 'Conta ' + str(
                                sub) + ' não existe na tabela de acordo com a estrutura.'),
                        }
                        return {'warning': warning}
                    else:
                        pass
                else:
                    self.exist_mae = True  # se existe conta mae


     def con_exist(self):
         if self.novo_plan == False:
            self.conta = self.cod_plan_cont
            self.pronto = True





