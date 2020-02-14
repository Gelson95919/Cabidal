# -*- coding: utf-8 -*-

from odoo import models, fields, api

class parametros(models.Model):
     _name = 'parametros.parametros'

     modulo = fields.Char(string="Modulo")
     variavel = fields.Char(string="Variavel")
     tipo = fields.Char(string="Tipo")
     valor = fields.Char(string="Valor")
     len = fields.Char(string="Tamanho")
