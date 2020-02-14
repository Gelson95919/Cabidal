# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class combustivel(models.Model):
    _name = 'combustivel.combustivel'
    _rec_name = 'name'
    _description = 'Combustivel'

    name = fields.Char(string="Combustivel")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

