# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions

class amortizacoaPorteria(models.Model):
    _name = 'amortizacoa.portuaria'
    _rec_name = 'name'
    _description = 'Amortização Porteria'
    name = fields.Char(string="Descrição")
    adquisicao = fields.Many2one('planconta.planconta')
    grupo = fields.Boolean(string="Grupo")
    amort_acomulada = fields.Many2one('planconta.planconta')
    amort_exerc = fields.Many2one('planconta.planconta')
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

