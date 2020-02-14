# -*- coding: utf-8 -*-

from odoo import models, fields, api

class selagemMercadoria(models.Model):
     _name = 'selagem.mercadoria'
     _description = "Selagem de Mercadoria"
     campo_1 = fields.Char()
     campo_2 = fields.Char()
     campo_3 = fields.Char()
     campo_4 = fields.Char()
     campo_5 = fields.Char()
     campo_6 = fields.Char()
     campo_7 = fields.Date()
     campo_8 = fields.Char()
     alfandiga_praia = fields.Date()
     obs = fields.Text()
     campo_9 = fields.Char()
     num_copia = fields.Integer()
     mercadoria_ids = fields.One2many('mercadoria.selado', 'selagem_mercadoria_id', string="Mercadoria")

class mercadoria(models.Model):
    _name = 'mercadoria.selado'
    #_rec_name = 'name'
    _description = 'Mercadoria'

    quantidades = fields.Char(string="Unidades a selar-Quantidade")
    qualidades = fields.Char(string="Unidades a selar-Qualidade")
    designacao_mercadoria = fields.Char(string="Designação mercadoria")
    marca = fields.Char(string="Marca")
    preco_instanmpilha_por_unidade = fields.Integer(string="Preço da estampilha por unidade")
    importancia = fields.Char(string="Importância")
    selagem_mercadoria_id = fields.Many2one('selagem.mercadoria', string="Selagem de Mercadoria")
