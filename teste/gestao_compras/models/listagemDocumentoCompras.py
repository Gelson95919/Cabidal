# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class listadocun(models.Model):
     _name = 'listadocun.listadocun'
     _description = "Listagens Documentos"

     listagem = fields.Selection([('Listagem Total', 'Listagem Total'), ('listagem de compras / contas a pagar em aberto', 'Listagem de Compras / Contas a Pagar em aberto'), ('Documentos com Diferencia na Regulacao', 'Documentos com Diferencia na Regulação')], 'Tipo Listagem', default='Listagem Total', widget='radio')
     so_cm_imposto = fields.Boolean(string='So com Imposto')
     so_gastos_prop = fields.Boolean(string='So Gastos Prop (não CE)')
     por_beneficiario = fields.Boolean(string='Por Beneficiario')
     benificiario = fields.Many2one('terceiro.terceiro', string='Beneficiario')
     uma_folha_por_benificiario = fields.Boolean(string='Uma Folha por Beneficiario')
     ditalhes_pagamento = fields.Boolean(string='Detalhe de Pagamento')
     data = fields.Selection([('documento', 'Documento'), ('vencimento', 'Vencimento'), ('movimento', 'Movimento')], 'Data', default = 'documento', widget='radio')
     de = fields.Date(string='De')
     ate = fields.Date(string='Ate')
     confirencia_contabilidade = fields.Boolean(string='Confirencia Contabilidade')
