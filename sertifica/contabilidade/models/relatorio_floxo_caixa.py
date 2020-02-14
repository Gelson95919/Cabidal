# -*- coding: utf-8 -*-

from odoo import models, fields, api

class relatoriofluxocaixa(models.Model):
    _name = 'relatorio.fluxo.caixa'
    #_rec_name = 'name'
    _description = 'Relatorio Fluxo Caixa"'

    ano = fields.Date(string='Ano')
    tipo = fields.Selection([('extracto', 'Extracto'), ('balancete', 'Balancete'), ], default='extracto')

    mes__tot_interval = fields.Selection([('todos', 'Todos'), ('intervalo', 'Intervalo'), ], default='todos')
    mes_de = fields.Date(string='De')
    mes_ate = fields.Date(string='Ate')

    muda_pagina = fields.Boolean(string ="Mudar Pagena")
    mueda_estrangeiro = fields.Boolean(string="Moeda Estrangeira")
    editar_relatorio = fields.Boolean(string="Editar Relatorio")

    cod_intr__alt = fields.Selection([('intervalo', 'Intervalo'), ('alternado', 'Alternado'), ], default='intervalo')
    cod_intr__alt_de = fields.Date(string='De')
    cod_intr__alt_ate = fields.Date(string='Ate')
    alternado = fields.Many2many('planteso.planteso', string="Alternado")

