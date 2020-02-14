# -*- coding: utf-8 -*-

from odoo import models, fields, api

class listagemPertences(models.Model):
    _name = 'listagem.pertences'
    _description = "Listagem Pertences"
    faturas_id = fields.Char(string="Faturas embarque") # Este campo nao e do campo dd tipo "char" mas sim Mane2one

class NewModule(models.Model):
    _name = 'pertences.cobrados'
    #_rec_name = 'name'
    _description = 'Pertences Cobrado'

    de = fields.Date(string="De", default=fields.Date.today)
    a = fields.Date(string="A", default=fields.Date.today)
    data_no_relatorio = fields.Boolean(string="Data no relatório")
