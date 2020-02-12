# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class valorDescarga(models.Model):
    _name = 'valor.descarga'
    _rec_name = 'name'
    _description = 'Valor de Descarga'

    name = fields.Char(string="Clase")
    porto = fields.Many2one('portos.escalas')
    criterio = fields.Selection([('med', 'MED.(M3)'), ('peso', 'PESO(KG)'), ('pessoal', 'PESSOAL'), ('velumem', 'VOLUMEN')],)
    valor_inicia = fields.Float()
    valor_final = fields.Float()
    taxa = fields.Float()
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)


