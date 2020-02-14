# -*- coding: utf-8 -*-

from odoo import api, fields, models


class historicoReembolso(models.TransientModel):
    _name = 'historico.reembolso'
    _description = 'Histórico de Riembolso'

    num_credito = fields.Char(string='Numento Credito', store=True)


    @api.multi
    def get_report(self):
        """Ligue quando o botão "Get Report" for clicado.
        """
        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'num_credito': self.num_credito,

            },
        }

        return self.env.ref('gestao_relatorio.historico_reembolso_report').report_action(self, data=data)


class historico(models.AbstractModel):
    """Modelo abstrato para o modelo de relatório.

    Para `_name` model, Por favor, use `report.` como prefixo, em seguida, adicione `module_name.report_name`.
    """

    _name = 'report.gestao_relatorio.listagem_historico_reembolso_view'

    @api.model
    def _get_report_values(self, docids, data=None):
        num_credito = data['form']['num_credito']

        docs = []
        dados_emprest = []

        hist_reembolso = self.env['reg.docum'].search([('numero_credito', '=', num_credito)], order='id asc')
        at_dado_cred = self.env['acta.comite'].search([('numero_credito', '=', num_credito)], order='id asc')
        dado_client = self.env['clientes'].search([('nome_terc', '=', at_dado_cred.identificacao_proponente.id)], order='id asc')
        for f in hist_reembolso:
            docs.append({
                'valor_desembolso': f.valor_desembolso,
                'numer_prest': f.numer_prest,
                'data_documento': f.data_documento,
                'prestacao': f.prestacao,
                'juro_jerado': f.juro_jerado,
                'amortizacao': f.amortizacao,
                'divida': f.divida,

            })

        dados_emprest.append({
            'valor_total': at_dado_cred.valor_total,
            'amotizacao': at_dado_cred.amotizacao,
            'juros': at_dado_cred.juros,
            'numero_prestacoes': at_dado_cred.numero_prestacoes,
            'date_start': at_dado_cred.date_start,
            'valor': at_dado_cred.valor,
            'name_agente': at_dado_cred.name_agente,
            'num_cliente': at_dado_cred.valor,
            'codigo_cliente': dado_client.codigo_cliente,
            'name_prop': dado_client.name_prop,
        })



        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'agrup_agente': num_credito,
            'docs': docs,
            'dados_emprest': dados_emprest,
        }
