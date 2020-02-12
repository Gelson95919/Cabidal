# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class carteraEmRisco(models.TransientModel):
     _name = 'carteira.em.risco'
     _description = 'Carteira em Risco'

     date_start = fields.Date('De')
     date_end = fields.Date('Ate')
     agente = fields.Many2one('res.users', string="Agente")
     agrup_agente = fields.Boolean(string="Agrupar Por Agente")
     data_realise = fields.Date(string="Data Realizado", default=fields.Date.today)

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
                    'data_realise': self.data_realise,
               },
          }

          return self.env.ref('gestao_relatorio.carteira_em_risco_report').report_action(self, data=data)


class catRisc(models.AbstractModel):
    """Modelo abstrato para o modelo de relatório.

    Para `_name` model, Por favor, use `report.` como prefixo, em seguida, adicione `module_name.report_name`.
    """

    _name = 'report.gestao_relatorio.listagem_carteira_em_risco_report_view'

    @api.model
    def _get_report_values(self, docids, data=None):
        date_start = data['form']['date_start']
        date_end = data['form']['date_end']
        agente = data['form']['agente']
        agrup_agente = data['form']['agrup_agente']
        data_realise = data['form']['data_realise']



        docs = []
        if agrup_agente == True:
            prev = self.env['reg.docum'].search([('agente', '=', agente), ('data_documento', '>=', date_start), ('data_documento', '<=', date_end), ('data_documento', '<', data_realise), ('cobrado', '=', False), ('prest_zerro', '=', False)])
            for f in prev:

                docs.append({
                    'numero_credito': f.numero_credito,
                    'codigo_terc': f.codigo_terc,
                    'nome_terceiro': f.nome_terceiro,
                    'valor_desembolso': f.valor_desembolso,
                    'valor_pago': f.prestacao,
                    'valor_atrazo': f.valor_desembolso,
                    #'indici_atraso': f.indici_atraso,
                    'valor_em_risco': f.valor_desembolso,


                })
        else:
            prev = self.env['reg.docum'].search(
                [('data_documento', '>=', date_start), ('data_documento', '<=', date_end), ('data_documento', '<', data_realise), ('cobrado', '=', False), ('prest_zerro', '=', False)])
            for f in prev:
                docs.append({
                    'numero_credito': f.numero_credito,
                    'codigo_terc': f.codigo_terc,
                    'nome_terceiro': f.nome_terceiro,
                    'valor_desembolso': f.valor_desembolso,
                    'valor_pago': f.prestacao,
                    'valor_atrazo': f.valor_desembolso,
                    #'indici_atraso': f.indici_atraso,
                    'valor_em_risco': f.valor_desembolso,


                })
        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'date_start': date_start,
            'date_end': date_end,
            'agente': agente,
            'data_realise': data_realise,
            'agrup_agente': agrup_agente,
            'docs': docs,
        }
