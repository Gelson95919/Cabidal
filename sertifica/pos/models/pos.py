# -*- coding: utf-8 -*-

from odoo import models, fields, api
class pos(models.Model):
     _name = 'pos.pos'
     _description = 'POS'
     cliente_id =fields.Many2one('terceiro.terceiro', string="Cliente")
     nif =fields.Integer(string="NIF", related="cliente_id.nif", store=True)
     endereco = fields.Char(string="Endereço", related="cliente_id.street", store=True)
     artigo_id =fields.Many2one('artigo.artigo', string="Produto")
     quantidade=fields.Float(string='Quantidade')
     preco_unitario=fields.Float(string="Prec.Unitario", related="artigo_id.preco_custo", store=True)
     iva = fields.Selection(string="Iva", related="artigo_id.ivasel", store=True)
     parcial=fields.Float(string="Parcial")
     dto=fields.Float(string="Dto.")
     quadro_pos=fields.One2many('pos.pos', 'id')
     total_venda=fields.Float(string="Total Venda")
     forma_pagamento=fields.Selection([('dinheiro', 'Dinheiro'), ('cartao', 'Cartão'), ('credito', 'Credito'), ('dinh_cart_cred', 'Dinh.Cart.Cred'), ('dinh_cart', 'Dinh.Cart'), ('dinh_cred', 'Dinh.Cred'),  ('cart_cred', 'Cart.Cred')], default='dinheiro')
     efectivo_recebido = fields.Float(string="Efectivo Recebido")
     cartao = fields.Float(string="Cartão")
     credito = fields.Float(string="Credito")
     troco = fields.Float(string="Troco")
     imprimir=fields.Boolean(string="Imprimir V.D")
     auto_venda=fields.Boolean(string="Auto Venda")
     imprimir_ticket=fields.Boolean(string="Imprimir Ticket")

class caixa(models.Model):
    _name = 'caixa.caixa'
    _rec_name = 'name'
    _description = 'Caixa'

    name = fields.Char(string="Descrição")
    cod = fields.Integer(string="Codigo")
    utilizador_id = fields.Many2one('res.users', string="Utilizador")
    permit_recebiment = fields.Boolean(string="Permitir Recebimentos")
    permit_pag = fields.Boolean(string="Permitir Pagamentos")
    permit_anul = fields.Boolean(string="Permitir Anular")
    numeros_independent = fields.Boolean(string="Numeros Indipendentes")

    #CAMPO DE CONTROLO
    type = fields.Selection(
        [('caixa_pos', 'Caixa Pos'), ('caixa_restourante', 'Caixas restourante')],
        readonly=True, index=True, change_default=True, default=lambda self: self._context.get('type', 'caixa_pos'),
        track_visibility='always')

class abrirCaixa(models.Model):
    _name = 'abrir.caixa'
    #_rec_name = 'name'
    _description = 'Abrir Caixa'
    caixa_id = fields.Many2one('caixa.caixa', string="Caixa")
    utilizador_id = fields.Many2one('res.users', string="Utilizador")
    armazem_id = fields.Many2one('armazem.armazem', string="Armazem")
    data_abertura = fields.Datetime(string="Data", default=fields.Datetime.today)
    data_fecho = fields.Datetime(string="Data", default=fields.Datetime.today)
    montante_total_movimento = fields.Float(string="Montante Total Movimento")
    doc_intern_fecho = fields.Char(string="Documento Interno de Fecho")
    f_pag = fields.Selection(
        [('dinheiro', 'Dinheiro'), ('cartao', 'Cartão'), ('credito', 'Credito'), ('dinh_cart_cred', 'Dinh.Cart.Cred'),
         ('dinh_cart', 'Dinh.Cart'), ('dinh_cred', 'Dinh.Cred'), ('cart_cred', 'Cart.Cred')], default='dinheiro')

    # CAMPO DE CONTROLO
    type = fields.Selection(
        [('aber_caixa_pos', 'Abre Caixa Pos'), ('aber_caixa_restourante', 'Abre Caixas restourante')],
        readonly=True, index=True, change_default=True, default=lambda self: self._context.get('type', 'aber_caixa_pos'),
        track_visibility='always')


