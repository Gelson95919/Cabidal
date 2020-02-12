# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
import math
from odoo import api, fields, models, tools, _

_logger = logging.getLogger(__name__)

class moeda(models.Model):

     _name = 'moeda.moeda'
     _description = 'Moeda'

     name = fields.Char('Descrição', required=True)
     codigo = fields.Char(string="Codigo", required=True, copy=False, readonly=True, index=True,
                          default=lambda self: self._get_next_cod(), store=True, )
     simbolo = fields.Char('Símbolo')
     abreviatura = fields.Char('Abreviatura')
     aredondamento = fields.Selection(
          [('1', 'Unidade'), ('2', 'Décimas'),  ('3', 'Dezenas unidade'), ('4', 'Centenas unidade'), ('5', 'Centésimas'), ('6', 'Milhares unidade'),],
          'Tipo Movimento', Widget="radio", default="decimais")
     inteiro = fields.Char('Inteiro')
     decimal = fields.Char('Decimal')
     moeda_base= fields.Boolean('Moeda Base')
     cambio_fixo = fields.Boolean('Câmbio Fixo')
     decimal_places = fields.Integer(compute='_compute_decimal_places', store=True)

     tipo = fields.Selection(
          [('3', 'superior'), ('1', 'Sem Arredondamento'), ('2', 'Defeito'),
           ('4', ' Inferior'), ],
          'Tipo', default="3")
     cambio = fields.One2many('cambio', 'moeda_id', string='cambio')
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

     @api.model
     def _get_next_cod(self):
         sequence = self.env['ir.sequence'].search([('code', '=', 'moeda.codigo')])
         next = sequence.get_next_char(sequence.number_next_actual)
         return next

     @api.model
     def create(self, vals):
         vals['codigo'] = self.env['ir.sequence'].next_by_code('moeda.codigo') or _('New')
         res = super(moeda, self).create(vals)

         return res


class cambio(models.Model):
    _name = 'cambio'
    #_rec_name = 'name'
    _description = 'Cambio'

    data = fields.Date(string="Data")
    montante = fields.Float(string="Montante")
    moeda_id = fields.Many2one('moeda.moeda')

