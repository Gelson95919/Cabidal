# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class curso(models.Model):
    _name = 'curso.curso'
    _rec_name = 'name'
    _description = 'Curso'

    name = fields.Char()
    valor_matricula = fields.Float()
    prestacoes = fields.Integer()
    valor_anual = fields.Float()
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)









