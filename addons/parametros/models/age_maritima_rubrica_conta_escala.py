# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class rubricaContaEscala(models.Model):
    _name = 'agenc.rubrica.conta.escala'
    _rec_name = 'name'
    _description = 'Rubrica Contas Escala'

    name = fields.Char(string="Descrição")
    tipo = fields.Selection([('1', 'Despesas Navios Nacionais'), ('2', 'Despesas Navios Estrangeiros'), ('3', 'Receitas')],
                            'tipo', default='despesa_navio_nacional', widget='radio')
    valor_abusoluto = fields.Boolean()
    receitas = fields.Selection([('1', 'Passagem e Fretes/Entrada'), ('2', 'Passagem e Fretes/Saida'), ('3', 'Outros')],
                            'tipo', widget='radio')
    rub_idioma = fields.Selection(
        [('en', 'EN'), ('es', 'ES'),
         ('fr', 'FR')],
        'tipo', default='en', widget='radio')
    desc_idioma = fields.Char(string="Clase")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

