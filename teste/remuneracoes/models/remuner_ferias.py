
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ferias(models.Model):
    _name= 'ferias.ferias'
    _description = 'Férias'
    ano_ferias = fields.Date(string="Ano Ferias")
    ano_processo = fields.Date(string="Ano processo")
    a_processar =fields.Float(string="% a Processar")
    consider_remuner = fields.Boolean(string = "Conciderar Somente Remuneracoes Base")
    consider_proporcional = fields.Boolean(string="Considerar proporcional Data de Ingresso ou case")
