# -*- coding: utf-8 -*-

from odoo import models, fields, api

class deocumentoIngresso(models.Model):
    _name = 'remuner.deocumento.ingresso'
   #_rec_name = 'name'
    _description = 'Remunerações Documento Ingresso'
    name = fields.Char(string='Descrição')
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

class motivoDemissao(models.Model):
    _name = 'remuner.motivo.demissao'
    #_rec_name = 'name'
    _description = 'Remunerações Motivo Demissão'

    name = fields.Char(string='Descrição')

    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)
