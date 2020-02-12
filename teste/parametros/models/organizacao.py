# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class organizacao(models.Model):
     _name = 'organizacao.organizacao'
     _description = 'Organização'
     name = fields.Char('Descrição', required=True)
     C_Custo = fields.Many2one('planconta.planconta', string='C.Custo')
     Abreviatura = fields.Char(string='Abreviatura')
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)



