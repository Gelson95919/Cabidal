# -*- coding: utf-8 -*-

from odoo import models, fields, api

class extractos(models.Model):
    _name = 'extracto.extracto'
    #_rec_name = 'name'
    _description = 'Extracto'

    por = fields.Selection([('porconta', 'Por Conta'), ('porterceiro', 'Por Terceiro'), ('porcentrocusto','Por Centro de Custo'), ], string='por', default='porconta')
    data_in = fields.Date(string='Data inicial')
    data_fin = fields.Date(string='Data Final')
    data_de = fields.Date(string='De')
    data_ate = fields.Date(string='Ate')
    inter_mes = fields.Selection([('todos', 'Todos'), ('intervalo', 'Intervalo')], string='Mes', default='todos')
    nadaver=fields.Date(string='De', readonly=True,)
    mudar_pagina=fields.Boolean(string='Mudar Pagina')
    moeda_estrangeiro = fields.Boolean(string='Moeda Estrangeiro')
    conta_inicial = fields.Many2one('planconta.planconta', string='Conta Inicial')
    conta_final = fields.Many2one('planconta.planconta', string='Conta Final')
    cod_inter_altern = fields.Selection(
        [('intervalo', 'Intervalo'),
         ('alternado', 'Alternado')],
        string='por', default='intervalo')
    inter_de = fields.Many2one('planconta.planconta', string='Data inicial')
    inter_ate = fields.Many2one('planconta.planconta', string='Data Final')
    campo_alterna = fields.Many2many('planconta.planconta', string='Alternado')