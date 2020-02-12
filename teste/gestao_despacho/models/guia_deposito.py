# -*- coding: utf-8 -*-

from odoo import models, fields, api

class guiaDeposito(models.Model):
     _name = 'guia.deposito'
     _description = "Guia de Entrada"
     campo_a_1= fields.Char(string="a")
     esc = fields.Integer(string="Esc")
     cabecalho = fields.Boolean(string="Cabeçalho")
     campo_1 = fields.Char(string="")
     campo_2 = fields.Char(string="")
     campo_3 = fields.Char(string="")
     campo_4 = fields.Char(string="")
     campo_5 = fields.Char(string="")
     campo_6 = fields.Char(string="")
     campo_7 = fields.Char(string="")
     campo_8 = fields.Char(string="")
     campo_9 = fields.Char(string="")
     campo_10 = fields.Char(string="")
     num_copia = fields.Integer(string="Numero Conta")
     verso = fields.Boolean(string="Verco")
