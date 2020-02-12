# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class entbanc(models.Model):
     _name = 'entbanc.entbanc'
     _description = 'Entidade Bancaria'

     name = fields.Char('Descrição', required=True)
     terceiro = fields.Many2one('terceiro.terceiro', string='Terceiro')
     codigo_SWIFT = fields.Char(string='Código SWIFT')
     codigo = fields.Char(string="Código", required=True, copy=False, readonly=False, index=True,
                          default=lambda self: self._get_next_cod(), store=True, )
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

     @api.model
     def _get_next_cod(self):
          sequence = self.env['ir.sequence'].search([('code', '=', 'entbanc.entbanc')])
          next = sequence.get_next_char(sequence.number_next_actual)
          return next

     @api.model
     def create(self, vals):
          vals['codigo'] = self.env['ir.sequence'].next_by_code('entbanc.entbanc') or _('New')
          obg = super(entbanc, self).create(vals)
          return obg