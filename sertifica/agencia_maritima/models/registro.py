# -*- coding: utf-8 -*-

from odoo import models, fields, api

class registro(models.Model):
   _name = 'registro'
   _description = "Registro"
   viagem = fields.Char(string="Viagem")
   navio_motor_id = fields.Many2one('navios.navios', string="Navio")
   motivo_escala_id = fields.Many2one('motivo.escala', string="Escala")
   armador_id = fields.Many2one('terceiro.terceiro', string="Armador")
   fretador_id = fields.Many2one('terceiro.terceiro', string="Fretador")
   data_entrada = fields.Datetime(string="Data Entrada")
   porto_agencia_id = fields.Many2one('portos.escalas', string="Porto")
   procedencia_id = fields.Many2one('portos.escalas', string="Procedencia")
   embarcados = fields.Integer(string="Embarcados")
   desembarcado = fields.Integer(string="Desenbarcado")
   carregada = fields.Float(strging="Carregadas")
   descaregadas = fields.Float(strging="Descaregadas")
   data_saida = fields.Datetime(string="Data Saida")
   porto_id_1 = fields.Many2one('portos.escalas')
   porto_id_2 = fields.Many2one('portos.escalas')
   porto_id_3 = fields.Many2one('portos.escalas')
   porto_id_4 = fields.Many2one('portos.escalas')
   porto_id_5 = fields.Many2one('portos.escalas')
   porto_id_6 = fields.Many2one('portos.escalas')
   porto_id_7 = fields.Many2one('portos.escalas')
   porto_id_8 = fields.Many2one('portos.escalas')
   porto_id_9 = fields.Many2one('portos.escalas')
   numero_tripolante = fields.Integer(string="Numero Tripolante")
   contracto = fields.Selection([('liner', 'Liner'), ('liner_out', 'Liner Out'), ('full_liner', 'Full Liner'), ('out', 'Outro')], default="liner")
   obsevacao = fields.Text(string="Observacao")
   conta_id = fields.Many2one('planconta.planconta', string="Plano Conta")
   terceiro_id = fields.Many2one('terceiro.terceiro', string="Terceiro")
   comandante = fields.Char(string="Comandante")
   outro = fields.Char(string="Outros")
