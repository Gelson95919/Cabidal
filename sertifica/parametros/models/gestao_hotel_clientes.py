# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class clientes(models.Model):
    _name = 'clientes.clientes'
    _rec_name = 'name'
    _description = 'Clientes'

    name = fields.Char(string="Descrição")
    endereco = fields.Char(string="endereco")
    pais = fields.Many2one('nacionalidade.nacionalidade')
    e_mail = fields.Char()
    notas = fields.Text()

    reserva_id = fields.Many2one('reserva', string="Reserva")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)
