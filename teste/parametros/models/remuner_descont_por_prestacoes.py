# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class descontoPrestacoes(models.Model):
     _name = 'remuner.desconto.prestacoes'
     _description = 'Desconto Por Prestações'
     numero = fields.Integer(string='Numero', required=True)
     data_inicio = fields.Date('Data Inicio')
     tipo = fields.Many2one('desconto.desconto', string='Numero', )
     numero_prestacao = fields.Integer(string='Número Prestação')
     montante = fields.Float(string='Numero')
     a_descontar = fields.Float(string='Numero')
     valor_descontado = fields.Float(string='Numero')
     descont_assoc_id = fields.Many2one('desconto.desconto')

     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)


