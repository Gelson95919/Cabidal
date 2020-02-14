# -*- coding: utf-8 -*-

from odoo import models, fields, api

class consultaextracto(models.Model):
    _name = 'consulta.extracto'
    #_rec_name = 'name'
    _description = 'Consulta Extracto'

    tipo = fields.Selection(
        [('porconta', 'Por Contas'), ('porterceiro', 'Por Terceiros'), ('porcentrocusto', 'Por Centro de Custo'), ('porfluxocaixa', 'Por Fluxo Caixa'), ],
        string='Tipo', default='porconta')
    conta =fields.Many2one('planconta.planconta', string='Conta', domain=[('grupo', '=', False)])
    data_realizado = fields.Date(string="Data",  default=fields.Date.today)
    terceiro = fields.Many2one('terceiro.terceiro', string='Terceiro')
    periodo = fields.Char(string='Periodo', comput="add_ano")
    lansamendo_ids = fields.One2many('lancamento_diario.lancamento_diario', 'consult_extrat_id', string="Lançamento")
    select = fields.Boolean(string="Selecionar")
    tot_1 = fields.Float(string='')
    tot_2 = fields.Float(string='')

    @api.model
    @api.onchange('data_realizado')
    def add_ano(self):
        dat = self.data_realizado
        d = str(dat)
        x = d.split('-')
        datefec = x
        list = []
        for a in datefec:
            list.append(a)
        self.periodo = list[0]

    def _comput_line(self, line):
        return {'displlay_type': line.displlay_type, 'state': 'draft', }


    @api.model
    @api.onchange('terceiro')
    def selecionar(self):
            domain = ''
            if self.tipo == 'porterceiro':
                domain = [('terceiro_id_doc_conta_corente_receb', '=', self.terceiro.id)]
            elif self.tipo == 'porconta':
                domain = [('conta_d', '=', self.conta.id)]
            else:
                pass #Falta adicionar por centro custo e por Fluxo de caixa

            select_pres = self.env['lancamento_diario.lancamento_diario'].search(domain)
            list_of_docum = []
            for line in select_pres:
                data = self._comput_line(line)
                data.update({'diamov': line.diamov, 'mesmov': line.mesmov,  'anomov': line.anomov,  'ordem': line.ordem,
                             'cod_terce': line.cod_terce, 'nome_conta': line.nome_conta, 'debito': line.debito, 'credito': line.credito})
                list_of_docum.append((1, line.id, data))
            return {'value': {"lansamendo_ids": list_of_docum}}