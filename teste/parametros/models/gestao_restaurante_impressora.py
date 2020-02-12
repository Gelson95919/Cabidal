# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class impressora(models.Model):
    _name = 'impressoras.impressoras'
    _rec_name = 'name'
    _description = 'Impressoras'

    name = fields.Char(string="Descrição")
    impressor = fields.Selection([('microssoft', 'Microsoft XPS Document Writer'), ('hp', 'HP ePrint'),
                                   ('foxit', 'Foxit PhantontomPDF Print'), ('fax', 'Fax'),
                                   ('enviarParaOnenot', 'Enviar para o Onenote 2013'), ('secretaria', '\\\secretaria-pc\HP LaserJet P2050 Series PCL6')], string="Impressora")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)


