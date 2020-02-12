# -*- coding: utf-8 -*-

from odoo import models, fields, api

class mapasOficiaisReparticao(models.Model):
      _name = 'mapas.oficiais.reparticao'
      _description = 'Mapas Oficiais Imposto Unico de Rendimento'
      data = fields.Date(string="Data")
      de_reparticao_id = fields.Many2one('reparticao.financas', string="De")
      ate_reparticao_id = fields.Many2one('reparticao.financas', string="Ate")

