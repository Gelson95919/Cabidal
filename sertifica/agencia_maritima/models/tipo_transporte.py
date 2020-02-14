# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tituloTransporte(models.Model):
    _name = 'transporte'
    _description = "Titulo Transporte"
    transitari_destino = fields.Char(strind="Transitario Destino")# Verificar esse campo no sistema
    tipo_tt_id = fields.Many2one('tipott', string="Tipo TT")
    referencia_tt = fields.Integer(string="Referência")
    fluxo_tt_id = fields.Many2one('fluxott', string="Fluxo TT")
    embalagem = fields.Char(string="Embalagem")# Verificar esse campo no sistema
    numero_s = fields.Integer(string="Numero")
    pesso = fields.Float(string="Pesso")
    volume = fields.Float(string="Volume")
    marca = fields.Text(string="Marca")
    descricao = fields.Text(string="Descricao")
    informacoes = fields.Text(string="Informacoes")
    interessados_ids = fields.One2many('interessados', 'titulo_transporte_id', string="Interessodo")
    contentor_ids = fields.Many2many('contentor', 'titulo_transporte_id', string="Contentor")
    valor_frete = fields.Float(string="Valor Frete")
    moeda_id= fields.Many2one('moeda.moeda', string="Moeda")

class interessados(models.Model):
    _name = 'interessados'
    _rec_name = 'nome'
    _description = 'interessados'
    tipo = fields.Selection([('exportado', 'Exportado'), ('distinata', 'Distinata'), ('notificar', 'Notificar')], default="exportado")
    nome = fields.Char(string="Nome")
    endereco = fields.Text(string="Endereco")
    titulo_transporte_id = fields.Many2one('transporte', string="Titulo Transporte")
    codigo = fields.Char(string="Codigo")
