# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class planiva(models.Model):
     _name = 'planiva.planiva'
     _description = 'Plano Iva'
     _rec_name = 'cod_plan_iva'
     _order = "filho_de asc"
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

     nome = fields.Char('Descrição', required=True)
     cod_plan_iva = fields.Char(string="Código")
     grupo = fields.Boolean(string='Grupo')
     estruturas_Contas = fields.Char(string='Estructura')
     taxa_IVA = fields.Float(string='Taxa IVA')
     deducao = fields.Float(string='Dedução')
     conta_id = fields.Many2one('planconta.planconta', string='Conta', required=True)
     tipo_nao_liquidado = fields.Selection([('a', 'A'),
           ('b', 'B'),
           ('c', 'C'),],'Tipo Não Liquidado')
     linha_destino = fields.Selection([('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'),
                                       ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('10', '10'),
                                       ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'),
                                       ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'),
                                       ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'),
                                       ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30')], 'Linha Destino')
     tipologia = fields.Selection([('imo', 'IMO'), ('inv', 'INV'), ('obc', 'OBC'), ('srv', 'SRV')], 'Tipológia')

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


     @api.model
     def create(self, vals):
         res = super(planiva, self).create(vals)
         res.con_exist()
         return res
     @api.depends('estruturas_Contas')
     def val_estrutura(self):
         if self.estruturas_Contas != '':
             self.valida_estrut = True

     @api.onchange("cod_plan_iva")
     def chekStrutur(self):
         cod_def = self.cod_plan_iva
         cod_def_str = str(cod_def)
         list_mae = []
         count = 0
         for item in cod_def_str:
             list_mae.append(item)
             count += 1
         if count == 1:
             self.filho_de = self.cod_plan_iva

         if count > 1:
             self.filho_de = cod_def_str[0]
             plano = self.env['planiva.planiva'].search([('cod_plan_iva', '=', self.filho_de)])
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

     @api.onchange('cod_plan_iva')
     def ver_estru(self):
         conta = str(self.cod_plan_iva)
         list_fatias = []
         cont_item = 0
         for w in conta:
             list_fatias.append(w)
             cont_item += 1
         if cont_item > 1:
             if (conta.isnumeric()) == True:
                 plano = self.env['planiva.planiva'].search([('cod_plan_iva', '=', self.filho_de)])
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

     @api.onchange('conta_id')
     def upStrutuConta(self):
         conta = str(self.cod_plan_iva)
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

     @api.onchange('conta_id')
     def ver_eliment_strutuConta(self):
         estrutura = ['X', '.', 'X', '.', 'X', '.', 'X', '.', 'X', '.', 'XX', '.', 'XX', '.', 'XX', '.']
         iten_list = []
         conta = str(self.cod_plan_iva)
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
         cont_dif = self.cod_plan_iva
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
             plano = self.env['planiva.planiva'].search([('cod_plan_iva', '=', self.sub_filho)])
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
             plano = self.env['planiva.planiva'].search([('cod_plan_iva', '=', self.sub_filho)])
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
             plano = self.env['planiva.planiva'].search([('cod_plan_iva', '=', self.sub_filho)])
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
             plano = self.env['planiva.planiva'].search([('cod_plan_iva', '=', self.sub_filho)])
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
             plano = self.env['planiva.planiva'].search([('cod_plan_iva', '=', self.sub_filho)])
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
         self.conta = self.cod_plan_iva
         self.pronto = True
