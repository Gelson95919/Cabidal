# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class litrecib(models.TransientModel):
     _name = 'litrecib.litrecib'
     _description = 'Listagem de Registro recebimento'
     ano = fields.Integer('Ano')
     em_branco = fields.Boolean('Em Branco')
     mes = fields.Selection(
          [('Janeiro', 'Janeiro'),
           ('Fevereiro', 'Fevereiro'),
           ('Março', 'Março'),
           ('Abril', 'Abril'),
           ('Maio', 'Maio'),
           ('Junho', 'Junho'),
           ('Jlho', 'Jlho'),
           ('Agosto', 'Agosto'),
           ('Setembro', 'Setembro'),
           ('Outubro', 'Outubro'),
           ('Novembro', 'Novembro'),
           ('Dezembro', 'Dezembro')],
          'Mês', default='Janeiro')
     tipo = fields.Selection(
          [('Listagtem de Recibo', 'Listagtem de Recibo'),
           ('Listagem de Imposto Selo', 'Listagem de Imposto Selo'),
           ('Modelo GP 010', 'Modelo GP 010')],
          'Tipo Movimento', Widget="radio", default='Listagtem de Recibo')

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

         return self.env.ref('gestao_tesouraria.listagem_recebimentom_report').report_action(self, data=data)


class ListRecebiment(models.AbstractModel):
    """Modelo abstrato para o modelo de relatório.

    Para `_name` model, Por favor, use `report.` como prefixo, em seguida, adicione `module_name.report_name`.
    """

    _name = 'report.gestao_tesouraria.listagem_recebimento_report_view'

    @api.model
    def _get_report_values(self, docids, data=None):
        date_start = data['form']['date_start']
        date_end = data['form']['date_end']

        docs = []
        list_recb = self.env['pagamento.recebimento'].search(
            [('date', '>=', date_start), ('date', '<=', date_end), ('type_docum', '=', 'recebimento')], order='name asc')
        for l in list_recb:
            docs.append({
                'n_recibo': l.n_recibo,
                'date': l.date,
                'nome_cliente': l.nome_cliente,
                'vervalor_total_receb': l.montante_receb,
                'detalhes': l.detalhes,

            })

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'date_start': date_start,
            'date_end': date_end,
            'docs': docs,
        }

