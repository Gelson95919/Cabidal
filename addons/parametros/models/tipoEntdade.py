# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class entidade(models.Model):
     _name = 'entidade.entidade'
     _description = 'Tipo Entidade'
     name = fields.Char('Tipo Entidade', required=True)
     date_release = fields.Date('Data de lançamento')

     value = fields.Integer()
     value3 = fields.Integer()
     value2 = fields.Float(compute="_value_pc", store=True)
     descript = fields.Text()
     desc = fields.Text()

     currency_id = fields.Many2one(
          'res.currency', string='Currency')

     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

     @api.depends('value')
     def _value_pc(self):
         self.value2 = float(self.value) / 100


