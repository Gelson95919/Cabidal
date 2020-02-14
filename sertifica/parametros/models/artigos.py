# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, exceptions, _

class artigo(models.Model):
     _name = 'artigo.artigo'
     _description = 'Artigo '
     #date_release = fields.Date('Data de lançamento')
     name = fields.Char('Descrição')# required=True
     codigo = fields.Char(string="Codigo", copy=False, readonly=False, index=True,
                          default=lambda self: _('New'))# required=True,
     familia_id = fields.Many2one('familia.familia', string='Familia')
     sub_familia_id = fields.Many2one('subfamilha.subfamilha', string='Sub Familia')
     codigo_de_bara = fields.Char(string='Código de Bara')
     descricao_sintetica = fields.Char(string='Descrição Sintetica')
     unidade_movimento_id = fields.Many2one('unimedida.unimedida', string='Unidade Movimento')
     iva_id = fields.Many2one('iva.iva', string='IVA')#para remover
     ivasel = fields.Selection([('0.00', '0.00'), ('15.00', '15.00'), ('15.50', '15.50'),], string='IVA')
     image = fields.Binary('Logo')
     controlo_stock = fields.Boolean(string='Controlo Stock')
     armazem = fields.Char(string='Armazem')
     existencia = fields.Integer(string='Existência')
     preco_custo = fields.Float(string='Preço Custo')

     adiantamento_de_clientes = fields.Boolean(string='Adiantamento de Clientes')
     recebimento_por_contra_de_outrem = fields.Boolean(string='Recebimento Por Contra de Outrem')
     conta_artigo_id = fields.Many2one('planconta.planconta', string='Conta Artigo')
     centro_custo_id = fields.Many2one('planconta.planconta', string='Centro Custo')
     conta_iva_id = fields.Many2one('planconta.planconta', string='Conta Iva')
     fluxo_de_caixa_id = fields.Many2one('planteso.planteso', string='Fluxo de Caixa')
     codigo_iva_id = fields.Many2one('planiva.planiva', string='Codigo Iva')
     descricao = fields.Html(
          'OBS',
          sanitize=True,
          strip_style=False,)

     preco = fields.One2many('artigo.artigo', 'id', string='preço', oldname='preco_line')
     n_preco = fields.Many2one('preco.preco', string='Numero Preço')
     valor = fields.Float(string='Valor', store=True)#,related="n_preco.valor"
     iva_incluido = fields.Boolean(string='IVA Incluido', related="n_preco.iva_incluido", store=True)
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

     taxa = fields.Float(related = 'iva_id.taxa')

     stock = fields.One2many('artigo.artigo', 'id', string='preco', oldname='preco_line')

     ccodart = fields.Char()
     ccodart1 = fields.Integer()
     ccodcon = fields.Char()


     """
     @api.constrains('date_release')
     def check_name(self):
          if not self.date_release:
               raise exceptions.ValidationError(
                    "Data de lançamento must be filled!!!"
               )"""

     _sql_constraints = [
          ('codigo', 'unique(codigo)', 'Codigo already exists'),
     ]

     @api.model
     def create(self, vals):
          vals['codigo'] = self.env['ir.sequence'].next_by_code('art.codigo') or _('New')
          #codigo = vals.get('codigo')  # obter codigo da forma
          #if codigo:
          #     pass  # você pode fazer algo com ele, por exemplo, pesquisando
          res = super(artigo, self).create(vals)
          # res.gerar()
          return res  # finalmente, chame o método create da superclasse e crie o registro depois que você terminar
