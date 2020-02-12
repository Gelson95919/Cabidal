# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class listagFofla(models.TransientModel):
     _name = 'listagem.folha.tesouraria'
     _description = 'Listagem Folha Tesouraria'

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

          return self.env.ref('gestao_tesouraria.listagem_folha_tesouraria_report').report_action(self, data=data)


class listaFol(models.AbstractModel):
    """Modelo abstrato para o modelo de relatório.

    Para `_name` model, Por favor, use `report.` como prefixo, em seguida, adicione `module_name.report_name`.
    """

    _name = 'report.gestao_tesouraria.listagem_folha_tesoura_report_view'

    @api.model
    def _get_report_values(self, docids, data=None):
        date_start = data['form']['date_start']
        date_end = data['form']['date_end']


        docs = []
        list_folha = self.env['folha.tesouraria'].search([('data', '>=', date_start), ('data', '<=', date_end)], order='name asc')
        for f in list_folha:

            docs.append({
                'movimento': f.movimento,
                'tot_parc_entrada': f.tot_parc_entrada,
                'tot_parc_saida': f.tot_parc_saida,
                 'saldo_ant': f.saldo_ant,
                 'fechado': f.fechado,
                'data': f.data,


            })

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'date_start': date_start,
            'date_end': date_end,
            'docs': docs,
        }
