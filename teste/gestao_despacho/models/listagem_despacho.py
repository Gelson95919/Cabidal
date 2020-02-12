# -*- coding: utf-8 -*-

from odoo import models, fields, api

class listagem_Despachos(models.Model):
     _name = 'listagem.despachos'
     _description = "Listagem Despacho"
     tipo = fields.Selection([('listagem_total', 'Listagem Total'), ('listagem_recibo_gerado', 'Listagem Recibo Gerado')
                              ], default="listagem_total")
     em_aberto = fields.Boolean(string="Em Aberto")
     por_beneficiario = fields.Boolean(string="Por Beneficiario")
     terceiro_id = fields.Many2one('terceiro.terceiro', string="Benificiario")
     uma_folha_por_beneficiario = fields.Boolean(string="Uma Folha Por Beneficiario")
     data_de = fields.Date(string="Data de")
     data_ate = fields.Date(string="Data ate")
