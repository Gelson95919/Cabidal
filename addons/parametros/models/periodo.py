# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class periodo(models.Model):
     _name = 'periodo.periodo'
     _description = 'Periodo'
     codigo = fields.Char(string="Codigo", required=True, copy=False, readonly=False,
                          index=True, default=lambda self: _('New'))
     name = fields.Char('Descrição', required=True)
     data_inicio = fields.Date(string='Data Inicio')
     data_fim = fields.Date(string='Data Fim')
     fecho = fields.Boolean(string='Fechar')
     dfecinic = fields.Char()
     dfecfin = fields.Char()
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

     @api.model
     def create(self, vals):
          vals['codigo'] = self.env['ir.sequence'].next_by_code('periodo.periodo') or _('New')
          res = super(periodo, self).create(vals)
          #res.create_period()
          return res

     @api.multi
     def write(self, vals):
          self.ensure_one()
          val = {}
          if 'name' in vals: val['descricao'] = vals['name']
          if 'codigo' in vals: val['Periodo'] = vals['codigo']
          #campo = self.env['orcamenteso.orcamenteso'].search(
          #     [('Periodo', '=', self.codigo)])
          #campo.write(val)
          obg = super(periodo, self).write(vals)
          return obg


     def create_period(self):
          per_obj = self.env['orcamenteso.orcamenteso']
          period = per_obj.create({'Periodo': self.codigo, 'descricao': self.name})
          return period

     @api.multi
     def name_get(self):
          result = []
          for record in self:
               name = '' + str(record.codigo) + ' ' + ' ' + record.name
               result.append((record.id, name))
          return result