# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class pais(models.Model):
    _name = 'pais.pais'
    _rec_name = 'nome_internacional'
    _description = 'País'

    nome_internacional = fields.Char(string="Nome Internacional")#Nome INT
    cod_alfa_2 = fields.Char(string="Codigo Alfa2") #ISO_A2
    cod_alfa_3 = fields.Char(string="Codigo Alfa3") #ISO_A3
    cod_numerico = fields.Char(string="Codigo Numerico3") #ISO_N3
    fips = fields.Char(string="FIPS")  # FIPS
    nome_ES = fields.Char(string="Nome ES")  # Nome ES
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)


