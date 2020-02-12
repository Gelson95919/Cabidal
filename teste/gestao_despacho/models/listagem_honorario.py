# -*- coding: utf-8 -*-

from odoo import models, fields, api

class listagemsRubros(models.Model):
    _name = 'listagems.rubros'
    _description = "Listagens de Rubros"
    rubrica_alfandega = fields.Boolean(string="Rubrica de Alfandega")
    rubrica_alfandega_id = fields.Many2one('')
    terceiro_id = fields.Many2one('terceiro.terceiro', string="Beneficiario")
    de_pagamento = fields.Boolean(string="De Pagamento")
    data_de = fields.Date(string="De")
    data_ate = fields.Date(string="Ate")
