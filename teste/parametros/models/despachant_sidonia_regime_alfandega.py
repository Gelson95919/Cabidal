# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class regimeAlfandega(models.Model):
    _name = 'regime.alfandega'
    _rec_name = 'name'
    _description = 'Regime Alfândega'

    name = fields.Char()
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)



