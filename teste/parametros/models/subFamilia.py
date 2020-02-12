# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class subfamilha(models.Model):
     _name = 'subfamilha.subfamilha'
     _description = 'Subfamilia'
     name = fields.Char(string='Descrição', required=True)
     familia = fields.Many2one('familia.familia', string='Familia')
     sug_nome_artugo = fields.Char(string='Sug.Nome Artigo')
     unidade_mov = fields.Many2one('unimedida.unimedida', string='Unidade Movimento')
     iva = fields.Many2one('planiva.planiva', string='IVA')
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)


