# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class motivoEscala(models.Model):
    _name = 'motivo.escala'
    _rec_name = 'name'
    _description = 'Motivo Escala'

    name = fields.Char(string="Motivo")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

