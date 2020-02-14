# -*- coding: utf-8 -*-

from odoo import models, fields, api

class mapasOficiaisSeguros(models.Model):
      _name = 'mapas.oficiais.seguros'
      _description = 'Mapas Oficiais Seguros'
      data = fields.Date(string="Data")
      por = fields.Boolean(string="Por Area Departamento")
      area_departamento = fields.Char(string="Area Departamento")
      de_seguro_id = fields.Many2one('seguros.seguros', string="De")
      ate_siguro_id = fields.Many2one('seguros.seguros', string="Ate")

