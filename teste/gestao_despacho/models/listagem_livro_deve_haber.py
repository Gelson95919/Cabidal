# -*- coding: utf-8 -*-

from odoo import models, fields, api

class listagemLivrosDeveHaber(models.Model):
    _name = 'listagem.livros.deve.haber'
    _description = "Listagem de Livros Deve-haber"

    ordenar_por = fields.Selection([('numero_processo', 'Nº Processo'), ('data', 'Data'),
                                    ('importador', 'Importador')], default="numero_processo")
    data = fields.Boolean(string="Data")
    data_de = fields.Date(string="De")
    data_ate = fields.Date(string="Ate")
    processo = fields.Boolean(string="Processo")
    haber_id_de = fields.Many2one('nova.data', string="Haber")
    haber_id_ate = fields.Many2one('nova.data', string="Haber")
    valor = fields.Boolean(string="Valor")
    valor_de = fields.Float(string="Valor de")
    valor_ate = fields.Float(string="Valor ate")
    por_importador = fields.Boolean(string="por Importador")
    terceiro_id = fields.Many2one('terceiro.terceiro', string="Importador")
    todos_movimentos = fields.Boolean(string="Todos os Movimentos")

    def aceitar(self):
        return {
            'name': ('Nova Data'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'nova.data',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'target': 'new'
        }

class novaData(models.Model):
    _name = 'nova.data'
    #_rec_name = 'name'
    _description = 'Nova Data'

    codigo = fields.Integer(string="CODIGO")
    tipo = fields.Char(string="TIPO")
    numero = fields.Float(string="NUMERO")
    data_recib = fields.Date(string="DATARECIB")
    descricao = fields.Char(string="DESCRIÇÃO")
    valor_proc = fields.Float(string="VALORPROC")
    valor_hono = fields.Float(string="VALORHONO")
    honocta = fields.Float(string="HONOCTA")
    valor_reci = fields.Float(string="VALORRECI")
    saldo_proc = fields.Float(string="SALDOPROC")
    debe = fields.Float(string="DEBE")
    haber = fields.Float(string="HABER")
    data_ultim = fields.Float(string="DATAULTIM")
