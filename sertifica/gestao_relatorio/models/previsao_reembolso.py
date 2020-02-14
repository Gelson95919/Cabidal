# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class previsaoReembolso(models.TransientModel):
     _name = 'previsao.reembolso'
     _description = 'Listagem Previsao Reembolso'

     date_start = fields.Date('De')
     date_end = fields.Date('Ate')
     agrup_por = fields.Boolean(string="Agrupar Por")
     por = fields.Selection([('1', 'Setor',), ('2', 'Localidade')], default="1", string="Por")
     agente = fields.Many2one('res.users', string="Agente")
     agrup_agente = fields.Boolean(string="Agrupar Por Agente")

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
                    'agente': self.agente.id,
                    'agrup_agente': self.agrup_agente,
               },
          }

          return self.env.ref('gestao_relatorio.previsao_reembolso_report').report_action(self, data=data)


class listaPrev(models.AbstractModel):
    """Modelo abstrato para o modelo de relatório.

    Para `_name` model, Por favor, use `report.` como prefixo, em seguida, adicione `module_name.report_name`.
    """

    _name = 'report.gestao_relatorio.listagem_previsao_reembolso_report_view'

    @api.model
    def _get_report_values(self, docids, data=None):
        date_start = data['form']['date_start']
        date_end = data['form']['date_end']
        agente = data['form']['agente']
        agrup_agente = data['form']['agrup_agente']



        docs = []
        if agrup_agente == True:
            prev = self.env['reg.docum'].search([('cobrado', '=', False), ('prest_zerro', '=', False), ('agente', '=', agente), ('data_documento', '>=', date_start), ('data_documento', '<=', date_end)])
            for f in prev:

                docs.append({
                    'numero_credito': f.numero_credito,
                    'numer_prest': f.numer_prest,
                    'codigo_terc': f.codigo_terc,
                    'nome_terceiro': f.nome_terceiro,
                    'data_documento': f.data_documento,
                    'total': f.total,
                    'capital': f.amortizacao,
                    'juro_jerado': f.juro_jerado,
                    #'obs': f.obs,


                })
        else:
            prev = self.env['reg.docum'].search(
                [('cobrado', '=', False), ('prest_zerro', '=', False), ('data_documento', '>=', date_start), ('data_documento', '<=', date_end)])
            for f in prev:
                docs.append({
                    'numero_credito': f.numero_credito,
                    'numer_prest': f.numer_prest,
                    'codigo_terc': f.codigo_terc,
                    'nome_terceiro': f.nome_terceiro,
                    'data_documento': f.data_documento,
                    'total': f.total,
                    'capital': f.amortizacao,
                    'juro_jerado': f.juro_jerado,
                    #'obs': f.obs,

                })
        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'date_start': date_start,
            'date_end': date_end,
            'agente': agente,
            'agrup_agente': agrup_agente,
            'docs': docs,
        }
