# -*- coding: utf-8 -*-

from odoo import api, fields, models


class indicadores(models.TransientModel):
    _name = 'indicadores'
    _description = 'Indicadores'

    ano = fields.Integer(string='Ano')
    dia_atraso = fields.Integer(string='Dias de atraso')
    num_funcionario = fields.Integer('Num Funcionario')
    num_agentes = fields.Integer('Num Agente')

    @api.multi
    def get_report(self):
        """Ligue quando o botão "Get Report" for clicado.
        """
        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'ano': self.ano,
                'dia_atraso': self.dia_atraso,
                'num_funcionario': self.num_funcionario,
                'num_agentes': self.num_agentes,

            },
        }

        return self.env.ref('gestao_relatorio.indicadores_financeiro_report').report_action(self, data=data)


class indca(models.AbstractModel):
    """Modelo abstrato para o modelo de relatório.

    Para `_name` model, Por favor, use `report.` como prefixo, em seguida, adicione `module_name.report_name`.
    """

    _name = 'report.gestao_relatorio.listagem_indicadores_view'

    @api.model
    def _get_report_values(self, docids, data=None):
        ano = data['form']['ano']
        dia_atraso = data['form']['dia_atraso']
        num_funcionario = data['form']['num_funcionario']
        num_agentes = data['form']['num_agentes']

        docs = []
        prev = self.env['reg.docum'].search([])
        for f in prev:
            docs.append({
                'numero_credito': f.numero_credito,
                'codigo_terc': f.codigo_terc,
                'nome_terceiro': f.nome_terceiro,
                'valor_desembolso': f.valor_desembolso,
                'valor_pago': f.prestacao,
                'valor_atrazo': f.valor_desembolso,
                'valor_em_risco': f.valor_desembolso,

            })

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'ano': ano,
            'dia_atraso': dia_atraso,
            'num_funcionario': num_funcionario,
            'num_agentes': num_agentes,

    }
