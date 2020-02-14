# -*- coding: utf-8 -*-

from odoo import models, fields, api

class relatoriMotivo(models.Model):
     _name = 'relatorio.motivo'
     _description = 'Relatorio Motivo Saida/Entrada Stock'
     motivo= fields.Many2one('movimentostok.movimentostok', string="Motivo")
     data_inicio=fields.Date(string='Data Inicio')
     data_fim = fields.Date(string='Data Fim')
     artigo_id = fields.Many2one('artigo.artigo', string="Artigo")

