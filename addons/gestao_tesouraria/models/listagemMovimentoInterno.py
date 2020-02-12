# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class litregpag(models.TransientModel):
     _name = 'listagem.movimento.interno'
     _description = 'Listagem Movimento Interno'

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

          return self.env.ref('gestao_tesouraria.listagem_movimento_interno_report').report_action(self, data=data)


class ListagemMovInter(models.AbstractModel):
    """Modelo abstrato para o modelo de relatório.

    Para `_name` model, Por favor, use `report.` como prefixo, em seguida, adicione `module_name.report_name`.
    """

    _name = 'report.gestao_tesouraria.listagem_movimento_interno_report_view'

    @api.model
    def _get_report_values(self, docids, data=None):
        date_start = data['form']['date_start']
        date_end = data['form']['date_end']


        docs = []
        list_mov_int = self.env['pagamento.recebimento'].search([('date', '>=', date_start), ('date', '<=', date_end), ('type_docum', '=', 'movimento'), ('mov_sai', '=', False)], order='name asc')
        for lmi in list_mov_int:

            docs.append({
                'date_release': lmi.date_release,
                'n_pagam': lmi.n_pagam,
                 'cheque': lmi.cheque,
                 'nome_conta_origem': lmi.nome_conta_origem,
                 'nome_conta_dest': lmi.nome_conta_dest,
                'montante_mov': lmi.montante_mov,
                'anulado': lmi.anulado,
                'detalhes': lmi.detalhes,

            })

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'date_start': date_start,
            'date_end': date_end,
            'docs': docs,
        }
