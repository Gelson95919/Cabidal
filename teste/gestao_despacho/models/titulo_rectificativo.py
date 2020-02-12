# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tituloRectificativo(models.Model):
     _name = 'titulo.rectificativo'
     _description = "TCE-Titulo Rectificativo"
     nome = fields.Char()
     endereco = fields.Char()
     ramo_de_actividade = fields.Text()
     alvara = fields.Char()
     nif = fields.Char()
     fax = fields.Integer()
     telefone = fields.Integer()
     e_mail = fields.Char()
     designacao_operacao = fields.Text()
     numero = fields.Integer()
     emitido_em = fields.Date()
     registro_previo = fields.Boolean()
     autorizacao_previa = fields.Boolean()
     prorrogacao = fields.Boolean()
     dias_30 = fields.Boolean()
     rectificacao= fields.Boolean()
     dias_40 = fields.Boolean()
     para_pagamento = fields.Boolean()
     dias_6o = fields.Boolean()
     para_despacho = fields.Boolean()
     dias_90 = fields.Boolean()
     substituicao = fields.Boolean()
     outra_especificar = fields.Text()
     onde_se_le = fields.Text()
     devese_ler = fields.Text()
     observacoes = fields.Text()
     dadta = fields.Date()
     num_copia = fields.Integer()

