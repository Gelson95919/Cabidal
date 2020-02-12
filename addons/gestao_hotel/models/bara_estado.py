# -*- coding: utf-8 -*-

from odoo import models, fields, api

class statusbar(models.Model):
    _name = 'statusbar.demo'
    name = fields.Char('Name', required=True)
    """
    Este campo de seleção contém todos os valores possíveis para a barra de status.
    A primeira parte é o valor do banco de dados, o segundo é a string que é mostrada. Exemplo:
    ('finished','Done'). 'finished 'é a chave do banco de dados e' Done 'o valor mostrado para o usuário
    """
    state = fields.Selection([
            ('concept', 'Conceito'),
            ('started', 'Começada'),
            ('progress', 'Em progresso'),
            ('finished', 'Feita'),
            ],default='concept')

    #Esta função é acionada quando o usuário clica no botão
    #'Definido para o conceito

    @api.one
    def concept_progressbar(self):
        self.write({
            'state': 'concept',
        })

    # Esta função é acionada quando o usuário clica no botão 'Definir para começar'
    @api.one
    def started_progressbar(self):
        self.write({
            'state': 'started'
        })

    # Esta função é acionada quando o usuário clica no botão 'Em progresso'
    @api.one
    def progress_progressbar(self):
        self.write({
            'state': 'progress'
        })

    # Esta função é acionada quando o usuário clica no botão 'Concluído'
    @api.one
    def done_progressbar(self):
        self.write({
            'state': 'finished',
        })