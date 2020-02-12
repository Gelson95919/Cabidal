# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class qualidadeMercadoria(models.Model):
    _name = 'qualidade.mercadoria'
    _rec_name = 'name'
    _description = 'Qualidade Mercadoria'

    name = fields.Char(string="Mercadoria")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

