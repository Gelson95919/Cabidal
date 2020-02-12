# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class orcamenteso(models.Model):
     _name = 'orcamenteso.orcamenteso'
     _description = 'Orcamento da Tesouraria'
     Periodo = fields.Char(string='Período', readonly=True)
     descricao = fields.Char(string='Descrição')
     filtrar = fields.Selection([('semfiltro', 'Sem Tiltros'), ('Códigos de Movimento', 'Códigos de Movimento'),
                                 ('Montante > 0', 'Montante > 0'), ('Montantes <= 0', 'Montantes <= 0')], 'Filtrar',
                                Widget="radio")
     orcament = fields.Many2many('alteracao.orcamento.tesouraria', 'orcamenteso_id', oldname='detal_line')
     alteracoes_ret = fields.Many2many('alteracao.orcamento.tesouraria', 'orcamenteso_id', oldname='detal_line')
     compromiso = fields.Many2many('alteracao.orcamento.tesouraria', 'orcamenteso_id', oldname='detal_line')
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)





