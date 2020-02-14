# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class portosEscalas(models.Model):
    _name = 'portos.escalas'
    _rec_name = 'name'
    _description = 'Portos Escalas'

    name = fields.Char(string="Nome")
    porto_nacional = fields.Boolean(string="Porto Nacional")
    indicaativo = fields.Many2one('nacionalidade.nacionalidade', string="Indicativo")
    pais = fields.Many2one('nacionalidade.nacionalidade', string="Pais")
    telefone = fields.Integer(string="Telefone")
    fax = fields.Integer(string="Fax")
    email = fields.Integer(string="E-mail")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)
