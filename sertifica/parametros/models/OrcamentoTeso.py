# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class orcamentoTesouraria(models.Model):
     _name = 'orcamento.tesouraria'
     _description = 'Orçamento de Tesouraria '
     ano = fields.Date('Ano')
     pagamento_id = fields.Many2one('tesopagame.tesopagame', string='Codigo', required=True)#para remover
     valor_anual = fields.Float(string='Valor Anual')
     mes_inic = fields.Integer(string='Mes Inicial')
     janeiro = fields.Float(string='Janeiro')
     fevereiro = fields.Float(string='Fevereiro')
     marco = fields.Float(string='Março')
     abril = fields.Float(string='Abril')
     maio = fields.Float(string='Maio')
     junho = fields.Float(string='Junho')
     julho = fields.Float(string='Julho')
     agosto = fields.Float(string='Agosto')
     setembro = fields.Float(string='Setembro')
     outubro = fields.Float(string='Outubro')
     novembro = fields.Float(string='Novembro')
     dezembro = fields.Float(string='Dezembro')
     motivo = fields.Text(string='Motivo')
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)
