
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class altercoesMensais(models.Model):
    _name = 'altercoes.mensais'
    _description = 'Alterações Mensais'

    funcionario_id = fields.Many2one('funcionario.remuneracoes')
    data = fields.Datetime(string="Data")
    faltas_processadas = fields.Many2one('faltas.faltas', string="Faltas Processadas")
    alteracoes_id = fields.Many2one('altercoes.mensais')
    dur =fields.Char(string="Duração")
    mes = fields.Selection(
        [('janeior', 'Janeiro'), ('fevereiro', 'Fevereiro'), ('marco', 'Março'), ('abril', 'Abril'), ('Maio', 'Maio'),
         ('junho', 'Junho'), ('julho', 'Julho'), ('agosto', 'Agosto'), ('setembro', 'Setembro'), ('outubro', 'Outubro'),
         ('novembro', 'Novembro'), ('dezembro', 'Dezembor'), ], string='Mes')

               #RMUNERACOES
    remuneracoes_lista = fields.One2many('altercoes.mensais', 'id')
    remuneracoes_id = fields.Many2one('remuneracoes.remuneracoes')
    desc_remuner = fields.Char(string="Descrição", related='remuneracoes_id.name')
    temp_qt = fields.Float(string="Tempo/Qt.")
    valor_auxil = fields.Float(string="Valor Auxiliar")

               #DESCONTOS
    descont_id = fields.Many2one('desconto.desconto')
    descre_descont = fields.Char(string="Descrição", related="descont_id.name")
    valor = fields.Float(string="Valor")
    desconto_lista = fields.One2many('altercoes.mensais', 'id')

    mes_remuner = fields.Selection(
        [('janeior', 'Janeiro'), ('fevereiro', 'Fevereiro'), ('marco', 'Março'), ('abril', 'Abril'), ('Maio', 'Maio'),
         ('junho', 'Junho'), ('julho', 'Julho'), ('agosto', 'Agosto'), ('setembro', 'Setembro'), ('outubro', 'Outubro'),
         ('novembro', 'Novembro'), ('dezembro', 'Dezembor'), ], string='Mes')

class altercoesMensaisFaltas(models.Model):
    #_name = 'altercoes.mensais.faltas'
    _description = 'Alteracoes Mensais Faltas'
    _inherit = 'altercoes.mensais'
    faltas = fields.Many2one('faltas.faltas', string="Falta")
    tipofalta = fields.Selection([('horas', 'Horas'), ('dias', 'Dias')], default="horas",related="faltas.tipofalta")
    duracao = fields.Float(string="Qt.")
    observacao = fields.Char(string="Observações")
    calindario = fields.Datetime(string="Dia")
    outras_alteracao = fields.One2many('altercoes.mensais', 'alteracoes_id')#Lista de lado Dereito na aba Faltas-->
    lista_faltas = fields.One2many('altercoes.mensais', 'alteracoes_id')  # Lista de lado Esquerdo na aba Faltas



class altercoesMensaisHoras(models.Model):
    #_name = 'altercoes.mensais.horas'
    _inherit = 'altercoes.mensais'
    _description = 'Alteracoes Mensais Horas'
    horas_extra_processadas = fields.Many2one('horas.extras', string="Horas Extra Processadas")
    horas = fields.Many2one('horas.extras', string="Hora Extra")
    lista_horas = fields.One2many('altercoes.mensais', 'alteracoes_id')#Lista de lado Esquerdo na aba Hors
    outras_alteracao_horas = fields.One2many('altercoes.mensais', 'alteracoes_id')#Lista de lado Dereito na aba Horas