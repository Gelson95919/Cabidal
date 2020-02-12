# -*- coding: utf-8 -*-

from odoo import models, fields, api

class consultaContaCorrente(models.Model):
     _name = 'consulta.conta.corrente'
     _description = "Consulta Conta Corrente"
     ano = fields.Date(default=fields.Date.today)
     socio_id = fields.Many2one('terceiro.terceiro', string='Socio')
     #cont_corent_ids = fields.One2many('fatuclient.fatuclient', 'consulta_conta_corrente_id', oldname='detal_line', copy=True, store=True, auto_join=True)
     fatuclient_id = fields.Many2one('fatuclient.fatuclient', string="Clientes")

     def _comput_line(self, line):
          return {
               'displlay_type': line.displlay_type,
               'name': line.name,
               'state': 'draft',
          }

     @api.onchange('socio_id')
     def _onchange_socio_id(self):
         terms_obj = self.env['fatuclient.fatuclient'].search(
             [('terceiro_id', '=', self.socio_id.id), ('pago_control', '=', False),
              ('visualizar_no_tesorer', '=', True)])
         list_of_dict = []
         for line in terms_obj:
             data = self._comput_line(line)
             data.update(
                 {'name_control': line.name_control, 'pago_control': line.pago_control, 'date_control': line.date,
                  'acobrado_control': line.acobrado, 'total_resumo_control': line.total_resumo,
                  'saldo_control': line.saldo})
             list_of_dict.append((0, 0, data))
         return {'value': {"cont_corent_ids": list_of_dict}}
