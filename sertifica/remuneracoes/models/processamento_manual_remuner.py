
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class processamentoManualRemuneracoes(models.Model):
    _name = 'processamento.manual.remuneracoes'
    _description = 'Processamento Manual Remunerações'
    funcionario_di = fields.Many2one('funcionario.remuneracoes')
    #mes = fields.Selection([('01', '01-Janeiro'), ('02', '02-Fevereiro'), ('03', '03-Março'), ('04', '04-Abril'), ('05', '05-Maio'), ('06', '06-Junho'),
    #                        ('07', '07-Julho'), ('08', '08-Agosto'), ('09', '09-Setembo'), ('10', '10-Outubro'), ('11', '11-Novembro'), ('12', '12-Dezembro'),])
    ano = fields.Date(string="Ano")
    remuneracoes_salario_ids = fields.One2many('remuneracoes.salario', 'processamento_manual_id', string="Remunerações Fixas")
    descontos_salario_ids = fields.One2many('desconto.salario', 'processamento_manual_id',
                                       string="Descontos Fixos")
    alteracoes_list_ids = fields.Many2many('alteracoes.mensais.process.manual', 'process_manual_id')



class alteracoesMensaisProcesManual(models.Model):
    _name = 'alteracoes.mensais.process.manual'
    #_rec_name = 'name'
    _description = 'Alterações Mensais Process Manual'

    tipo = fields.Selection([('falta', 'Faltas'), ('horas', 'Horas'), ('remuneracoes', 'Remunerações'), ('descontos', 'Derscontos')], default = "falta", string="Tipo")
    falta_id = fields.Many2one('faltas.faltas', string="Faltas")
    hora_id = fields.Many2one('horas.extras', string="Horas")
    remuneracao_id = fields.Many2one('remuneracoes.remuneracoes', string="Remuneracoes")
    desconto_id = fields.Many2one('desconto.desconto', string="Descontos")
    montante = fields.Integer(string="Qt./Montante")
    mes = fields.Date(string="Data")
    process_manual_id = fields.Many2one('processamento.manual.remuneracoes')

