# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class moninterno(models.Model):
     _name = 'moninterno.moninterno'
     _description = 'Movimento Interno'
     name = fields.Text('Descrição')
     date_release = fields.Date('Data', default=fields.Date.today)

     movimento = fields.Many2one('movinterno.movinterno', string='Movimento')
     tipo_movimento = fields.Selection([('1', 'Tranfirencia'), ('2', 'Entrada'), ('3', 'Saida')],
                                       'Tipo Movimento', Widget="radio", default='1', related="movimento.tipo_movimento", store=True)

     centro_custo = fields.Many2one('planconta.planconta', string='Centro Custo')
     montante = fields.Float(string='Montante')
     conta_origem = fields.Many2one('monetario.monetario', string='Conta Origem')
     cheque = fields.Char(string='Cheque')
     contabilizado = fields.Boolean(string='Contabilizado')
     diario = fields.Integer(string='Diario')
     saldo = fields.Float(string='Saldo', related='conta_origem.saldo_inicial')
     esc = fields.Float(string='Esc')
     numero = fields.Integer(string='Numero')
     conta_destino = fields.Many2one('monetario.monetario', string='Conta Destino')
     diariod = fields.Integer(string='Diario')
     contabilizadod = fields.Boolean(string='Contabilizado')
     escd = fields.Float(string='Esc')
     numerod = fields.Integer(string='Numero')
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

     dados_antigo = fields.Boolean(string="Dados Antigo")  # se True porque os dados são antigo


