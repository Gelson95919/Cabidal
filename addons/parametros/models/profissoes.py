# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class profissoes(models.Model):
     _name = 'profissoes.profissoes'
     _description = 'Cargos'
     _rec_name = 'name'
     name = fields.Char('Profissões', required=True)
     codigo = fields.Char(string="Codigo")
     type = fields.Selection(
          [('professoes', 'Profesõoe'), ('mircocred_professoes', 'Microcred/Professões'), ],
          readonly=True, index=True, change_default=True,
          default=lambda self: self._context.get('type', 'professoes'),
          track_visibility='always')
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

     @api.model
     def create(self, vals):
          vals['codigo'] = self.env['ir.sequence'].next_by_code('profissoes') or _('New')
          res = super(profissoes, self).create(vals)

          return res



