# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class armanzem(models.Model):
     _name = 'armanzem.armanzem'
     _description = 'Armanzem '
     name = fields.Char(string='Descrição', required=True)
     date_release = fields.Date('Data lançamento', style="width:180px")
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

