# -*- coding: utf-8 -*-

from odoo import models, fields, api

class situacoes(models.Model):
    _name = 'situacoes.situacoes'
    _rec_name = 'name'
    _description = 'Situações'
    name = fields.Char(string="Descrição")
    estado = fields.Selection([('ativo', 'Activo'), ('baixatemporada', 'Baixa temporada'), ('inativo', 'Inativo'),
                                       ('baixaprolongada', 'Baixa prolongada')], string="Aredondamento",  default = 'ativo')
    baixa_prolong = fields.Many2one('faltas.faltas')
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)


class categorias(models.Model):
    _name = 'categorias.categorias'
    _rec_name = 'name'
    _description = 'Categorias'

    name = fields.Char(string="Descrição")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)


class profecoes(models.Model):
    _name = 'profecoes.profecoes'
    _rec_name = 'name'
    _description = 'Profissões'

    name = fields.Char(string="Descrição")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)


class habilitacoes(models.Model):
    _name = 'habilitacoes.habilitacoes'
    _rec_name = 'name'
    _description = 'Habilitações'

    name = fields.Char(string="Descrição")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

class estadoCivil(models.Model):
    _name = 'estado.civil'
    _rec_name = 'name'
    _description = 'Estado Civil'

    name = fields.Char(string="Descrição")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)
