# -*- coding: utf-8 -*-

from odoo import models, fields, api

class diarioauxiliar(models.Model):
    _name = 'diario.auxiliar'
    #_rec_name = 'name'
    _description = 'Diario Auxiliar'

    ano = fields.Date(string='')
    diario_inter_alter = fields.Selection([('intervalo', 'Intervalo'), ('alternado', 'Alternado'), ], string='Ano', default='intervalo')
    diario_de = fields.Many2one('diario.diario', string='De')
    diario_ate = fields.Many2one('diario.diario', string='Ate')
    alternado_an = fields.Many2many('diario.diario', string='Alternado')

    op_mes_doc = fields.Selection([('mes', 'Mes'), ('documento', 'Documento'), ], string='Opcao', default='mes')
    opc_intr__alt = fields.Selection([('intervalo', 'Intervalo'), ('alternado', 'Alternado'), ], string='Opcao', default='intervalo')
    opc_de = fields.Date(string='De')
    opc_ate = fields.Date(string='Ate')
    alternado_op = fields.Many2many('diario.diario', string="Alternado")

