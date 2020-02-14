# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class passagemMaritima(models.Model):
    _name = 'passagem.maritima'
    _rec_name = 'name'
    _description = 'Passagem Inter Ilhas'

    name = fields.Char(string="Nome")
    origem = fields.Many2one('portos.escalas')
    destino = fields.Many2one('portos.escalas')
    tarifa_base = fields.Float()
    agencia = fields.Float()
    selos = fields.Float()
    impressos = fields.Float()
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

