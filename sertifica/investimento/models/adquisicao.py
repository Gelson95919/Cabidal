# -*- coding: utf-8 -*-

from odoo import models, fields, api

class adquisicao(models.Model):
     _name = 'adquisicao'
     _description = "Adquisições"

     name= fields.Char(string="Designação")
     codigo = fields.Integer(string="Código")
     codigo_patrimonial = fields.Integer(string="Código Patrimonial")
     data_adquisicao = fields.Date(string="Data Adquisição")
     data_inic_utiliaac = fields.Date(string="Data Inicio Util")
     porteria_id = fields.Many2one('', string="Portaria")
     taxa = fields.Float(string="Taxa")
     cod_sequencial = fields.Integer(string="Código Sequencial")
     vida_utel = fields.Float(string="Vida Utel")
     met_calculo_quotas = fields.Selection([('constante', 'Constante'), ('decreciva', 'Descritiva'), ('proporcionais', 'Proporcionais á Utilização')], default="constante")
     tipo = fields.Many2one('tipo.imobilizado', string="Tipo")
     conta_id = fields.Many2one('planconta.planconta', string="Conta")
     exercicio_id = fields.Many2one('planconta.planconta', string="Exercicio")
     acumulada_id = fields.Many2one('planconta.planconta', string="Acumulada")
     depart_id = fields.Many2one('departamento.area', string="Local")
     planconta_id= fields.Many2one('planconta.planconta', string="Centro")
     terceiro_id = fields.Many2one('terceiro.terceiro', string="Fornecidor")
     num_elimentos = fields.Integer(string="Nro.limento")
     unimed_id = fields.Many2one('unimedida.unimedida', string="Unidade Medida")
     obs = fields.Text(string="OBS")
     valor_aquisicao = fields.Float(string="Valor Aquisição")
     valor_residual = fields.Float(string="Valor Residual")
     iva_dedutivel = fields.Float(string="Iva Dedutivel")
     valor_amortizavel = fields.Float(string="Valor Amortizavel")
     valor_actual = fields.Float(string="Valor Actual")
     quotas_ids = fields.One2many('quotas.amort', 'adquisicao_id', string="Quotas Amortização")
     adquiz_seguro_ids = fields.One2many('adquiz.seguro', 'adquisicao_id')

class quotasAmort(models.Model):
    _name = 'quotas.amort'
    #_rec_name = 'name'
    _description = 'Quotas Amortização'

    ano = fields.Date(string="Ano")
    taxa = fields.Float(string="Taxa")
    valor = fields.Float(string="Valor")
    amor_acu = fields.Float(string="Amort.Acum")
    valor_liquid = fields.Float(string="Valor Liquido")
    amort = fields.Float(string="Amort")
    adquisicao_id = fields.Many2one('adquisicao', string="Adquisições")

class adqSeguros(models.Model):
    _name = 'adquiz.seguro'
    #_rec_name = 'name'
    _description = 'Adquisições seguro'

    sequence = fields.Integer(default=10, help="Dá a seqüência desta linha .")
    siguro_id = fields.Many2one('seguros.seguros', string="SEGURO")
    apolice = fields.Char(string="APOLICE")
    data = fields.Date(string="DATA")
    franquia = fields.Float(string="FRANKIAS")
    adquisicao_id = fields.Many2one('adquisicao', string="Adquisições")

