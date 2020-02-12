# -*- coding: utf-8 -*-

from odoo import models, fields, api

class detalhDocArmanz(models.Model):
    _name = 'detalhes.documento.armanzem'
    _rec_name = 'name'
    _description = 'Detalhes Documento Armazem'
    name = fields.Char(string="Descrição") #para remover no proximo BD
    preco_custo_meio = fields.Float('Preço custo Meio')
    artigo_id = fields.Many2one('artigo.artigo', string="Descrição")
    unidade_medida_arm = fields.Many2one('unimedida.unimedida', string='Unidade Medida')
    preco_custo = fields.Float('Preço custo', related="artigo_id.valor", store=True)
    quantidade = fields.Integer(string='Quantidade')
    sub_total = fields.Float(string='Sub Total', compute="_calcula_subtotal")
    ubicacoes = fields.Char()
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

    @api.one
    @api.depends('preco_custo','quantidade')
    def _calcula_subtotal(self):
        self.sub_total = self.preco_custo * self.quantidade

