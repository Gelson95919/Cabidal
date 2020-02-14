# -*- coding: utf-8 -*-

from odoo import models, fields, api

class declaiperiod(models.Model):
    _name = 'declarar.perio.rend'
    #_rec_name = 'name'
    _description = 'Declaração periódica dos rendimentos'
    ano = fields.Date(string='Ano')
    mes = fields.Selection([('janeior','Janeiro'),('fevereiro','Fevereiro'),('marco','Março'),('abril','Abril'),('Maio','Maio'),('junho','Junho'),('julho','Julho'),('agosto','Agosto'),('setembro','Setembro'),('outubro','Outubro'),('novembro','Novembro'),('dezembro','Dezembor'),], string='Mes')
    processar = fields.Boolean(string='Processar')
    formulario = fields.Selection([('modelo106','Modelo 106'),('anexocliente','Anexo Cliente'),('anexofornecidor','Anexo Fornecedores')], string='Formulario', default='modelo106', widget = 'radio')
    accao = fields.Selection([('imprimir','Imprimir'),('exportarpdf','Exportar PDF'),('exportarxml','Exportar XML')], string='Acção', default='imprimir', widget = 'radio')

    #dados_fatura_salario = fields.One2many('despesa.despesa', 'id', string="Anexo Fornecedores", required=False)
    dados_fatura_client = fields.One2many('fatuclient.fatuclient', 'fatuclient_id', string="Anexo Clientes", required=False,)
    dados_fatura_fornecedores = fields.One2many('despesa.despesa', 'id', string="Anexo Fornecedores", required=False)

    tipo_decl_anex = fields.Selection([('noprazo','No prazo'),('foradoprazo','Fora do prazo'),('subustituicao','Substetuição')], string="Tipo", default='noprazo')
    salario = fields.Boolean(string='Salario')
    cliente = fields.Boolean(string='Cliente')
    fornecidor = fields.Boolean(string='Fornecidor')
    obs = fields.Text(string='obs')
    data = fields.Date(string='Data')
    total_pagar = fields.Float(string='Tota a pagar')
    conceito_despesas_fornec = fields.Many2many('artigo.artigo',string="Conceitos de Despesas")
    g1 = fields.Integer()
    g2 = fields.Integer()
    g3 = fields.Integer()
    g4 = fields.Integer()
    g5 = fields.Integer()
    g6 = fields.Integer()
    g7 = fields.Integer()


