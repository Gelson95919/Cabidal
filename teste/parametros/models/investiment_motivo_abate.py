# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions

class motivoAbate(models.Model):
    _name = 'motivo.abate'
    _rec_name = 'name'
    _description = 'Motivo Abate'
    name = fields.Char(string="Descrição")
    conta_movimento = fields.Many2one('planconta.planconta')
    motivo_venda = fields.Boolean(string="Motivo Venda")
    conta = fields.Many2one('planconta.planconta', string="Conta")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

