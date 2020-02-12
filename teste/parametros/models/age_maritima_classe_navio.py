# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class classeNavio(models.Model):
    _name = 'classe.navio'
    _rec_name = 'name'
    _description = 'classe Navio'

    name = fields.Char(string="Clase")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)


