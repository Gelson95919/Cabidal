# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class horasRemuneracoes(models.Model):
    _name = 'horas.remuneracoes'
    _rec_name = 'name'
    _description = 'Horas Remuneração'

    name = fields.Char()
    complementar = fields.Boolean()
    detalhes = fields.One2many('horas.remuneracoes', 'id')
    hora_formula = fields.Char(string="Hora/Formula")
    condicao = fields.Char(string="Condição")
    quantidade = fields.Float(string="Quantidade(Qt")
    sequencia = fields.Integer(default=10, help="Dá a seqüência desta linha ao exibir a Detalhes.")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)


