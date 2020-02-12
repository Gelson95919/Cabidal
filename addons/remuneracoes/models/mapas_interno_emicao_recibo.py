# -*- coding: utf-8 -*-

from odoo import models, fields, api

class emicaoRecibo(models.Model):
      _name = 'emicao.recibo'
      _description = 'Emissão Recibo'
      data = fields.Date(string="Data")
      por = fields.Boolean(string="Por Area Departamento")
      area_departamento = fields.Many2one('departamento.area', string="Area Departamento")
      de_funcionario_id = fields.Many2one('funcionario.remuneracoes', string="De")
      ate_funcionario_id = fields.Many2one('funcionario.remuneracoes', string="Ate")

