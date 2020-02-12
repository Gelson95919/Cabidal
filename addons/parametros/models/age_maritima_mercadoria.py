# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class mercadoria(models.Model):
    _name = 'mercadoria'
    _rec_name = 'name'
    _description = 'Mercadoria'

    name = fields.Text(string="Mercadoria")
    cubicagem = fields.Float(string="Cubicagem M³")
    peso = fields.Float(string="Peso Kg")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

