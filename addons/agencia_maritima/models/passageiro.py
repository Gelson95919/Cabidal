# -*- coding: utf-8 -*-

from odoo import models, fields, api

class passagem(models.Model):
    _name = 'passagem'
    _description = "Passagens Inter Ilhas"
    navio_id = fields.Many2one('navios.navios', string="Navio")
    numer_navio = fields.Integer(string="Numero Navio")
    num_viagem = fields.Integer(string="Numero Viagem")
    ano = fields.Date(string="Ano")
    porto_id_o = fields.Many2one('portos.escalas', string="Origem")
    porto_id_d = fields.Many2one('portos.escalas', string="Destino")
    num_bilhete = fields.Integer(string="Numero Bilhete")
    classe_id = fields.Many2one('classe.navio', string="Classe")
    nome = fields.Char(string="Nome")
    edade = fields.Integer(string="Edade")
    domento = fields.Char(string="Documento")
    contocto = fields.Integer(string="Contacto")
    data_emicao = fields.Date(string="Data Emicao", default=fields.Date.today)
    nqacionalidade = fields.Many2one('nacionalidade.nacionalidade', string="Nacionalidade")
    tarifa = fields.Float(string="Tarifa")
    agencia = fields.Float(string="Agencia")
    taxa_enapor = fields.Float(sring="Taxa Enapor")
    selos = fields.Float(string="Selos")
    impressos = fields.Float(string="Impresso")
    total = fields.Float(string="Total")
    pagamento = fields.Selection([('pendentes', 'Pendentes'), ('cash', 'Cash'), ('credito', 'Credito')], default="cash")
