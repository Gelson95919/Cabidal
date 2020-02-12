# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class filiais(models.Model):
     _name = 'filiais.filiais'
     _description = 'Filiais'
     name = fields.Char(string='Descrição', required=True)
     cod = fields.Many2one('fiscal', string='Codigo')
     name1 = fields.Text(string='Descrição', )
     terceiro_id = fields.Many2one('terceiro.terceiro')
     #date_release = fields.Date('Data lançamento', style="width:180px")
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)



