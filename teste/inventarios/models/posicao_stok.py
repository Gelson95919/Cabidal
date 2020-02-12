# -*- coding: utf-8 -*-

from odoo import models, fields, api

class posicaoStock(models.Model):
    _name = 'posicao.stock'
    _description = 'Posição de Stock'
    armazem = fields.Many2one('armanzem.armanzem', string="Armazem")
    familia = fields.Many2one('familia.familia', string="Familia")
    sub_familia = fields.Many2one('subfamilha.subfamilha', string="Sub Familia")
    tipo = fields.Selection([('porFamilia', 'Por Familia'), ('porNomeArtigo', 'Por Nome Artigo'), ('porCodigoArtigo', 'Por Codigo Aritigo')], default='porFamilia')
    somente_desponivel = fields.Boolean(string="Somente Desponiveis (Qt.> 0)")
    qt_abaixo_minimo = fields.Boolean(string="Qt.Abaixo do minimo")
    data = fields.Date(string="Data")
    posicastock = fields.One2many('artigo.artigo', 'id', string="Posicao stock")
