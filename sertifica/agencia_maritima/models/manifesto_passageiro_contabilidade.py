# -*- coding: utf-8 -*-

from odoo import models, fields, api

class manifestoPassageiroContabilizado(models.Model):
     _name = 'manifesto.passageiro.contabilizado'
     _description = "Manifesto de Passageiro-Contabilizado"
     navio_id = fields.Many2one('navios.navios', string="Navio")
     viagem_id = fields.Many2one('registro', string="Registro")
     incluir_data_recebimento = fields.Boolean(string="Incluir Data")
     porto_id_o = fields.Many2one('portos.escalas', string="Origem")
     porto_id_d = fields.Many2one('portos.escalas', string="Destino")
