# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class listadocunv(models.Model):
     _name = 'listadocunv.listadocunv'
     _description = 'Listagem Documento'
     #desclistdoc = fields.Char('Descrição')
     listagem = fields.Selection([('Listagem Total', 'Listagem Total'), ('listagem de Documento / Contas a Cobrar em Aberto', 'Listagem de Documento / Contas a Cobrar em Aberto'), ('Documentos com Diferencia na Regulacao', 'Documentos com Diferencia na Regulação')], 'Tipo Listagem', widget='radio', default="Listagem Total")
     por_cliente = fields.Boolean(string='Por Cliente')
     cliente = fields.Many2one('terceiro.terceiro', string='Cliente')
     uma_folha_por_benificiario = fields.Boolean(string='Uma Folha por Beneficiario')
     ditalhes_pagamento = fields.Boolean(string='Detalhe de Pagamento')
     em_aberto_ate_data_lancamento = fields.Boolean(string='Em aberto ate data selecionada')
     data_inicio = fields.Date(string='De')
     data_fim = fields.Date(string='Ate')
     tipo_documemt = fields.Boolean(string='Tipo Documento')
     movimento = fields.Selection([('ordenar por data', 'Ordenar por Data'), ('ordenar por numero doc', 'Ordenar por Numero Doc')], ' ', widget='radio', default="ordenar por data")
     confirencia_contabilidade = fields.Boolean(string='Confirencia Contabilidade')
     documento = fields.Many2many('documento.documento', string='  ')
     #outros = fields.One2many('listadocunv.listadocunv', 'id', string='detal', oldname='detal_line')
