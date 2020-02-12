# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class reembolsoRecebido(models.TransientModel):
     _name = 'reembolso.recebido'
     _description = 'Listagem Reembolso Recebido'

     date_start = fields.Date('De')
     date_end = fields.Date('Ate')
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

          return self.env.ref('gestao_relatorio.reembolso_recebido_report').report_action(self, data=data)


class reembRec(models.AbstractModel):
    """Modelo abstrato para o modelo de relatório.

    Para `_name` model, Por favor, use `report.` como prefixo, em seguida, adicione `module_name.report_name`.
    """

    _name = 'report.gestao_relatorio.listagem_reembolso_recebido_report_view'

    @api.model
    def _get_report_values(self, docids, data=None):
        date_start = data['form']['date_start']
        date_end = data['form']['date_end']
        agente = data['form']['agente']
        agrup_agente = data['form']['agrup_agente']



        docs = []
        if agrup_agente == True:
            prev = self.env['reg.docum'].search([('cobrado', '=', True), ('prest_zerro', '=', False), ('agente', '=', agente), ('data_documento', '>=', date_start)])
            for f in prev:

                docs.append({
                    'data_realise': f.data_realise,
                    'codigo': f.codigo, #numero de recibo
                    'nome_terceiro': f.nome_terceiro,
                    'cod_documento': f.cod_documento,
                    'data_documento': f.data_documento,
                    'valor_desembolso': f.valor_desembolso,
                    'capital': f.amortizacao,
                    'juro_jerado': f.juro_jerado,
                    #'obs': f.obs,


                })
        else:
            prev = self.env['reg.docum'].search(
                [('cobrado', '=', True), ('prest_zerro', '=', False), ('data_documento', '>=', date_start)])
            for f in prev:
                docs.append({
                    'data_realise': f.data_realise,
                    'codigo': f.codigo, #numero de recibo
                    'nome_terceiro': f.nome_terceiro,
                    'cod_documento': f.cod_documento,
                    'data_documento': f.data_documento,
                    'valor_desembolso': f.valor_desembolso,
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
