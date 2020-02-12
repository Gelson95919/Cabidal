# -*- coding: utf-8 -*-

from odoo import models, fields, api

class autorizacaoSaida(models.Model):
     _name = 'autorizacao.saida'
     _description = "Autorização de Saida"
     num_ordem= fields.Integer()
     data = fields.Date()
     merca = fields.Char()
     em = fields.Char()
     pl_1 = fields.Char()
     pl_2 = fields.Char()
     pl_3 = fields.Char()
     contetor_1 = fields.Char()
     contetor_2 = fields.Char()
     contetor_3 = fields.Char()
     contetor_4 = fields.Char()
     contetor_5 = fields.Char()
     contetor_6 = fields.Char()
     contetor_7 = fields.Char()
     contetor_8 = fields.Char()
     contetor_9 = fields.Char()
     contetor_10 = fields.Char()
     num_copia = fields.Integer()

