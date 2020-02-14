# -*- coding: utf-8 -*-

from odoo import models, fields, api

class plaformaPlanoCarga(models.Model):
    _name = 'plaforma.plano.carga'
    _description = "Plaforma Plano Carga"
    fretador_id = fields.Many2one('terceiro.terceiro', string="Armador")
    navio_id = fields.Many2one('navios.navios', string="Navio")
    porto1_id = fields.Many2one('portos.escalas', string="Origem")
    porto2_id = fields.Many2one('portos.escalas', string="Destino")
    data_chegada = fields.Datetime(string="Data Chegada")
    calado = fields.Float(string="Calado")
    motivo_escala_id = fields.Many2one('motivo.escala', string="Escala")
    contracto = fields.Selection(
        [('liner', 'Liner'), ('liner_out', 'Liner Out'), ('full_liner', 'Full Liner'), ('fios', 'Fios')],
        default="liner")
    remitente = fields.Char(string="Remetente")
