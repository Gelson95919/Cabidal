# -*- coding: utf-8 -*-

from odoo import models, fields, api

class mapasOficiaisSegurancaSocial(models.Model):
      _name = 'mapas.oficiais.seguranca.social'
      _description = 'Mapas Oficiais Seguranças Social'
      data = fields.Date(string="Data")
      imprimir_modelo_oficial = fields.Boolean(string="Imprimir")
      de_seguranca_social_id = fields.Many2one('seguranca.social', string="De")
      ate_seguranca_social_id = fields.Many2one('seguranca.social', string="Ate")
      notas = fields.Text(string="Notas")

