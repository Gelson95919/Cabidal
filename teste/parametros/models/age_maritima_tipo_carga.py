# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class tipoCarga(models.Model):
    _name = 'tipo.carga'
    _rec_name = 'name'
    _description = 'Tipo Carga'

    name = fields.Char(string="Carga")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

