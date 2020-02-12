# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class anoLectivo(models.Model):
    _name = 'ano.lectivo'
    _rec_name = 'name'
    _description = 'Ano Lectivo'

    name = fields.Char(string="Descricao")
    fecho = fields.Boolean()
    detalhes = fields.One2many('detalhes', 'ano_lectivo_id')
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)




class detalhes(models.Model):
    _name = 'detalhes'
    #_rec_name = 'name'
    _description = 'Detalhes Ano letivo'

    data = fields.Date(string="Data")
    descricao = fields.Char(string="Descrição")
    numero = fields.Integer(string="Numero")
    ano_lectivo_id = fields.Many2one('ano.lectivo', string="Ano Lectivo")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)
