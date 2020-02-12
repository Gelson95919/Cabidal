# -*- coding: utf-8 -*-

from odoo import models, fields, api

class configurarprocesso(models.Model):
    _name = 'configurar.processo'
    #_rec_name = 'name'
    _description = 'Configuração de Processos'

    processo = fields.Integer(string="Processo")
    desc = fields.Char(string="Descrição")
    tipo = fields.Selection([('anual', 'Anual'), ('mensal', 'Mensal'),], string="Tipo")
    fase = fields.Integer(string="Fase")
    descricao = fields.Char(string="Descrição")

    mes_inicio = fields.Integer(string="Mes Inicio")
    mes_fim = fields.Integer(string="Mes Final")
    mes_contrapartida = fields.Integer(string="Mes Contrapartida")
    dia_contrapartida = fields.Integer(string="Dia Contrapartida")
    agrupar_por = fields.Selection([('codigoterceiro', 'Codigo Terceiro'), ('centroanalisis', 'Centro Analisis'),],string="Agrupar Por")
    unico = fields.Char(string="Unico")
    mesmo_ano = fields.Boolean(string="Descrição")

    tipo_movi = fields.Selection([('reflectivo', 'Reflectivo'), ('translativo', 'Translactivo'),],string="Movimento", default='reflectivo')
    descri = fields.Char(string="Desc")
    diario = fields.Many2one('diario.diario', string="Diario")
    no_ordem = fields.Char(string="No.Ordem")

    tree_contrapartida = fields.One2many('configurar.processo', 'id', string="Tree")
    conta_saldo = fields.Many2one('planconta.planconta', string="Conta a Saldar")
    descricao_conta = fields.Char(string="Descrição", related="conta_saldo.nome", store=True)
    contrapartida = fields.Many2one('planconta.planconta', string="Conta a Saldar")
    descricao_contra = fields.Char(string="Descrição", related="contrapartida.nome", store=True)

    tree1 = fields.One2many('configurar.processo', 'id')



