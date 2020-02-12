# -*- coding: utf-8 -*-

from odoo import api, fields, models


class fichaCredito(models.TransientModel):
    _name = 'ficha.credito'
    _description = 'Ficha Credito'

    date_start = fields.Date('De')
    date_end = fields.Date('Ate')

    @api.multi
    def get_report(self):
        """Ligue quando o botão "Get Report" for clicado.
        """
        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'date_start': self.date_start,
                'date_end': self.date_end,

            },
        }

        return self.env.ref('gestao_relatorio.rep_fich_solicitacaor').report_action(self, data=data)


class catRisc(models.AbstractModel):
    """Modelo abstrato para o modelo de relatório.

    Para `_name` model, Por favor, use `report.` como prefixo, em seguida, adicione `module_name.report_name`.
    """

    _name = 'report.gestao_relatorio.rep_ficha_solicit_view'

    @api.model
    def _get_report_values(self, docids, data=None):
        date_start = data['form']['date_start']
        date_end = data['form']['date_end']

        docs = []

        prev = self.env['reg.docum'].search(
            [('data_documento', '>=', date_start), ('data_documento', '<=', date_end), ('cobrado', '=', False), ('prest_zerro', '=', False)])
        for f in prev:
            docs.append({
                'numero_credito': f.numero_credito,
                'codigo_terc': f.codigo_terc,
                'nome_terceiro': f.nome_terceiro,
                'valor_desembolso': f.valor_desembolso,
                'valor_pago': f.prestacao,
                'valor_atrazo': f.valor_desembolso,
                # 'indici_atraso': f.indici_atraso,
                'valor_em_risco': f.valor_desembolso,

            })

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'date_start': date_start,
            'date_end': date_end,

    }
