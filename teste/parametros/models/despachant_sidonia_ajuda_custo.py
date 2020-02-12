# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class ajudaCusto(models.Model):
    _name = 'ajuda.custo'
    _rec_name = 'name'
    _description = 'Ajuda de Custo'

    name = fields.Char()
    quantidade = fields.Float()
    condicao = fields.Selection([('=', '='),('>', '>'),('<', '<'),('>=', '>='),('<=', '<=')])
    verificador = fields.Float()
    recerificador = fields.Float()
    auxiliar = fields.Float()
    outro = fields.Float()
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)


