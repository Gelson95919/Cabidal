# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class litregpag(models.TransientModel):
     _name = 'litregpag.litregpag'
     _description = 'Listagem Registo Pagamento'

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

          return self.env.ref('gestao_tesouraria.listagem_pagamento_report').report_action(self, data=data)


class listRegPag(models.AbstractModel):
    """Modelo abstrato para o modelo de relatório.

    Para `_name` model, Por favor, use `report.` como prefixo, em seguida, adicione `module_name.report_name`.
    """

    _name = 'report.gestao_tesouraria.listagem_pagamento_report_view'

    @api.model
    def _get_report_values(self, docids, data=None):
        date_start = data['form']['date_start']
        date_end = data['form']['date_end']


        docs = []
        list_pag = self.env['tesouraria.pagamento'].search([('date', '>=', date_start), ('date', '<=', date_end), ('type_docum', '=', 'pagamento')], order='name asc')
        for l in list_pag:

            docs.append({
                'n_recibo': l.n_pagam,
                'date': l.date,
                 'nome_terceiro': l.nome_terceiro,
                 'valor_total_pag': l.valor_total_pag,
                 'detalhes': l.detalhes})

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'date_start': date_start,
            'date_end': date_end,
            'docs': docs,
        }
