# -*- coding: utf-8 -*-

from odoo import models, fields, api

class facturaPrevisoria(models.Model):
    _name = 'factura.previsoria'
    _description = "Factura Previsória"
    data = fields.Date(string="Data", default=fields.Date.today, readonly="True")
    nume_recib = fields.Integer(string="Numero Recibo")
    xml_asycuda = fields.Boolean(string="XML ASYCUDA", default="True")
    nord = fields.Integer(string="N.O.R.D")
    terceiro_id = fields.Many2one('terceiro.terceiro', string="Destinatario")
    descricao_mercadoria = fields.Text(string="Descrição Mercadoria")
    guia_emolumento_ids = fields.One2many('guia.emolumento', 'factura_previsoria_id', string="factura Previsoria")
    impresso_principal = fields.Integer(string="Impresso Principal")
    p_l = fields.Integer(string="P.L")
    g_t_i = fields.Integer(string="G.T.I")
    form = fields.Integer(string="Form")
    impresso_intercalar = fields.Integer(string="Impresso Intercalar")
    d_v = fields.Integer(string="D.V")
    fotocopias = fields.Integer(string="Fotocopia")
    t_c_e = fields.Integer(string="T.C.E")
    t_n = fields.Integer(string="T.N")
    quantidade_estampilhas = fields.Integer(string="Quantidade Estampilhas")
    regime_ids = fields.One2many('regime', 'factura_previsoria_id', string="Regimes")
    requerimento_normal = fields.Float(string="requerimento normal")
    exame_previo = fields.Float(string="exame previo")
    requerimento_especial = fields.Float(string="requerimento especial")
    expediente_matricula = fields.Float(string="expediente matricula")
    desconto = fields.Float(string="Desconto")
    desconto_2 = fields.Float()
    total = fields.Float(string="Total")
    rubricas_ids = fields.One2many('detalhe.items', 'factura_previsoria_id')

    extracto_num = fields.Many2one('XXXXXXX') #Verificar esse campo
    montante = fields.Float(string="Montante")

class guiaEmolumento(models.Model):
    _name = 'guia.emolumento'
    #_rec_name = 'name'
    _description = 'Guia Emolumento'

    tarifa_alfandiga_id = fields.Many2one('tarifa.alfandega', string="Tipo")
    horas_remuneracoes_id = fields.Many2one('horas.remuneracoes', string="Embalagem")
    quantidade = fields.Float(string="Quantidade")
    factura_previsoria_id = fields.Many2one('factura.previsoria', string="Factura Previsória")

class regime(models.Model):
    _name = 'regime'
    #_rec_name = 'name'
    _description = 'Regime'
    regime_id = fields.Many2one('regime.alfandega', string="Agenciamento")
    valor_base = fields.Float(string="Valor Base")
    agencia_desp_id = fields.Many2one('agencia.despacho', string="Tabela Anexa")
    dep = fields.Boolean(string="Dep.50%")
    factura_previsoria_id = fields.Many2one('factura.previsoria', string="Factura Previsória")

class detalhesItems(models.Model):
    _name = 'detalhe.items'
    #_rec_name = 'name'
    _description = 'Detalhes Items'
    cod = fields.Char(string="Cod")
    rubricas_id = fields.Many2one('rubricas', string="Items")
    montante = fields.Float(string="Montante")
    factura_previsoria_id = fields.Many2one('factura.previsoria', string="Factura Previsória")