
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class pagamentos(models.Model):
    _name = 'processamento.pagamento.remuneracoes'
    _description = 'Processamento Pagamento Remunerações'
    ano = fields.Date(string="Ano")
    data = fields.Date(string="Data")
    pagamento_lista = fields.One2many('remuneracoes.salario', 'pagamentos_id')
    Examples_count = fields.Char()

