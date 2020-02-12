# -*- coding: utf-8 -*-

from odoo import models, fields, api

class feixoCaixa(models.Model):
      _name = 'feixo.caixa'
      _description = 'Fecho Caixa Hotel'
      caixa = fields.Char(string="Caixa")
      operador = fields.Char(string="Operador")
      movimento = fields.Char(string="Movimento")
      turno = fields.Char(string="Turno")
      data = fields.Date(string="Data")
      checkin_ids = fields.One2many('reserva', 'feixo_caixa_id', string="Check-in")

      def _comput_line(self, line):
          return {
              'displlay_type': line.displlay_type,
              'name': line.name,
              'state': 'draft',
          }

      def selecionar(self):
          terms_obj = self.env['reserva']
          list_of_dict = []
          for line in terms_obj:
              data = self._comput_line(line)
              data.update(
                  {'habitacao_id': line.habitacao_id, 'montante_check_kin': line.montante_check_kin, 'cliente_ids': line.cliente_ids, 'start_date': line.start_date,
                   'end_date': line.end_date})
              list_of_dict.append((0, 0, data))
          return {'value': {"checkin_ids": list_of_dict}}