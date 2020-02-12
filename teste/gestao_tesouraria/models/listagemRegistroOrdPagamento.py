# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class litregpag(models.TransientModel):
     _name = 'listagem.ordem.pagamento'
     _description = 'Listagem Registo Ordem Pagamento'

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

          return self.env.ref('gestao_tesouraria.listagem_ordem_pagamento_report').report_action(self, data=data)


class listOp(models.AbstractModel):
    """Modelo abstrato para o modelo de relatório.

    Para `_name` model, Por favor, use `report.` como prefixo, em seguida, adicione `module_name.report_name`.
    """

    _name = 'report.gestao_tesouraria.listagem_orde_pagamento_report_view'

    @api.model
    def _get_report_values(self, docids, data=None):
        date_start = data['form']['date_start']
        date_end = data['form']['date_end']


        docs = []
        list_ord_pag = self.env['tesouraria.ordem.pagamento'].search([('date_release', '>=', date_start), ('date_release', '<=', date_end)], order='id asc')
        for op in list_ord_pag:

            docs.append({
                'date_release': op.date_release,
                'numero': op.numero,
                 'numerof': op.numerof,
                 'fornecidor': op.fornecidor,
                 'montante': op.montante,


            })

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'date_start': date_start,
            'date_end': date_end,
            'docs': docs,
        }
