# -*- coding: utf-8 -*-


#from odoo import models, fields, api, tools



from datetime import timedelta
from odoo import models, fields, api, exceptions

class selecaofil(models.Model):
    _name = 'selecao.fil'
    teste1 = fields.Char(string='Nome Filho')
    teste2 = fields.Char(string='Apelido')
    pai_id = fields.Many2one('selecao.pai', string='Pai')
    pais = fields.One2many('selecao.pai', 'id', string='Pais', oldname='pais')
    currency_id = fields.Many2one('res.currency')
    fil_id = fields.Many2one('selecao.fil')

    @api.onchange('pai_id')
    def _onchange_pai_id(self):
        if not self.pai_id:
            return {}
        self.currency_id = self.fil_id.currency_id
        new_lines = self.env['selecao.pai']
        for line in self.fil_id.pais:
            new_lines += new_lines.new(line._prepare_invoice_line())
        self.pais += new_lines
        #self.pai_id = False
        return {}

        res = []
        for line in self.pais:
            pais = {
                'id': line.id,
                'name': line.nome_pae,
                'apelido': line.apelido,
                'morada': line.morada,
                'telefone': line.telefone,
            }
            res.append(pais)
            return res