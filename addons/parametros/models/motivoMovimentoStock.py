# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class movimentostok(models.Model):
     _name = 'movimentostok.movimentostok'
     _description = 'Movimento Stok'
     name = fields.Char(string='Descrição', required=True)
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)


