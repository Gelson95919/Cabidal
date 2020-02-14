# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class aluno(models.Model):
    _name = 'aluno.aluno'
    _rec_name = 'name'
    _description = 'Aluno'

    name = fields.Char(string="Descricao")
    detalhes = fields.One2many('matricula.matricula', 'aluno')
    nif = fields.Integer()
    morada =fields.Char()
    idade = fields.Integer()
    sexo = fields.Selection([('feminino', 'Feminino'), ('masculino', 'Masculino')], default='feminino')
    bi = fields.Integer()
    concelho = fields.Char()
    e_mail = fields.Char()
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)




