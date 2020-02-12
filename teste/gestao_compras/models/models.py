# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class gestao_compras(models.Model):
     _name = 'gestao_compras.gestao_compras'
     name = fields.Char('Title', required=True)
     date_release = fields.Date('Data de lançamento')

     value = fields.Integer()
     value2 = fields.Float(compute="_value_pc", store=True)
     descript = fields.Text()
     desc = fields.Text()
     currency_id = fields.Many2one(
          'res.currency', string='Currency')

     currency_id = fields.Many2one(
          'res.currency', string='Curre')

     @api.depends('value')
     def _value_pc(self):
         self.value2 = float(self.value) / 100

gestao_compras()