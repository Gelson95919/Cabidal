# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class reparticaoFinancas(models.Model):
     _name = 'reposicao.financas'
     _rec_name = 'name'
     _description = 'Reposição Finanças'
     name = fields.Char(string='Descrição')
     codigo = fields.Char(string="Codigo", required=True, copy=False, readonly=True, index=True,
                           store=True, )
     numero =fields.Integer(string="Numero")
     terceiro_id =fields.Many2one('terceiro.terceiro', string="Terceiro")
     cod_comp_id = fields.Many2one('compras.compras', string="Despesa")
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

     """@api.model
     def _get_next_cod(self):
         sequence = self.env['ir.sequence'].search([('code', '=', 'reparticao.financas.codigo')])
         next = sequence.get_next_char(sequence.number_next_actual)
         return next

     @api.model
     def create(self, vals):
         vals['codigo'] = self.env['ir.sequence'].next_by_code('reparticao.financas.codigo') or _('New')
         res = super(reparticaoFinancas, self).create(vals)

         return res"""





class segurancaSocial(models.Model):
    _name = 'seguranca.social'
    _rec_name = 'name'
    _description = 'Segurança Social'
    name = fields.Char(string='Descrição')
    descont_asoc_id = fields.Many2one('desconto.desconto', string="Desconto Asoc")
    funcionario = fields.Float(string="Funcionário")
    empresa = fields.Float(string="Empresa")
    plano_conta_id = fields.Many2one('planconta.planconta', string="Conta Contribuinte")
    plan_conta_id = fields.Many2one('planconta.planconta', string="Conta")
    terceiro_id = fields.Many2one('terceiro.terceiro', string="Terceiro")
    cod_comp_id = fields.Many2one('compras.compras', string="Despesa")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)







class sindicato(models.Model):
    _name = 'sindicato.sindicato'
    _rec_name = 'name'
    _description = 'Sindicato'
    name = fields.Char(string="Descrição")
    valor = fields.Float(string="Valor")
    calculo_em_percentario = fields.Boolean(string="Cálculo em Percentagem")
    volor_minimo = fields.Float(string="Valo Minimo")
    descont_asoc_id = fields.Many2one('desconto.desconto', string="Desconto Asoc")
    terceiro_id = fields.Many2one('terceiro.terceiro', string="Terceiro")
    cod_comp_id = fields.Many2one('compras.compras', string="Despesa")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)





class seguros(models.Model):
    _name = 'seguros.seguros'
    _rec_name = 'name'
    _description = 'Seguros'
    name = fields.Char(string="Descrição")
    descont_asoc_id = fields.Many2one('desconto.desconto', string="Desconto Asoc")
    funcionario = fields.Float(string="Funcionário")
    calculo_em_percentario = fields.Boolean(string="Cálculo em Percentagem")
    calcu_em_percentario = fields.Boolean(string="Cálculo em Percentagem")
    empresa = fields.Float(string="Empresa")
    plano_conta_id = fields.Many2one('planconta.planconta', string="Conta")
    terceiro_id = fields.Many2one('terceiro.terceiro', string="Terceiro")
    cod_comp_id = fields.Many2one('compras.compras', string="Despesa")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)
