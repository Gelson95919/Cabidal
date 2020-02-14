# -*- coding: utf-8 -*-

from odoo import models, fields, api

class guiaTransf(models.Model):
     _name = 'guia.transfer'
     _description = 'Guia Transferencia'
     armazem_origem = fields.Many2one('armanzem.armanzem', string="Armazem Origem")
     armazem_destino = fields.Many2one('armanzem.armanzem', string="Armazem Origem")
     detalhe_documento = fields.One2many('detalhes.documento.armanzem', 'id', string="Detalhes")
     obs = fields.Text()

