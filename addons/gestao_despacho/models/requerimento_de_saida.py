# -*- coding: utf-8 -*-

from odoo import models, fields, api

class requerimentoSaidaMercadoriaDemorada(models.Model):
     _name = 'requerimento.saida.mercadoria.demorada'
     _description = "Requerimento de Saida Mercadoria Demorada"
     num_ordem = fields.Integer()
     data = fields.Date()
     abaixao = fields.Char()
     quant_vols_1 = fields.Float()
     quant_vols_2 = fields.Float()
     marcas_num = fields.Integer()
     vindos_de = fields.Char()
     no_navio_aviao = fields.Char()
     entrado_em = fields.Char()
     sob_a_cm_fiscal = fields.Char()
     consignado = fields.Char()
     com_valor_total_de = fields.Char()
     num_copia = fields.Char()
     bl_ou_lta_n = fields.Char()

