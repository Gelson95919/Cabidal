# -*- coding: utf-8 -*-



from odoo import api, fields, models, _

class processo(models.Model):
     _name = 'processo.processo'
     _description = 'Processo Compras'
     name = fields.Char('Descrição', required=True)
     #date_release = fields.Date('Data de lançamento')
     fecho = fields.Boolean(string='Fechado')
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

