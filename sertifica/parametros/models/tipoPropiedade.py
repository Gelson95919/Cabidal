# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class tipopropiedade(models.Model):
     _name = 'tipopropiedade.tipopropiedade'
     _description = 'Tipo Propiedade'
     name = fields.Char(string='Descrição', required=True)
     desc = fields.Text(string="Descrição")
     permite_public_em_armanze = fields.Boolean(string="Permitir Duplicar em Armanzem")
     propiedade_com_tabela_associada = fields.Boolean(string = "Propiedade com Tabela Associada")
     associa = fields.One2many('tipopropiedade.tipopropiedade', 'id', string='Outros', oldname='outros_line')
     cod = fields.Integer('Codigo')
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

