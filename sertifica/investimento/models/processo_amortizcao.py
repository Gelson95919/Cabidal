# -*- coding: utf-8 -*-

from odoo import models, fields, api

class processoAmortizacao(models.Model):
     _name = 'processo.amortizacao'
     _description = "Processo amortização"
     data = fields.Date(string="Data")
     acumular_meses = fields.Boolean(stirng="Acumular meses anteriores")
     selecionar_tudos = fields.Boolean(string="Selecionar todus")
     data_amort = fields.Date(string="Data")
     contabilizado = fields.Boolean(string="Contabilizado")
     diario = fields.Integer(string="Diario")
     numero = fields.Integer(string="Numreo")
     amortizados_ids = fields.One2many('amortizados', 'processo_amortizacao_id')

class amortizados(models.Model):
    _name = 'amortizados'
    #_rec_name = 'name'
    _description = 'Amortizados Inventario'

    cod = fields.Integer(string="Código")
    nome = fields.Char(string="Nome")
    valor = fields.Float(string="Valor")
    selec = fields.Boolean(string="Selec")
    processo_amortizacao_id = fields.Many2one('processo.amortizacao', string="Processo amortização")



