# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class tipoPagamento(models.Model):
    _name = 'tipo.pagamento'
    _rec_name = 'name'
    _description = 'Tipo Pagamentos'

    name = fields.Char(string="Descrição")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

