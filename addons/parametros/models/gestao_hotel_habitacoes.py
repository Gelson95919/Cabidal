# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class habitacoes(models.Model):
    _name = 'habitacoes.habitacoes'
    _rec_name = 'name'
    _description = 'Habitações'

    name = fields.Char(string="Descrição")
    numero = fields.Char(string="Numero")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

