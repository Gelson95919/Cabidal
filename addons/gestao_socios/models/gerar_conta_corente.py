# -*- coding: utf-8 -*-

from odoo import models, fields, api

class gerarContaCorente(models.Model):
     _name = 'gerar.conta.corente'
     _description = "Gerar Conta Corente"
     ano = fields.Date(string="Ano")
     mes = fields.Date(string="Mês")
     membros_ativos = fields.Boolean(string="Membros Activos")
     data_contabilizacao = fields.Date(string="Data Contabilização", default=fields.Date.today)
     conceuto = fields.Char(string="Conceito")
     selecionar_tuto = fields.Boolean(string="Selecionar Tudo")
     socios_ids = fields.One2many('socios.socios', 'gerar_conta_corente_id', oldname='detal_line', copy=True, store=True, auto_join=True)

     def _comput_line(self, line):
         return {
             'displlay_type': line.displlay_type,
             'name': line.name,
             'state': 'draft',
         }


     def selecionar(self):
         terms_obj = self.env['socios.socios']#.search(
             #[('terceiro_id', '=', self.socio_id.id), ('pago_control', '=', False), ('date', '=', self.ano),
              #('visualizar_no_tesorer', '=', True)])
         list_of_dict = []
         for line in terms_obj:
             data = self._comput_line(line)
             data.update(
                 {'numero_socio': line.numero_socio, 'name': line.name, 'tipo': line.tipo,
                  'activo': line.activo})
             list_of_dict.append((0, 0, data))
         return {'value': {"socios_ids": list_of_dict}}
