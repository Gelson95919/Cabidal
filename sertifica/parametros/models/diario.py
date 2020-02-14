# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class diario(models.Model):
     _name = 'diario.diario'
     _description = 'Diario'
     _rec_name = 'codigo'
     codigo = fields.Char(string="Documento", store=True, copy=True, index=True, default=lambda self: self._get_next_cod())
     name = fields.Char('Descrição')#, required=True
     fecho = fields.Char('Fecho')
     numero_documento_inicial = fields.Char(string='Numero Documento Inicial	')
     conta = fields.Many2one('planconta.planconta', string='Conta')
     sequence_id = fields.Many2one('ir.sequence', string='Sequência de entrada', copy=False)#, required=False,
     ttype = fields.Selection([('1', 'Folha de Caixa'), ('2', 'Folha de Banco'), ('3', 'Folha de Venda'), ('4', 'Folha de Compras'),
                               ('5', 'Operações Diversa'), ], string="Tipo",)#, required=True
     anual_mensal = fields.Selection([('0', 'Anual'), ('1', 'Mensal')], 'Anual/Mensal')
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

     @api.model
     def _get_next_cod(self):
          sequence = self.env['ir.sequence'].search([('code', '=', 'cod.diario')])
          next = sequence.get_next_char(sequence.number_next_actual)
          return next

     @api.model
     def create(self, vals):
          vals['codigo'] = self.env['ir.sequence'].next_by_code('cod.diario') or _('New')
          res = super(diario, self).create(vals)

          return res


