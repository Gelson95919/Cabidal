# -*- coding: utf-8 -*-

from odoo import models, fields, api

class manifestoCarga(models.Model):
    _name = 'manifesto.carga'
    _description = "Manifesto de Carga"
    estancia_aduaneira = fields.Char(string="Estancia Aduaneira")# Verificar esse campo no sistema
    numero_interno = fields.Integer(string="Numero Interno")
    modo_transporte = fields.Char(string="Modo Transporte")# Verificar esse campo no sistema
    ano_num_viagem = fields.Char(string="Manifesto")
    data_chegada= fields.Datetime(string="Data Chegada")
    local_embarque = fields.Many2one('portos.escalas', string="Local embarque")
    local_destino = fields.Many2one('portos.escalas', string="Local Destino")
    nome_transport_id = fields.Many2one('navios.navios', string="Nome transporte")
    nacionalidade_transporte = fields.Many2one(string="Nacionalidade Transporte", readonly=True, related="nome_transport_id.nacionalidade", store=True)
    imo_transporte = fields.Integer(string="IMO Transporte")
    nome = fields.Char(strinfg="Nome")
    codigo = fields.Integer(string="Codigo")
    endereco = fields.Text(string="Enderco")
    armazem = fields.Many2one('armanzem.armanzem', string="Armanzem")
    contentor_ids = fields.One2many('contentor', 'manifesto_carga_id', string="Contentor")
    total_docums = fields.Float(string="Total Documento")
    total_pak = fields.Float(string="Total Pagamento")
    total_pesso = fields.Float(string="Total Pesso")
    n_contentores = fields.Integer(string="Numeros Contentores")
