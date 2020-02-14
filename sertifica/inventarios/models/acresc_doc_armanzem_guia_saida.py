# -*- coding: utf-8 -*-

from odoo import models, fields, api

class guiaSaida(models.Model):
     _name = 'guia.saida'
     _description = 'Guia Saida'
     numero = fields.Integer(string="Numero")
     armanzem = fields.Many2one('armanzem.armanzem', string="Armazem")
     terceiro = fields.Many2one('terceiro.terceiro', string="Terceiro")
     data = fields.Date('Data')
     motivo = fields.Many2one('movimentostok.movimentostok', string="Motivo")
     doc_ref_n = fields.Char(string="Doc.Ref.Nº")
     data_thek = fields.Date('Data', default=fields.Date.today)
     valor_tot_doc=fields.Float(string="Valor Total de Documento")
     detalhe_documento_armanzem = fields.One2many('detalhes.documento.armanzem', 'id', string="Detalhes")
     obs = fields.Text()

