# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class unimedida(models.Model):
     _name = 'unimedida.unimedida'
     _description = 'Unidade Medida'
     _rec_name = 'name'
     name = fields.Char(string='Descrição', required=True)
     codigo = fields.Char(string="Código", required=True, copy=False, readonly=True,
                              index=True, default=lambda self: self._get_next_cod())
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

     type = fields.Selection(
          [('inventario_uni_medida', 'Inventa/UniMedida'), ('mircocred_uni_medida', 'Microcred/UniMedida'), ],
          readonly=True, index=True, change_default=True, default=lambda self: self._context.get('type', 'inventario_uni_medida'),
          track_visibility='always')
     @api.model
     def _get_next_cod(self):
          sequence = self.env['ir.sequence'].search([('code', '=', 'unidade.medida')])
          next = sequence.get_next_char(sequence.number_next_actual)
          return next

     @api.model
     def create(self, vals):
        vals['codigo'] = self.env['ir.sequence'].next_by_code('unidade.medida') or _('New')
        res = super(unimedida, self).create(vals)

        return res



