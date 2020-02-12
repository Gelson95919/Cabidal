# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class notacred(models.Model):
     _name = 'notacred.notacred'

     date_release = fields.Date('Data de lançamento')
     name = fields.Char(string='Descrição')
     armazem = fields.Many2one('armanzem.armanzem', string='Armanzem')
     nometerc = fields.Many2one('terceiro.terceiro', string='Nome')
     nif = fields.Integer(string='NIF', readonly=True, related="nometerc.nif", store=True)
     street2 = fields.Char(string='Endereço', readonly=True, related="nometerc.street2", store=True)
     forma = fields.Many2one('pagamento.pagamento', string='Forma')
     moeda = fields.Many2one('moeda.moeda', string='Moeda')
     numerof = fields.Char(string='Numero')
     date = fields.Date('Data')
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
     montante = fields.Float(string='Montante')

     preco3 = fields.One2many('notacred.notacred', 'id', string='preco', oldname='preco_line')
     ivamo = fields.Many2one('iva.iva', string='IVA')
     contabiliza = fields.Boolean(string='Contabilizado')
     diario = fields.Integer(string='Diario')
     numero = fields.Integer(string='Numero')

     desconto = fields.Float(string='Desconto')
     ivar = fields.Many2one('iva.iva', string='IVA')
     totalr = fields.Float(string='Total')




