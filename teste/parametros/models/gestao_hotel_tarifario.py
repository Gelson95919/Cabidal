# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class tarifario(models.Model):
    _name = 'tarifario.tarifario'
    _rec_name = 'name'
    _description = 'Tarifário'

    name = fields.Char(tring="Nome")
    montante = fields.Float()
    iva = fields.Float()
    num_ocupam= fields.Float()
    cod_fact = fields.Many2one('fatura.fatura')
    no_taxa_turistica = fields.Boolean()
    adulto= fields.Float()
    crianca= fields.Float()
    incluir_pequeno_almoco= fields.Boolean()
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)
