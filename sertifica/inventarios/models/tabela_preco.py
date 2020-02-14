# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tabelaPreco(models.Model):
     _name = 'tabela.preco'
     _description = 'Tabela Preco'
     armazem = fields.Many2one('armanzem.armanzem', string="Armazem")
     familia = fields.Many2one('familia.familia', string="Familia")
     sub_familia = fields.Many2one('subfamilha.subfamilha', string="Sub Familia")
     todos_precos = fields.Boolean(string="Tudos os Preço")
     incluir_estoque = fields.Boolean(string="Incluir Estoque")
     tiporelat = fields.Selection([('relatorioImprecoporOrdemFamilia', 'Relatorio Impresso por ordem de Familia'), ('relatorioImprecoporNomeProduto', 'Relatorio Impresso por nome produto')], default = 'relatorioImprecoporOrdemFamilia')