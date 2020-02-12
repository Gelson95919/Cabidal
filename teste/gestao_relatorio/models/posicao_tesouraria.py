# -*- coding: utf-8 -*-

from odoo import api, fields, models


class posicaoTesoura(models.TransientModel):
    _name = 'posicao.tesouraria'
    _description = 'Posição de Tesouraria'

    date_start = fields.Date('De')
    date_end = fields.Date('Ate')
    tot_despo = fields.Float('Total Desp', compute="get_report")

    @api.multi
    def get_report(self):
        """Ligue quando o botão "Get Report" for clicado.
        """
        folha = self.env['folha.tesouraria'].search([('name', '!=', ' ')])
        for f in folha:
            self.tot_despo += f.sald_sigu
        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'date_start': self.date_start,
                'date_end': self.date_end,
                'tot_despo': self.tot_despo,

            },
        }

        return self.env.ref('gestao_relatorio.listagem_folha_tesouraria_report').report_action(self, data=data)


class posTeso(models.AbstractModel):
    """Modelo abstrato para o modelo de relatório.

    Para `_name` model, Por favor, use `report.` como prefixo, em seguida, adicione `module_name.report_name`.
    """

    _name = 'report.gestao_relatorio.listagem_folha_tesoura_report_view'

    @api.model
    def _get_report_values(self, docids, data=None):
        date_start = data['form']['date_start']
        date_end = data['form']['date_end']
        tot_despo = data['form']['tot_despo']

        docs = []
        folha = self.env['folha.tesouraria'].search([('name', '!=', ' ')])
        for f in folha:
            docs.append({
                'codigo': f.codigo,
                'name': f.name,
                'sald_sigu': f.sald_sigu,

            })

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'date_start': date_start,
            'date_end': date_end,
            'tot_despo': tot_despo,
            'docs': docs,

    }


