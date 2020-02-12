# -*- coding: utf-8 -*-

from odoo import models, fields, api

class rubrica(models.Model):
     _name = 'rubrica'
     _description = "Rubricas"
     codigo = fields.Integer(string="Codigo")
     descricao = fields.Char(string="Descrição")
     rubrica_terceiro = fields.Boolean(struing="Rubrica Terceiro")
     terceiro_id = fields.Many2one('terceiro.terceiro')
     rubrica_iva = fields.Boolean(string="Rubrica Iva")
     documento = fields.Many2one('documento.documento', string="Documento")
     juntar_em_guia_cobranca = fields.Boolean(string="Juntar em Guia Cobrança")
     codigo_guia_cobranca = fields.Integer(string="Codigo guia cobrança")
     rubrica_despachante_id = fields.Many2one('rubrica.despachante', string="Rubrica Documento Despachante")
     compras_compras_id = fields.Many2one('compras.compras', string="Rubrica Documento Terceiro")
     observacoes = fields.Text(string="Descrição")
     plano_conta_id =fields.Many2one('planconta.planconta', string="Conta Artigo")
     organizacao_id = fields.Many2one('organizacao.organizacao', string="Centro Custo")
     plan_cont_id = fields.Many2one('planconta.planconta', string="Conta IVA")
     plano_teso_id = fields.Many2one('planteso.planteso', string="Fluxo Caixa")
     plan_iva_id = fields.Many2one('planiva.planiva', string="Código IVA")
