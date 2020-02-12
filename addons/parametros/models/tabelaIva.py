# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _
import math

class iva(models.Model):
     _name = 'iva.iva'
     _description = 'IVA'
     name = fields.Char('Descrição', required=True)
     codigo = fields.Char(string="Codigo", required=True, copy=False, readonly=True, index=True,
                          default=lambda self: self._get_next_cod(), store=True, )
     taxa = fields.Float(string='Taxa')
     _rec_name = 'taxa'
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

     @api.model
     def _get_next_cod(self):
          sequence = self.env['ir.sequence'].search([('code', '=', 'iva.codigo')])
          next = sequence.get_next_char(sequence.number_next_actual)
          return next

     @api.model
     def create(self, vals):
          vals['codigo'] = self.env['ir.sequence'].next_by_code('iva.codigo') or _('New')
          res = super(iva, self).create(vals)
          # self.remo_docum_allter()

          return res
