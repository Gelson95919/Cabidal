# -*- coding: utf-8 -*-

from odoo import models, fields, api

class facturaDefinitiva(models.Model):
    _name = 'factura.definitiva'
    _description = "Factura Definitiva"
    num_factur = fields.Integer(string="Nº Factura")
    montante = fields.Float(string="Montante")
    nord = fields.Integer(string="N.O.R.D")
    data = fields.Date(string="Data", default=fields.Date.today)
    terceiro_id = fields.Many2one('terceiro.terceiro', string="Destinatario")
    regime = fields.Char(string="Regime")
    num_ordem = fields.Integer(string="Nº Ordem")
    data_ordem = fields.Date(string="Data")
    num_receita = fields.Integer(string="Nº Receita")
    data_receita = fields.Date(string="Data")
    mercadoria_ids = fields.One2many('mercadorias', 'factura_definitiva_id', string="Mercadoria")
    iva_cobrado_hanorario = fields.Float(string="IVA Cobrado Sobre honorário")
    total_geral_hanorario = fields.Float(string="Total geral honorário")
    hanorario_nota = fields.Float(string="Redução honorário (Nota)")
    date_release = fields.Date(string='Data Movimento', store=True, readonly=True)# related="tipo_docum_id.date_release",
    diario = fields.Many2one(string='Diario', readonly=True)#related="tipo_docum_id.diario", store=True,
    numero = fields.Integer(string='Numero')
    contabilizado = fields.Boolean(string='Contabilizado')

    recibo = fields.Char(string="Recibo(S)")
    factura_prov = fields.Many2one('XXXXXX') #Verificar Este campo

    outros_agenciamento_ids = fields.One2many('outras.agenciamento', 'factura_definitiva_id', string="Outras Agenciamento")

class mercadoria(models.Model):
    _name = 'mercadorias'
    #_rec_name = 'name'
    _description = 'Agêncimento Mercadoria'

    mercadoria = fields.Text(string="Mercadoria")
    valor = fields.Float(string="Valor")
    quantidade = fields.Float(string="Quantidade(d)")
    posicao_tabela = fields.Char(string="Posição Tabela")
    hanorarios = fields.Float(string="Honorários(e)")
    acrescimo = fields.Float(string="Acréscimos")
    factura_definitiva_id = fields.Many2one('factura.definitiva', string="Factura Definitiva")

class outrasAgenciamento(models.Model):
    _name = 'outras.agenciamento'
    #_rec_name = 'name'
    _description = 'Outras Agenciamento'
    descricao = fields.Selection([('1', '1 - Prienchemento de:TCE, C.E, Pertences, Cadastro, GTI e TN'),
                                  ('2', '2 - Requerimento de Pedidos de Regime Espicial'),
                                  ('3', '3 - Outros Requerimento'),
                                  ('4', '4 - Contestações'),
                                  ('5', '5 - Exames Prévios e Comerciais'),
                                  ('6', '6 - Expidiente para Matricula de Veículos Automóveis')], string="Descrição")
    posicao_tabela = fields.Float(string="Posição Tabela")
    hanorario = fields.Float(string="Honorários(e)")
    factura_definitiva_id = fields.Many2one('factura.definitiva', string="Factura Definitiva")

