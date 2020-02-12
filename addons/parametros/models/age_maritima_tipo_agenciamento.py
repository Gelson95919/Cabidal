# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class tipoAgenciamento(models.Model):
    _name = 'tipo.agenciamento'
    _rec_name = 'name'
    _description = 'Tipo Agenciamento'

    name = fields.Char(string="Agenciamento")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

