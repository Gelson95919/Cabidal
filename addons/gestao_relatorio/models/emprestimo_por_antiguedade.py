# -*- coding: utf-8 -*-

from odoo import api, fields, models


class emprestAntig(models.TransientModel):
    _name = 'emprest.antiguidade'
    _description = 'Emprestimo por Antiguidade'

    date = fields.Date('Data')
    todos = fields.Boolean(string="Todos")
    so_val_atraso = fields.Boolean(string="Só com valor atrasado")
    agrup_por_agente = fields.Boolean(string="Agrupar por Agente")
    agente_id = fields.Many2one('res.users', string="Agente")


    @api.multi
    def get_report(self):
        """Ligue quando o botão "Get Report" for clicado.
        """
        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'date': self.date,
                'todos': self.todos,
                'so_val_atraso': self.so_val_atraso,
                'agrup_por_agente': self.agrup_por_agente,
                'agente_id': self.agente_id.id,

            },
        }

        return self.env.ref('gestao_relatorio.emprestimo_antiguidade_report').report_action(self, data=data)


class emprAnt(models.AbstractModel):
    """Modelo abstrato para o modelo de relatório.

    Para `_name` model, Por favor, use `report.` como prefixo, em seguida, adicione `module_name.report_name`.
    """

    _name = 'report.gestao_relatorio.listagem_empres_antiguidade_report_view'

    @api.model
    def _get_report_values(self, docids, data=None):
        date = data['form']['date']
        todos = data['form']['todos']
        so_val_atraso = data['form']['so_val_atraso']
        agrup_por_agente = data['form']['agrup_por_agente']
        agente_id = data['form']['agente_id']


        docs = []
        prev = self.env['reg.docum'].search([])
        for f in prev:
            docs.append({
                'numero_credito': f.numero_credito,
                'codigo_terc': f.codigo_terc,
                'nome_terceiro': f.nome_terceiro,
                'valor_desembolso': f.valor_desembolso,
                'valor_pago': f.prestacao,
                'valor_atrazo': f.valor_desembolso,
                # 'indici_atraso': f.indici_atraso,
                'valor_em_risco': f.valor_desembolso,

            })

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'date': date,
            'todos': todos,
            'so_val_atraso': so_val_atraso,
            'agrup_por_agente': agrup_por_agente,
            'agente_id': agente_id,
            'docs': docs,

        }
