# -*- coding: utf-8 -*-

from odoo import models, fields, api

class usuario(models.Model):
    _name = 'usuario.usuario'
    _rec_name = 'name'
    _description = 'New Description'

    name = fields.Char()
    last_login = fields.Datetime(string="", required=False, )
