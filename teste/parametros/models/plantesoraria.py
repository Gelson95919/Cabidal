# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

from odoo.exceptions import ValidationError


class planteso(models.Model):
     _name = 'planteso.planteso'
     _description = 'Plano Tesouraria '
     _rec_name = 'cod_plan_teso'
     _order = "filho_de asc"

     cod_plan_teso = fields.Char(string='Código')
     nome = fields.Char('Descrição', required=True)
     tipo_movimento = fields.Selection([('3', 'Transferência'), ('1', 'Entrada'), ('2', 'Saida')], 'Tipo Movimento')
     estruturas_Contas = fields.Char(string='Estrutura')
     grupo = fields.Selection([('1', '')])

     filho_de = fields.Char(string='Filho de', compute='chekStrutur', store=True)
     tama_estru = fields.Integer(string='Tamanho estrutura', compute='chekStrutur', store=True)
     estrutura = fields.Boolean(string='Estrutura', compute='ver_estru', store=True)
     eliment_estr = fields.Boolean(string='Eliment Estrutura', compute='ver_eliment_strutuConta', store=True)
     esnumerico = fields.Boolean(string='Estrutura', compute='ver_conta', store=True)
     pronto = fields.Boolean(string='Pronto', compute='con_exist', store=True)
     exist_mae = fields.Boolean(string='Existe mae', compute='ver_conta', store=True)
     sub_filho = fields.Char(string='Sub Filho', compute='ver_conta', store=True)
     conta = fields.Char(string="Conta", store=True)
     _sql_constraints = [('conta_unique', 'unique(conta)', 'Conta ja existe!')]
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

     @api.model
     def create(self, vals):
         res = super(planteso, self).create(vals)
         res.con_exist()
         return res

     @api.onchange("cod_plan_teso")
     def chekStrutur(self):
         cod_def = self.cod_plan_teso
         cod_def_str = str(cod_def)
         list_mae = []
         count = 0
         for item in cod_def_str:
             list_mae.append(item)
             count += 1
         if count == 1:
             self.filho_de = self.cod_plan_teso

         if count > 1:
             self.filho_de = cod_def_str[0]
             plano = self.env['planteso.planteso'].search([('cod_plan_teso', '=', self.filho_de)])
             if plano:
                 self.estruturas_Contas = plano.estruturas_Contas
             else:
                 self.estruturas_Contas = ''

     @api.constrains('estrutura', 'eliment_estr', 'esnumerico', 'exist_mae')  # verificação final
     def cont_exist(self):
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

     @api.onchange('cod_plan_teso')
     def ver_estru(self):
         conta = str(self.cod_plan_teso)
         list_fatias = []
         cont_item = 0
         for w in conta:
             list_fatias.append(w)
             cont_item += 1
         if cont_item > 1:
             if (conta.isnumeric()) == True:
                 plano = self.env['planteso.planteso'].search([('cod_plan_teso', '=', self.filho_de)])
                 if plano:
                     for rec in plano:
                         if self.tama_estru < rec.tama_estru:
                             warning = {
                                 'title': _('ERRO!'),
                                 'message': _('Conta tem deferente estrutura da conta mãe'),
                             }
                             return {'warning': warning}

                         else:
                             if (conta.isnumeric()) == True:
                                 self.estrutura = True
         else:
             if (conta.isnumeric()) == True:
                 self.estrutura = True

     @api.onchange('tipo_movimento')
     def upStrutuConta(self):
         conta = str(self.cod_plan_teso)
         if (conta.isnumeric()) == True:
             part = self.estruturas_Contas
             if not part:
                 warning = {
                     'title': _('Warning!'),
                     'message': _('Você deve primeiro Adicionar uma estrutura!'),
                 }
                 return {'warning': warning}
             else:
                 val_up = str(self.estruturas_Contas)
                 self.estruturas_Contas = val_up.upper()

     @api.onchange('tipo_movimento')
     def ver_eliment_strutuConta(self):
         estrutura = ['X', '.', 'X', '.', 'X', '.', 'X', '.', 'X', '.', 'XX', '.', 'XX', '.', 'XX', '.']
         iten_list = []
         conta = str(self.cod_plan_teso)
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
                         self.eliment_estr = True

             count += 1
         self.tama_estru = count

     @api.onchange('nome')
     def ver_conta(self):
         # self.ensure_one
         list_fatias = []
         cont_dif = self.cod_plan_teso
         try:
             val = int(cont_dif)
             self.esnumerico = True
         except ValueError:
             if cont_dif:
                 warning = {
                     'title': _('ERRO!'),
                     'message': _('Esta conta não é um numero!' ' ' + str(cont_dif)),
                 }
                 return {'warning': warning}
             else:
                 pass
         element = str(cont_dif)
         cont_item = 0
         for w in element:
             list_fatias.append(w)
             cont_item += 1

         if cont_item == 1:
             self.exist_mae = True  # se existe conta mae


         elif cont_item == 2:
             n = 1
             del list_fatias[n:]
             sub = ''.join(map(str, list_fatias))
             self.sub_filho = sub
             plano = self.env['planteso.planteso'].search([('cod_plan_teso', '=', self.sub_filho)])
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
                 self.exist_mae = True

         elif cont_item == 3:
             n = 2
             del list_fatias[n:]
             sub = ''.join(map(str, list_fatias))
             self.sub_filho = sub
             plano = self.env['planteso.planteso'].search([('cod_plan_teso', '=', self.sub_filho)])
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
             plano = self.env['planteso.planteso'].search([('cod_plan_teso', '=', self.sub_filho)])
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
             plano = self.env['planteso.planteso'].search([('cod_plan_teso', '=', self.sub_filho)])
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
             plano = self.env['planteso.planteso'].search([('cod_plan_teso', '=', self.sub_filho)])
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
         self.conta = self.cod_plan_teso
         self.pronto = True


