
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class processamentoAutomaticoRemuneracoes(models.Model):
    _name = 'processamento.automatico.remuneracoes'
    _description = 'Processamento Automático Remunerações'
    tipo_process = fields.Selection([('processar', 'Processar'), ('anular', 'Anular')], default="processar")
    mes = fields.Selection(
        [('01', '01-Janeiro'), ('02', '02-Fevereiro'), ('03', '03-Março'), ('04', '04-Abril'), ('05', '05-Maio'),
         ('06', '06-Junho'), ('07', '07-Julho'), ('08', '08-Agosto'), ('09', '09-Setembo'), ('10', '10-Outubro'), ('11', '11-Novembro'),
         ('12', '12-Dezembro')], string='Mes')
    data_process = fields.Date(string="Ult.Process", default=fields.Date.today)
    ano = fields.Date()
    remuneracoes_ids = fields.One2many('processamento.automatico.remuneracoes', 'id')
    processar = fields.Boolean(string="Processar")
    anular = fields.Boolean(string="Anular")
    tipo_organis = fields.Selection([('porNome', 'Por Nome'), ('porCodigo', 'Por Codigo')], default="porNome")
    contabilizado = fields.Boolean(string="Contabilizar")
    numero = fields.Integer(string="Numero")

class processamento(models.Model):
    #_name = 'new_module.new_module'
    _inherit = 'processamento.automatico.remuneracoes'
    _description = 'Processamento Automático Remunerações'
    funcionario_id = fields.Many2one('funcionario.remuneracoes', string="Nome")


