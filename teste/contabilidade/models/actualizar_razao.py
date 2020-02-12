# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class actualizarrazao(models.TransientModel):
    _name = 'actualizar.razao'
    #_rec_name = 'name'
    _description = 'Actualização da Razão'
    diario = fields.Many2one('diario.diario', string='Diario')
    data_realizado = fields.Date(string="Data",  default=fields.Date.today)
    mes = fields.Selection(
        [('1', 'Janeiro'), ('2', 'Fevereiro'), ('3', 'Março'), ('4', 'Abril'), ('5', 'Maio'),
         ('6', 'Junho'), ('7', 'Julho'), ('8', 'Agosto'), ('9', 'Setembro'), ('10', 'Outubro'),
         ('11', 'Novembro'), ('12', 'Dezembor'), ], string='Mes')
    tipo = fields.Selection([('dia', 'Dia'), ('documento', 'Documento'),], string='')
    tip_dia = fields.Integer(string='')
    tipo_doc = fields.Char(string='')

    @api.model
    def _default_periodo(self):
        domain = [('fecho', '=', False)]
        return self.env['periodo.periodo'].search(domain, limit=1)
    periodo = fields.Many2one('periodo.periodo', string='Periodo', default=_default_periodo, required=True)
    ano = fields.Char(string="Ano", related="periodo.codigo")

    def aceitar(self):
        domain = [('anomov', '=', self.ano), ('valor', '>', 0), ('atualizado', '=', False)]
        razao = self.env['lancamento_diario.lancamento_diario'].search(domain)
        for ra in razao:
            if ra.anomov != self.ano:
                raise ValidationError('Verifica se o periodo ja existe')
            ra.atualizado = True
            raz = self.env['razao.atualizado']
            atual_raz = raz.create({'conta_d': ra.conta_d.id, 'descricao': ra.nome_conta, 'deb_acum_mes': ra.valor,
                                    'cred_acum_mes': ra.valor, 'deb_acum_mes_sig': ra.valor,
                                     'cred_acum_mes_sig': ra.valor, 'sald_devedor': ra.valor, 'sal_credor': ra.valor,
                                     'data': self.data_realizado, 'ano': self.ano, 'mes': self.mes})




class razaoAtualizado(models.Model):
    _name = 'razao.atualizado'
    _description = 'Razão Atualizado'

    conta_d = fields.Many2one('planconta.planconta', store=True, domain=[('grupo', '=', False)])
    conta = fields.Char(string="Conta", related="conta_d.cod_plan_cont")
    descricao = fields.Char(string="Descrição", related="conta_d.nome")
    deb_acum_mes = fields.Float(string="Debito Acumulado de Mes")
    cred_acum_mes = fields.Float(string="Credito Acumulado de Mes")
    deb_acum_mes_sig = fields.Float(string="Debito Acumulado de Mes Siguinte")
    cred_acum_mes_sig = fields.Float(string="Credito Acumulado de Mes Siguinte")
    sald_devedor = fields.Float(string="Saldo Devedores")
    sal_credor = fields.Float(string="Saldo Creadores")
    data = fields.Date(string="Data")
    ano = fields.Char(string="Ano")
    mes = fields.Selection(
        [('1', 'Janeiro'), ('2', 'Fevereiro'), ('3', 'Março'), ('4', 'Abril'), ('5', 'Maio'),
         ('6', 'Junho'), ('7', 'Julho'), ('8', 'Agosto'), ('9', 'Setembro'), ('10', 'Outubro'),
         ('11', 'Novembro'), ('12', 'Dezembor'), ], string='Mes')



class reposcaoMovimento(models.TransientModel):
    _name = 'reposcao.movimento'
    # _rec_name = 'name'
    _description = 'Reposição Movimento'
    diario = fields.Many2one('diario.diario', string='Diario')
    mes = fields.Selection(
        [('1', 'Janeiro'), ('2', 'Fevereiro'), ('3', 'Março'), ('4', 'Abril'), ('5', 'Maio'),
         ('6', 'Junho'), ('7', 'Julho'), ('8', 'Agosto'), ('9', 'Setembro'), ('10', 'Outubro'),
         ('11', 'Novembro'), ('12', 'Dezembor'), ], string='Mes')
    tipo = fields.Selection([('dia', 'Dia'), ('documento', 'Documento'), ], string='')
    tip_dia = fields.Integer(string='')
    tipo_doc = fields.Char(string='')

    @api.model
    def _default_periodo(self):
        domain = [('fecho', '=', False)]
        return self.env['periodo.periodo'].search(domain, limit=1)

    periodo = fields.Many2one('periodo.periodo', string='Periodo', default=_default_periodo, required=True)
    ano = fields.Char(string="Ano", related="periodo.codigo")

    def aceitar_repor(self):
        domain = [('ano', '=', self.ano)]
        razao = self.env['razao.atualizado'].search(domain)
        for ra in razao:
            if ra.ano != self.ano:
                raise ValidationError('Verifica se o periodo ja existe')
            else:
                ra.unlink()
        domain = [('anomov', '=', self.ano), ('valor', '>', 0), ('atualizado', '=', True)]
        razao = self.env['lancamento_diario.lancamento_diario'].search(domain)
        for r in razao:
            r.atualizado = False
