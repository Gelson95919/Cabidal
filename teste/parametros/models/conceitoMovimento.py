# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class movinterno(models.Model):
     _name = 'movinterno.movinterno'
     _description = 'Conceito Movimento Interno'
     name = fields.Char('Descrição',)# required=True
     nmuero = fields.Char(string="Codigo", readoly=True)
     tipo_movimento = fields.Selection([('1', 'Transferência'), ('2', 'Entrada'), ('3', 'Saida')], 'Tipo Movimento', Widget="radio")#, default='1'
     movimento_reflexivo = fields.Boolean(string='Movimento Reflexivo')
     origem_nao_grava_contabilidade = fields.Boolean('Origem Não Grava Contabilidade')
     destino_nao_grava_contabilidade = fields.Boolean(string='Destino Não Grava Contabilidade')
     fluxo_de_caixa = fields.Many2one('planteso.planteso', string='Fluxo de Caixa')
     conta = fields.Many2one('planconta.planconta', string='Conta')
     centro_custo = fields.Many2one('planconta.planconta', string='Centro Custo')
     codigo_iva = fields.Many2one('planiva.planiva', string='Código Iva')
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)
     ccodigo = fields.Char()
     ccodcon = fields.Char()

     @api.model
     def create(self, vals):
          vals['nmuero'] = self.env['ir.sequence'].next_by_code('fatuclient.fatuclient.num') or _('New')
          res = super(movinterno, self).create(vals)
          return res

