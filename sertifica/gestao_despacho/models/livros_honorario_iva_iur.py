# -*- coding: utf-8 -*-

from odoo import models, fields, api

class livrosHonorarioIvaIur(models.Model):
    _name = 'livros.honorario.iva.iur'
    _description = "Livros Honorário/IVA/IUR"

    ordenar_por = fields.Selection([('numero_processo', 'Nº Processo'),('numero_recibo', 'Nº Recibo'), ('data', 'Data'),
                                    ('importador', 'Importador')], default="numero_processo")
    data = fields.Boolean(string="Data")
    data_de = fields.Date(string="De")
    data_ate = fields.Date(string="Ate")
    recibo = fields.Boolean(string="Recibo")
    fatura_defitiva_id_de = fields.Many2one('factura.definitiva', string="Recibo")
    fatura_defitiva_id_ate = fields.Many2one('factura.definitiva', string="Recibo")
    despacho = fields.Boolean(string="Despcho")
    despacho_id_de = fields.Many2one('depacho', string="Despacho de")
    despacho_id_ate = fields.Many2one('depacho', string="Despacho ate")
    valor = fields.Boolean(string="Valor")
    valor_de = fields.Float(string="Valor de")
    valor_ate = fields.Float(string="Valor ate")

    por_importador = fields.Boolean(string="por Importador")
    terceiro_id_de = fields.Many2one('terceiro.terceiro', string="De")
    terceiro_id_ate = fields.Many2one('terceiro.terceiro', string="Ate")
    todos_movimentos = fields.Boolean(string="Todos os Movimentos")
    so_recibo_com_pagamento = fields.Boolean(string="So recibo Com Pagamento")
    data_de_so = fields.Date(string="Data")
    data_ate_so = fields.Date(string="Data")


