# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class monetario(models.Model):
     _name = 'monetario.monetario'
     _description = 'Meio Monetario'
     codigo = fields.Char(string="Documento", store=True, copy=True, index=True, default=lambda self: self._get_next_cod())#,
     name = fields.Char('Descrição')#
     data = fields.Date(string="Dta")
     saldo_inicial = fields.Float(string='Saldo Inicial')#, required=True
     banco = fields.Many2one('entbanc.entbanc', string='Banco')
     terceiro_id = fields.Many2one('terceiro.terceiro', string='Encaregado')
     encaregado = fields.Char(string="Encarregado", related='terceiro_id.name')
     conc_rel_tesoura = fields.Boolean(string="Considerar no relatoriode posição tesouraria")
     estado = fields.Char(string='Estado')
     numero_fecho = fields.Integer(string='Numero de Fecho')
     valor_caucao = fields.Float(string='Valor Caução')
     moeda = fields.Many2one('moeda.moeda', string='Moeda')
     diario = fields.Many2one('diario.diario', string='Diario')
     name_diario = fields.Char(string="Nome Diario", related="diario.name")
     conta = fields.Many2one('planconta.planconta', string='Conta', domain=[('grupo', '=', False)])
     centro_custo = fields.Many2one('planteso.planteso', string='Centro Custo')
     tipo_meio = fields.Selection([('1', 'Caixa'), ('2', 'Deposito a Ordem'), ('3', 'Fundo de Maneio')], 'Tipo Meio', default="1")
     numero_movimento = fields.Integer(string="Numero Movimento")

     #dados de plano de conta
     grupo = fields.Boolean(string='Grupo', related='conta.grupo')
     leva_terce = fields.Boolean(string='Leva Terceiro', related='conta.leva_terce')
     leva_centro_custo = fields.Boolean(string='Leva Centro Custo', related='conta.leva_centro_custo')
     leva_moeda_estrangeira = fields.Boolean(string='Leva Moeda Estrangeira', related='conta.leva_moeda_estrangeira')
     fluxo_caixa = fields.Boolean(string='Fluxo Caixa', related='conta.fluxo_caixa')
     control_IVA = fields.Boolean(string='Control IVA', related='conta.control_IVA')
     natureza_conta = fields.Selection([('3', 'Neutro'), ('D', 'Devedor'), ('C', 'Criador')], 'Natureza de Conta',
                                        related='conta.natureza_conta')#required=True,
     natureza_saldo = fields.Selection([('3', 'Neutro'), ('C', 'Creador'), ('D', 'Devedor')], 'Natureza de Saldo',
                                        related='conta.natureza_saldo')#required=True,

     # dados de Diario
     numero_documento_inicial = fields.Char(string='Numero Documento Inicial', related='diario.numero_documento_inicial')
     codigo_diario = fields.Char(string="Codigo Diario", store=True, related='diario.codigo')
     #name_diario = fields.Char('Descrição', related="diario.name", store=True)
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

     @api.model
     def _get_next_cod(self):
          sequence = self.env['ir.sequence'].search([('code', '=', 'meios.codigo')])
          next = sequence.get_next_char(sequence.number_next_actual)
          return next

     @api.model
     def create(self, vals):
          vals['codigo'] = self.env['ir.sequence'].next_by_code('meios.codigo') or _('New')
          res = super(monetario, self).create(vals)
          res.create_folha()
          return res
     
     @api.multi
     def create_folha(self):
          folh_obj = self.env['folha.tesouraria']
          folha = folh_obj.create({
               'folha': self.id,
               'name': self.name,
               'codigo': self.codigo,
               'saldo_ant': self.saldo_inicial,
               'diario': self.diario.id,
          })
          return folha


