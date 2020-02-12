# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class reparticaoFinanca(models.Model):
    _name = 'reparticao.financa'
    _rec_name = 'name'
    _description = 'Repartição Finanças'

    name = fields.Char(string="Nome")
    codigo = fields.Char(string="codigo")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)


