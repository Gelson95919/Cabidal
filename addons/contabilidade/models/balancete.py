# -*- coding: utf-8 -*-

from odoo import models, fields, api

class balancete(models.TransientModel):
    _name = 'balancete.balancete'
    #_rec_name = 'name'
    _description = 'Balancete'
    tipo_balancete = fields.Selection([('razao', 'Razão Geral'), ('terceiro', 'Terceiro'), ('centrocusto','Centro Custo'),('graus','Graus')], string='tipo', default='razao')
    incluir_auxiliar = fields.Boolean(string ='Incluir Auxiliares')
    data_realizado = fields.Date(string="Data",  default=fields.Date.today)
    mes = fields.Selection(
        [('abertura', 'Abertura'), ('janeior', 'Janeiro'), ('fevereiro', 'Fevereiro'), ('marco', 'Março'),
         ('abril', 'Abril'), ('Maio', 'Maio'),
         ('junho', 'Junho'), ('julho', 'Julho'), ('agosto', 'Agosto'), ('setembro', 'Setembro'), ('outubro', 'Outubro'),
         ('novembro', 'Novembro'), ('dezembro', 'Dezembor'), ('rectificado', 'Rectificado'),
         ('antes_result', 'Antes dos Resultado'), ('dep_result', 'Depos dos Resultados')], string='Mes')
    acomulado =fields.Boolean(string='Acumulado')
    comparativo = fields.Boolean(string='Comparativo')
    mes1 = fields.Selection(
        [('abertura', 'Abertura'), ('janeior', 'Janeiro'), ('fevereiro', 'Fevereiro'), ('marco', 'Março'), ('abril', 'Abril'), ('Maio', 'Maio'),
         ('junho', 'Junho'), ('julho', 'Julho'), ('agosto', 'Agosto'), ('setembro', 'Setembro'), ('outubro', 'Outubro'),
         ('novembro', 'Novembro'), ('dezembro', 'Dezembor'), ('rectificado', 'Rectificado'), ('antes_result', 'Antes dos Resultado'), ('dep_result', 'Depos dos Resultados')], string='Mes')
    nivel = fields.Selection(
        [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
         ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),
         ('11', '11'), ], string='Nivel')
    inicio_conta =fields.Many2one('planconta.planconta', string='Inicio')
    fin_conta = fields.Many2one('planconta.planconta', string='Fim')
    ano = fields.Char(string='Ano', required=True, comput="add_ano")
    acomular_conta =fields.Boolean(string='Acomular Contas')

    inicio_terc = fields.Many2one('planconta.planconta', string='Inicio')
    fin_terce = fields.Many2one('planconta.planconta', string='Fim')

    inicio_centro_cust = fields.Many2one('planconta.planconta', string='Inicio')
    fin_centro_cust = fields.Many2one('planconta.planconta', string='Fim')

    tipo = fields.Selection([('conta','Conta'), ('alfabetico', 'Alfabetico')], default='conta')
    ordem = fields.Selection([('completo', 'Completo'), ('resumo', 'Resumo')], default='completo')

    formato_antigo = fields.Boolean(string='Formato Antigo')
    edit_report = fields.Boolean(string='Editar Relatorio')

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
        self.ano = list[0]

    def gerar(self):
        if self.tipo_balancete == 'razao':
            pass
        elif self.tipo_balancete == 'terceiro':
            pass
        elif self.tipo_balancete == 'centrocusto':
            pass
        elif self.tipo_balancete == 'graus':
            pass

        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'ano': self.ano,
                'mes': self.mes,
                'data_realizado': self.data_realizado,
            },
        }

        return self.env.ref('contabilidade.balancet_report').report_action(self, data=data)

class Balancet(models.AbstractModel):
        """Modelo abstrato para o modelo de relatório.

        Para `_name` model, Por favor, use `report.` como prefixo, em seguida, adicione `module_name.report_name`.
        """

        _name = 'report.contabilidade.balancet_report_view'

        @api.model
        def _get_report_values(self, docids, data=None):
            ano = data['form']['ano']
            mes = data['form']['mes']
            data_realizado = data['form']['data_realizado']
            domain = [('ano', '=', ano), ('mes', '=', mes)]
            docs = []
            list_balanc = self.env['razao.atualizado'].search(domain)

            for l in list_balanc:
                docs.append({
                    'conta_d': l.conta_d,
                    'conta': l.conta,
                    'descricao': l.descricao,
                    'deb_acum_mes': l.deb_acum_mes,
                    'cred_acum_mes': l.cred_acum_mes,
                    'deb_acum_mes_sig': l.deb_acum_mes_sig,
                    'cred_acum_mes_sig': l.cred_acum_mes_sig,
                    'sald_devedor': l.sald_devedor,
                    'sal_credor': l.sal_credor,})

            return {
                'doc_ids': data['ids'],
                'doc_model': data['model'],
                'ano': ano,
                'mes': mes,
                'data_realizado': data_realizado,
                'docs': docs,
            }



