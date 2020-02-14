# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class responsaves(models.Model):
     _name = 'responsaves.responsaves'
     _description = 'Responsaves'
     name = fields.Char('Descrição', required=True)

     morada = fields.Char(string='Morada')
     cargo = fields.Many2one('profissoes.profissoes', string='Cargo')
     telefone = fields.Integer(string='Telefone')
     telemovel = fields.Integer(string='Telemóvel')
     email = fields.Char(string="E-mail")
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)


