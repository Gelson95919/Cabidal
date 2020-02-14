# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class tarifaEnapor(models.Model):
    _name = 'tarifa.enapor'
    _rec_name = 'name'
    _description = 'Tarifa Enapor'

    name = fields.Char(string="Descrição")
    name2 = fields.Char(string="Descrição 2")
    unid_medida = fields.Many2one('unimedida.unimedida')
    tarifa_por_entervalo_valores = fields.Boolean()
    tarifa = fields.Float()
    tarifa_x_cdia_extra = fields.Float()

    medida_maxima= fields.Char(string="MEDIDA MAXIMA")
    medida_minima = fields.Char(string="MEDIDA MINIMA")
    taxa = fields.Char(string="TAXA")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

    mult = fields.One2many('tarifa.enapor','id')


