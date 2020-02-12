# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class preco(models.Model):
     _name = 'preco.preco'
     _description = 'Preço'
     name = fields.Char('Descrição', required=True)
     n_preco = fields.Integer(string='Nº Preço')
     valor = fields.Float(string='Valor')
     iva_incluido = fields.Boolean(string='IVA Incluido')
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)
