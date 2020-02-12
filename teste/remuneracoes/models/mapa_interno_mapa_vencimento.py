# -*- coding: utf-8 -*-

from odoo import models, fields, api

class mapaVencimento(models.Model):
      _name = 'mapa.vencimento'
      _description = 'Mapa Vencimentos'
      data = fields.Date(string="Data")
      departamento = fields.Many2one('departamento.area', string="Area Departamento")
      todos = fields.Boolean(string="Todas")
      por_departamento = fields.Boolean(string="Por Departamento")
      uma_folha_por_departamento = fields.Boolean(string="Uma Folha Por Departamento")

