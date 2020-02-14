# -*- coding: utf-8 -*-

from odoo import models, fields, api

class declaracaoValores(models.Model):
     _name = 'declaracao.valores'
     _description = "Declaração de Valores"
     aalfandiga_de = fields.Char(string="")
     campo_1 = fields.Char(string="")
     campo_2 = fields.Char(string="")
     declarante = fields.Char()
     designacao = fields.Text()
     volumes = fields.Float()
     meio_transporte = fields.Char()
     tipo_propriedade = fields.Char()
     procedencia = fields.Char()
     valor_fob = fields.Integer()
     fret = fields.Integer()
     seguro = fields.Integer()
     data = fields.Date()
     regime = fields.Integer()
     dbn = fields.Integer()
     campo_3 = fields.Integer()
     campo_4 = fields.Integer()
     num_copia = fields.Integer()