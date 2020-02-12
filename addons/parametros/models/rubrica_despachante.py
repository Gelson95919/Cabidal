# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
import math
from odoo import api, fields, models, tools, _

_logger = logging.getLogger(__name__)

class rubricaDespachante(models.Model):

     _name = 'rubrica.despachante'
     _description = 'Rubrica Despachante'
     codigo = fields.Integer(string="Codigo")
     descricao = fields.Char(string="Descrição")
     plano_conta_id = fields.Many2one('planconta.planconta', string="Conta Artigo")
     organizacao_id = fields.Many2one('organizacao.organizacao', string="Centro Custo")
     plan_cont_id = fields.Many2one('planconta.planconta', string="Conta IVA")
     plano_teso_id = fields.Many2one('planteso.planteso', string="Fluxo Caixa")
     plan_iva_id = fields.Many2one('planiva.planiva', string="Código IVA")
     juntar_em_guia_cobranca = fields.Boolean(string="Juntar em Guia Cobrança")
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)



