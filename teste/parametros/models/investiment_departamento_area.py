# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions

class departamentoArea(models.Model):
    _name = 'departamento.area'
    _rec_name = 'name'
    _description = 'Departamento/Area'
    name = fields.Char(string="Descrição")
    centro_custo = fields.Many2one('planconta.planconta', string="C.Custo")
    abreviatura = fields.Char(string="Abreviatura")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)


