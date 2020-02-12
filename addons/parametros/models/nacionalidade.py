# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class nacionalidade(models.Model):
     _name = 'nacionalidade.nacionalidade'
     _description = 'Nacionalidade'
     nacionalidad = fields.Char('Nacionalidade', required=True)
     pais_id = fields.Many2one('pais.pais', string="País")
     indicativo_id = fields.Char(string="Indicativo") #para Ver
     #ISO_A2 = fields.Char(string='ISO_A2')
     #ISO_N3 = fields.Integer(string='ISO_N3')
     #ISO_A3 = fields.Char(string='ISO_A3')
     #FIPS = fields.Char(string='FIPS')
     #desc = fields.Text()
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)



