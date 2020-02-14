# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class litregpag(models.TransientModel):
     _name = 'listagem.encontro.conta'
     _description = 'Listagem Encontro Conta'

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

          return self.env.ref('gestao_tesouraria.listagem_encontro_conta_report').report_action(self, data=data)


class ListagemEncontroConta(models.AbstractModel):
    """Modelo abstrato para o modelo de relatório.

    Para `_name` model, Por favor, use `report.` como prefixo, em seguida, adicione `module_name.report_name`.
    """

    _name = 'report.gestao_tesouraria.listagem_encontro_conta_report_view'

    @api.model
    def _get_report_values(self, docids, data=None):
        date_start = data['form']['date_start']
        date_end = data['form']['date_end']


        docs = []
        list_enc_conta = self.env['econtroconta.econtroconta'].search([('data', '>=', date_start), ('data', '<=', date_end)], order='name asc')
        for enc in list_enc_conta:

            docs.append({
                'numero': enc.numero,
                'cod_terc': enc.cod_terc,
                'name': enc.name,
                 'tot_parc_credito': enc.tot_parc_credito,
                 'data': enc.data,
                'anulado': enc.anulado,


            })

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'date_start': date_start,
            'date_end': date_end,
            'docs': docs,
        }
