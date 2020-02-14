# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class tipoReserva(models.Model):
    _name = 'tipo.movimento'
    _rec_name = 'name'
    _description = 'Tipo Reserva'

    name = fields.Char(string="Descrição")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

