# -*- coding: utf-8 -*-

from odoo import models, fields, api

class mapasOficiaissindicatos(models.Model):
      _name = 'mapas.oficiais.sindicatos'
      _description = 'Mapas Oficiais Sindicatos'
      data = fields.Date(string="Data")
      por = fields.Boolean(string="Por Area Departamento")
      area_departamento = fields.Char(string="Area Departamento")
      de_sindicatos_id = fields.Many2one('sindicato.sindicato', string="De")
      ate_sindicatos_id = fields.Many2one('sindicato.sindicato', string="Ate")

