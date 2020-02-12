# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class freteCabotagem(models.Model):
    _name = 'frete.cabotagem'
    #_rec_name = 'name'
    _description = 'Frete Cabotagem'

    origem = fields.Many2one('portos.escalas')
    destino = fields.Many2one('portos.escalas')
    taxa_m3_fr = fields.Float()
    taxa_m3_ad = fields.Float()
    taxa_tons_fr = fields.Float()
    taxa_tons_ad = fields.Float()
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

