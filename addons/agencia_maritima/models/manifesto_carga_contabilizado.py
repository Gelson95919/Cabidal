# -*- coding: utf-8 -*-

from odoo import models, fields, api

class manifestoCargaContabilizado(models.Model):
     _name = 'manifesto.carga.contabilizado'
     _description = "Manifesto de Carga-Contabilizado"
     navio_id = fields.Many2one('navios.navios', string="Navio")
     viagem_id = fields.Many2one('registro', string="Registro")
     culuna_piacao = fields.Boolean(string="Piacao")
