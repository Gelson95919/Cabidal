# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class pagamento(models.Model):
     _name = 'pagamento.pagamento'
     _description = 'Modo Pagamento'
     name = fields.Char('Descrição', required=True)
     leva_control = fields.Boolean(string='Leva Control')
     dias_venc = fields.Integer(string='Dias Vencidas')
     por_prestacoes = fields.Boolean(string='Por Prestações')
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

