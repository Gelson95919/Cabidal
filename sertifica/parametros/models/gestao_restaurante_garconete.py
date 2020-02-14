# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class garconete(models.Model):
    _name = 'garconete.garconete'
    _rec_name = 'name'
    _description = 'Garçonete'

    name = fields.Char(string="")
    nome = fields.Char()
    activo = fields.Boolean()
    pin = fields.Integer()
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)



