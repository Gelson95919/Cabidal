# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class tipoConsumo(models.Model):
    _name = 'tipo.consumo'
    _rec_name = 'name'
    _description = 'Tipo Consumo'

    name = fields.Char(tring="Nome")
    montante = fields.Float()
    iva_percent = fields.Many2one('iva.iva')
    cod_factura = fields.Many2one('fatura.fatura')
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)
