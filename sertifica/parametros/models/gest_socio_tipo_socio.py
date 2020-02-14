# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class tipoSocios(models.Model):
    _name = 'tipo.socios'
    _rec_name = 'name'
    _description = 'Tipo Sócios'

    name = fields.Char(string="Nome")
    valor_joia = fields.Float()
    quota_menasl = fields.Float()
    cod_faturacao = fields.Many2one('produto.produto')
    conta = fields.Many2one('planconta.planconta')
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)
