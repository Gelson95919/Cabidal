# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tituloComercioExterno(models.Model):
     _name = 'titulo.comercio.externo'
     _description = "Titulo do Comercio Externo"
     nome = fields.Char()
     endereco = fields.Char()
     ramo_de_actividade = fields.Text()
     alvara = fields.Char()
     nif = fields.Char()
     fax = fields.Integer()
     telefone = fields.Integer()
     e_mail = fields.Char()
     designacao_operacao = fields.Text()
     registro_previo = fields.Boolean()
     autorizacao_previa = fields.Boolean()
     nome_exp = fields.Char()
     endereco_exp = fields.Char()
     pais_origem = fields.Char()
     pais_destino = fields.Char()
     banco_agencia = fields.Char()
     tipo_contrato = fields.Char()
     moeda_contrato = fields.Char()
     modelidade_pagamento = fields.Char()
     despachante = fields.Char()
     estancia_aduaneir = fields.Char()
     com_dependencia_cambio = fields.Boolean()
     sem_dependencia_cambio = fields.Boolean()
     so_para_despacho = fields.Boolean()
     so_para_pagamento = fields.Boolean()
     so_para_despacho_pagamento = fields.Boolean()
     dadta = fields.Date()
     num_copia = fields.Integer()

