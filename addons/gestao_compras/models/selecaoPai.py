# -*- coding: utf-8 -*-


#from odoo import models, fields, api, tools



from datetime import timedelta
from odoo import models, fields, api, exceptions

class selecaoPai(models.Model):
    _name = 'selecao.pai'
    name = fields.Char(string = 'Nome Pai')
    apelido = fields.Char(string = "Apelido")
    morada = fields.Char(string='Morada')
    telefone = fields.Integer(string="Telefone")

    def _prepare_invoice_line(self):

        data = {
            'id': self.nome_pae,
            'name': self.nome_pae,
            'apelido': self.apelido,
            'morada': self.morada,
            'telefone': self.telefone,

        }
        return data