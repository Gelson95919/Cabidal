# -*- coding: utf-8 -*-

from odoo import models, fields, api

class imprimirDocumentoFatura(models.Model):
     _name = 'imprimir.documento.fatura'
     _description = "Imprimir Documento Fatura"
     ano_lectivo_id = fields.Many2one('matricula.matricula', string="Ano Lectivo") # Se epreciso utilizar este campo para celecionar
     prestacao = fields.Many2one('detalhes', string="Prestacao")           #o registro colocro relacao com com a tabela maricula
     curso_id = fields.Many2one('curso.curso', string="Curso")
     ano = fields.Selection([('primeiro_ano', 'Primeiro Ano'),
                             ('segundo_ano', 'Segundo Ano'),
                             ('terceiro_ano', 'Terceiro Ano'),
                             ('quarto_ano', 'Quarto Ano'),
                             ('quinto_ano', 'Quinto Ano')], default='primeiro_ano')
     documentos_pendentes = fields.Boolean(string="Docdumentos pendentes")
     matricula_ids = fields.One2many('matricula.matricula', 'documento_factura_id', string="Documento")
     data_emissao = fields.Date(string = "Data Emicao", default=fields.Date.today)
     alterar_data_emicao = fields.Boolean(string="Alterar Data Emissão")
     pre_visualizar = fields.Boolean(string="Pré-visualizar")
