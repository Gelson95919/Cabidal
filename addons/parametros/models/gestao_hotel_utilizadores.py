# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class utilizadores(models.Model):
    _name = 'utilizadores.utilizadores'
    _rec_name = 'name'
    _description = 'utilizadores'

    name = fields.Char(string="Descrição")
    utilizador = fields.Char()
    confirmar = fields.Char()
    palavra_passe = fields.Char()
    ativo = fields.Boolean()
    obs = fields.Text()
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)



