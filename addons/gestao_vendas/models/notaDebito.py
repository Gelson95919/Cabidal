# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning


class notadebito(models.Model):
     _name = 'notadebito.notadebito'


     armazem = fields.Many2one('armanzem.armanzem', string='Armanzem')
     nome = fields.Many2one('terceiro.terceiro', string='Nome')
     date_release = fields.Date('Data de lançamento')
     nif = fields.Integer(string='NIF', readonly=True, related="nome.nif", store=True)
     street2 = fields.Char(string='Endereço', readonly=True, related="nome.street2", store=True)
     forma = fields.Many2one('pagamento.pagamento', string='Forma')
     moeda = fields.Many2one('moeda.moeda', string='Moeda')
     date = fields.Date('Data')
     numerof = fields.Char(string='Numero')

     processo = fields.Char(string='Processo')
     name = fields.Char(string='Descrição')


     descricao = fields.Many2one('artigo.artigo', string='Descrição')
     preco_unitario = fields.Float(string='Preço Unitario')
     quantidade = fields.Float(string='Quantidade')
     iva = fields.Many2one('iva.iva', string='IVA')
     sub_total = fields.Float(string='Sub Total')
     arigo_servico = fields.Char(string='Artigo')



     total_preco_unt = fields.Float(string='Total Preço Unitario')
     total = fields.Float(string='Total')
     aredondamento = fields.Boolean(string='Aredondamento')
     artigoob = fields.Many2one('artigo.artigo', string='Artigo')
     obs = fields.Text(string='OBS')
     montante = fields.Char(string='Montante')

     preco2 = fields.One2many('notadebito.notadebito', 'id', string='preco', oldname='preco_line')
     ivamo = fields.Many2one('iva.iva', string='IVA')
     contabiliza = fields.Boolean(string='Contabilizado')
     diario = fields.Integer(string='Diario')
     numero = fields.Char(string='Numero')

     desconto = fields.Float(string='Desconto')
     ivar = fields.Many2one('iva.iva', string='IVA')
     totalr = fields.Float(string='Total')

     #nome = fields.Many2one('terceiro.terceiro', string='Terceiro')
     #notadebito_id = fields.Many2one('notadebito.notadebito', string='Nota Debito')
     """        
     @api.onchange('descricao')
     def _onchange_descricao(self):
          domain = {}
          if not self.notadebito_id:
               return

          part = self.notadebito_id.nome
          if not part:
               warning = {
                  'title': _('Warning!'),
                  'message': _('You must first select a partner!'),
               }
               return {'warning': warning}"""

