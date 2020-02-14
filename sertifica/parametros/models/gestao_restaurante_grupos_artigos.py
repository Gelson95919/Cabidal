# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class gruposArtigos(models.Model):
    _name = 'grupos.artigos'
    _rec_name = 'name'
    _description = 'Grupos Artigo'

    name = fields.Char(string="")
    grupo = fields.Integer()
    activo = fields.Boolean()
    ordem = fields.Integer()
    image = fields.Binary()
    impressora = fields.Many2one('impressoras.impressoras')
    associados = fields.Many2many('artigo.artigo', string="Artigo")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

