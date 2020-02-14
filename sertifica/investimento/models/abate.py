# -*- coding: utf-8 -*-

from odoo import models, fields, api

class abateImobilizado(models.Model):
     _name = 'abate.imobilizado'
     _description = "Abate Imobilizado"

     bem_id = fields.Many2one('adquisicao', string="Bem")
     codigo_patrimonial = fields.Integer(string="Código Patrimonial")
     valor_adquisicao = fields.Float(string="Valor Adquisção")
     valor_actual = fields.Float(string="Valor Actual")
     valor_amortizado = fields.Float(string="Valor Amortizado")
     motivo_abate_id = fields.Many2one('motivo.abate', string="Motivo")
     data_abater = fields.Date(string="Data  a Abater")
     valor_abate = fields.Float(string="Valor Abate")
     contabilizado = fields.Boolean(string="Contabilizado")
     diario = fields.Integer(string="Diario")
     numero = fields.Integer(string="Numero")

