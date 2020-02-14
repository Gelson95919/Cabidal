# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class confcontabv(models.Model):

     _name = 'confcontabv.confcontabv'
     _description = 'Confirencia Contabilidade'
     #descricaoconfcont = fields.Char(string='Descrição')
     nao_contabilizados = fields.Boolean(string='Não Contabilizado')
     nao_na_razao = fields.Boolean(string='Não na Rão')
     data_inicial = fields.Date(string='Data Inicial')
     data_final = fields.Date(string='Data Final')
     interno = fields.Integer(string='Interno')
     data = fields.Date(string='Data')
     numero = fields.Integer(string='Numero')
     nome = fields.Char (string='Nome')
     montante = fields.Integer(string='Montante')
     diario = fields.Integer(string='Diario')
     ordem = fields.Char(string='Ordem')
     razao = fields.Char(string='Razão')

     conf_contab = fields.One2many('confcontabv.confcontabv', 'id', string='detal', oldname='detal_line')




