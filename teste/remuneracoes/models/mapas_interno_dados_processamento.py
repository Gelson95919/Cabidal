
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class dadosProcessamento(models.Model):
    _name = 'dados.processamento'
    _description = 'Dados Processamento'
    tipo_dados = fields.Selection([('remuneracoes', 'Remunerações'), ('hora_extra', 'Horas Extras'), ('descontos', 'Descontos'), ('faltas', 'Faltas')], default="remuneracoes")
    remuneracoes = fields.Many2many('remuneracoes.remuneracoes', string="Remunerações")
    horas_extras = fields.Many2many('horas.extras', string="Horas Extras")
    descontos = fields.Many2many('desconto.desconto', string="Descontos")
    faltas = fields.Many2many('faltas.faltas', string="Faltas")
    de = fields.Date(string="De")
    ate = fields.Date(string="Ate")
    corte_pagina = fields.Boolean(string="Corte de Paginas")
    detalhe_por_funcionario = fields.Boolean(string="Ditalhe por Funcionario")

