# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class tarifaAlfandega(models.Model):
    _name = 'tarifa.alfandega'
    _rec_name = 'name'
    _description = 'Tarifa Alfândega'

    name = fields.Char()
    medida = fields.Selection([('hora', 'HORA'),('unidade', 'UNIDADE'),('volumen', 'VOLUMEN')])
    hora_igual = fields.Boolean()
    valor_fixo = fields.Boolean()
    servico_verificacao = fields.Float()
    servico_verificador = fields.Float()
    vitoria_outro_serv = fields.Float()
    outros = fields.Float()
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)


