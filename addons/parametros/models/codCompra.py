# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class codgoCompras(models.Model):
     _name = 'compras.compras'
     _description = 'Conceito de Compras '
     _rec_name = 'codigo'

     name = fields.Char('Descrição',)
     date_release = fields.Date('Data de lançamento')
     utiliza_configuracao_de_processo = fields.Boolean(string='Utiliza Configuração de Processo')
     mudar_tipo_de_movimento_se_for_negativo = fields.Boolean(string='Mudar Tipo de Movimento se For Negativo')
     conta_id = fields.Many2one('planconta.planconta', string='Conta', domain=[('grupo', '=', False)])
     conta_IVA_id = fields.Many2one('planconta.planconta', string='Conta IVA')
     fluxo_de_caixa_id = fields.Many2one('planteso.planteso', string='Fluxo de Caixa')
     codigo_IVA_di = fields.Many2one('planiva.planiva', string='Código IVA')
     adiantamento_de_compra_gasto = fields.Boolean(string='Adiantamento de Compra/Gasto')
     incluir_na_cta_cte = fields.Boolean(string='Incluir na Cta.Cte')
     pagamento_por_conta_de_outrem = fields.Boolean(string='Pagamento Por Conta de Outrem')
     tem_retencao_de_IUR = fields.Boolean(string='Tem Retenção de IUR')
     iur = fields.Float(string='Imposto')
     codigo_conta_id = fields.Many2one('planconta.planconta', string='Código Conta')
     utilizar_conta_reflexao = fields.Boolean(string='Utilizar Conta Reflexão')
     contac_id = fields.Many2one('planconta.planconta', string='Conta')
     centro_custo_id = fields.Many2one('organizacao.organizacao', string='Centro Custo')
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

     tipologia_dpr_fornecedores = fields.Selection(
          [('B.1', 'B.1'), ('B.2', 'B.2'), ('B.3', 'B.3'), ('B.4', 'B.4'),
           ('B.5', 'B.5'), ('B.6', 'B.6'), ('C.1', 'C.1'), ('C.2', 'C.2'),
           ('C.3', 'C.3'), ('C.4', 'C.4'), ('C.5', 'C.5'), ('D.1', 'D.1'),
           ('D.2', 'D.2'), ('D.3', 'D.3'), ('E.1', 'E.1'), ('E.2', 'E.2'),
           ('E.3', 'E.3'), ('T.1', 'T.1')], 'Tipo DPR Fornecedores')

     tipo = fields.Selection(
          [('1', 'Imobilizado'),
           ('2', 'Existencia'), ('3', 'Serviços'),
           ('4', 'Outros Bens de Consumo'),
           ('5 ', 'Adquisição de Serviço a não reside')], 'Tipo')

     # campo de controlo
     type = fields.Selection(
         [('cod_compras', 'Conceito de Compras'),
          ('conceitos_pagamento', 'Conceito Pagamento')],
         readonly=True, index=True, change_default=True,
         default=lambda self: self._context.get('type', 'cod_compras'),
         track_visibility='always')

     codigo = fields.Char(string="Código",  copy=False, readonly=False, index=True,
                          default=lambda self: self._get_next_cod(), store=True, )
     CCODCON = fields.Char()
     ccodcon = fields.Char()
     #dados plano conta
     leva_terce = fields.Boolean(string='Leva Terceiro', related='conta_id.leva_terce', store=True)
     control_IVA = fields.Boolean(string='Control IVA', related='conta_id.control_IVA')


     @api.model
     def _get_next_cod(self):
         sequence = self.env['ir.sequence'].search([('code', '=', 'compras.compras')])
         next = sequence.get_next_char(sequence.number_next_actual)
         return next

     @api.model
     def create(self, vals):
         vals['codigo'] = self.env['ir.sequence'].next_by_code('compras.compras') or _('New')
         obg = super(codgoCompras, self).create(vals)
         return obg

     #Substetui cod compra
     def compor_op(self):
          pass
          #plano = self.env['compras.compras'].search([('id', '>=', 1)])
          #for c in plano:
          #    c.ccodcon = c.CCODCON