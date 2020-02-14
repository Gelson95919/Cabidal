# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions

class amortizacaoGestao(models.Model):
    _name = 'amortizacao.gestao'
    _rec_name = 'name'
    _description = 'Amortização Gestão'
    name = fields.Char(string="Descrição")
    taxa = fields.Float(string="Taxa")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)


