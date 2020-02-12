# -*- coding: utf-8 -*-

from odoo import models, fields, api

class manifestoCargaDescretivo(models.Model):
     _name = 'manifesto.carga.descretivo'
     _description = "Manifesto de Carga-Descretivo"
     navio_id = fields.Many2one('navios.navios', string="Navio")
     viagem_id = fields.Many2one('registro', string="Registro")
     so_carga_cativa = fields.Boolean(string="So Carga Cativa")
     ficheiro_xml = fields.Boolean(string="Ficheiro XML")
     porto_id_o = fields.Many2one('portos.escalas', string="Origem")
     porto_id_d = fields.Many2one('portos.escalas', string="Destino")
