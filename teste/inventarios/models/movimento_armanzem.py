# -*- coding: utf-8 -*-

from odoo import models, fields, api

class movimentoArmazem(models.Model):
    _name = 'movimento.armazem'
    _description = 'Movimento do Armazem'
    armazem = fields.Many2one('armanzem.armanzem', string="Armazem")
    artigo_id = fields.Many2one('artigo.artigo', string="Artigo")
    data_de = fields.Date(string="De")
    data_ate = fields.Date(string="Ate")
    movimento_armanzem=fields.One2many('guia.entrada', 'id')