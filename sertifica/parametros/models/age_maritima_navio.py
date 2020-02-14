# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class navios(models.Model):
    _name = 'navios.navios'
    _rec_name = 'name'
    _description = 'Navio'

    name = fields.Char(string="Nome")
    navio_nacional = fields.Boolean(string="Navio Nacional")
    matriculo = fields.Char()
    num_imo = fields.Char()
    call_sing= fields.Char()
    nacionalidade = fields.Many2one('nacionalidade.nacionalidade')
    classe = fields.Many2one('classe.navio')
    porto_registro =fields.Char()
    numero_tripulante = fields.Integer()
    local_construcao =fields.Char()
    ano_construcao = fields.Date()
    armador = fields.Many2one('terceiro.terceiro')
    comandante_capitao = fields.Char()
    conta = fields.Many2one('planconta.planconta')
    tipo_carga = fields.Many2one('tipo.carga')
    combustivel = fields.Many2one('combustivel.combustivel')
    quantidade_combustivel = fields.Float()
    quanti_agua = fields.Float()
    velocidade = fields.Float()
    arquecao_bruta = fields.Float()
    numero_poroes = fields.Float()
    arquecao_liquida = fields.Float()
    Comprimento = fields.Float()
    calado_maximo = fields.Float()
    largura_boca = fields.Float()
    potencia_cavalo = fields.Float()
    marca_motor = fields.Char()
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