class alteracaoOrcamentoTesouraria(models.Model):
    _name = 'alteracao.orcamento.tesouraria'
    #_rec_name = 'name'
    _description = 'Alteração Orçamento Tesouraria'
    codigo_plan_cont_id = fields.Many2one('planteso.planteso', string="Descrição")
    valor_anual = fields.Float()
    mes_inicial = fields.Integer()
    orcamenteso_id = fields.Many2one('orcamenteso.orcamenteso')
    tipo = fields.Selection([('aumentar', 'Aumentar'), ('diminuir', 'Diminuir')])
    janeiro = fields.Integer(string='Janeiro', readonly=False, store=True)
    fevereiro = fields.Integer(string='Fevereiro', readonly=False, store=True)
    marco = fields.Integer(string='Março', readonly=False, store=True)
    abril = fields.Integer(string='Abril', readonly=False, store=True)
    maio = fields.Integer(string='Maio', readonly=False, store=True)
    junho = fields.Integer(string='Junho', readonly=False, store=True)
    julho = fields.Integer(string='Julho', readonly=False, store=True)
    agosto = fields.Integer(string='Agosto', readonly=False, store=True)
    setembro = fields.Integer(string='Setembro', readonly=False, store=True)
    outubro = fields.Integer(string='Outubro', readonly=False, store=True)
    novembro = fields.Integer(string='Novembro', readonly=False, store=True)
    dezembro = fields.Integer(string='Dezembro', compute='calc_valores', readonly=False, store=True)
    motivo = fields.Text(string='Motivo')
    editar = fields.Boolean(string="Editar")
    ano = fields.Integer()
    resultado = fields.Float(string="Resultado")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

    @api.depends('valor_anual', 'resultado', 'mes_inicial', 'janeiro', 'fevereiro', 'marco',
                 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro',)
    def calc_valores(self):
        self.resultado = self.valor_anual / 12
        if self.mes_inicial == 0 or self.mes_inicial == 1:
            self.janeiro = self.resultado
            self.fevereiro = self.resultado
            self.marco = self.resultado
            self.abril = self.resultado
            self.maio = self.resultado
            self.junho = self.resultado
            self.julho = self.resultado
            self.agosto = self.resultado
            self.setembro = self.resultado
            self.outubro = self.resultado
            self.novembro = self.resultado
            self.dezembro = self.valor_anual - (self.janeiro + self.fevereiro + self.marco + self.abril + self.maio +
                                                self.junho + self.julho + self.agosto + self.setembro + self.outubro + self.novembro)
        if self.mes_inicial == 2:
            self.janeiro = 0
            self.fevereiro = 0
            self.marco = self.resultado
            self.abril = self.resultado
            self.maio = self.resultado
            self.junho = self.resultado
            self.julho = self.resultado
            self.agosto = self.resultado
            self.setembro = self.resultado
            self.outubro = self.resultado
            self.novembro = self.resultado
            self.dezembro = self.valor_anual - (self.janeiro + self.fevereiro + self.marco + self.abril + self.maio +
                                                self.junho + self.julho + self.agosto + self.setembro + self.outubro + self.novembro)

        if self.mes_inicial == 3:
            self.janeiro = 0
            self.fevereiro = 0
            self.marco = 0
            self.abril = self.resultado
            self.maio = self.resultado
            self.junho = self.resultado
            self.julho = self.resultado
            self.agosto = self.resultado
            self.setembro = self.resultado
            self.outubro = self.resultado
            self.novembro = self.resultado
            self.dezembro = self.valor_anual - (self.janeiro + self.fevereiro + self.marco + self.abril + self.maio +
                                                self.junho + self.julho + self.agosto + self.setembro + self.outubro + self.novembro)

        if self.mes_inicial == 4:
            self.janeiro = 0
            self.fevereiro = 0
            self.marco = 0
            self.abril = 0
            self.maio = self.resultado
            self.junho = self.resultado
            self.julho = self.resultado
            self.agosto = self.resultado
            self.setembro = self.resultado
            self.outubro = self.resultado
            self.novembro = self.resultado
            self.dezembro = self.valor_anual - (self.janeiro + self.fevereiro + self.marco + self.abril + self.maio +
                                                self.junho + self.julho + self.agosto + self.setembro + self.outubro + self.novembro)

        if self.mes_inicial == 5:
            self.janeiro = 0
            self.fevereiro = 0
            self.marco = 0
            self.abril = 0
            self.maio = 0
            self.junho = self.resultado
            self.julho = self.resultado
            self.agosto = self.resultado
            self.setembro = self.resultado
            self.outubro = self.resultado
            self.novembro = self.resultado
            self.dezembro = self.valor_anual - (self.janeiro + self.fevereiro + self.marco + self.abril + self.maio +
                                                self.junho + self.julho + self.agosto + self.setembro + self.outubro + self.novembro)

        if self.mes_inicial == 6:
            self.janeiro = 0
            self.fevereiro = 0
            self.marco = 0
            self.abril = 0
            self.maio = 0
            self.junho = 0
            self.julho = self.resultado
            self.agosto = self.resultado
            self.setembro = self.resultado
            self.outubro = self.resultado
            self.novembro = self.resultado
            self.dezembro = self.valor_anual - (self.janeiro + self.fevereiro + self.marco + self.abril + self.maio +
                                                self.junho + self.julho + self.agosto + self.setembro + self.outubro + self.novembro)

        if self.mes_inicial == 7:
            self.janeiro = 0
            self.fevereiro = 0
            self.marco = 0
            self.abril = 0
            self.maio = 0
            self.junho = 0
            self.julho = 0
            self.agosto = self.resultado
            self.setembro = self.resultado
            self.outubro = self.resultado
            self.novembro = self.resultado
            self.dezembro = self.valor_anual - (self.janeiro + self.fevereiro + self.marco + self.abril + self.maio +
                                                self.junho + self.julho + self.agosto + self.setembro + self.outubro + self.novembro)

        if self.mes_inicial == 8:
            self.janeiro = 0
            self.fevereiro = 0
            self.marco = 0
            self.abril = 0
            self.maio = 0
            self.junho = 0
            self.julho = 0
            self.agosto = 0
            self.setembro = self.resultado
            self.outubro = self.resultado
            self.novembro = self.resultado
            self.dezembro = self.valor_anual - (self.janeiro + self.fevereiro + self.marco + self.abril + self.maio +
                                                self.junho + self.julho + self.agosto + self.setembro + self.outubro + self.novembro)

        if self.mes_inicial == 9:
            self.janeiro = 0
            self.fevereiro = 0
            self.marco = 0
            self.abril = 0
            self.maio = 0
            self.junho = 0
            self.julho = 0
            self.agosto = 0
            self.setembro = 0
            self.outubro = 0
            self.novembro = self.resultado
            self.dezembro = self.valor_anual - (self.janeiro + self.fevereiro + self.marco + self.abril + self.maio +
                                                self.junho + self.julho + self.agosto + self.setembro + self.outubro + self.novembro)

        if self.mes_inicial == 10:
            self.janeiro = 0
            self.fevereiro = 0
            self.marco = 0
            self.abril = 0
            self.maio = 0
            self.junho = 0
            self.julho = 0
            self.agosto = 0
            self.setembro = 0
            self.outubro = 0
            self.novembro = 0
            self.dezembro = self.valor_anual - (self.janeiro + self.fevereiro + self.marco + self.abril + self.maio +
                                                self.junho + self.julho + self.agosto + self.setembro + self.outubro + self.novembro)
