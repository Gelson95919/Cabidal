# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class contcore(models.Model):
     _name = 'contcore.contcore'
     _description = 'Conta Corrente'

     data_realise = fields.Date(string="Data Realizado", default=fields.Date.today)
     terceiro_id = fields.Many2one('terceiro.terceiro', string='Terceiro', domain=lambda self: [("id", "in",
                                    self.env['reg.docum'].search([('saldo', '!=', 0)],limit=900).mapped("nome_terc").ids)])

     data_inicial = fields.Date('Data Inicial')
     data_final = fields.Date(string='Data Final')
     detalhes = fields.Boolean(string='Detalhes')
     reg_docum_ids = fields.One2many('reg.docum', 'contcore_contcore_id', string="Reg Docum")

     tot_parc_credito = fields.Float('Total Credito', compute="calc_tot_parc", store=True, cope=True)
     tot_parc_debito = fields.Float('Total Debito', compute="calc_tot_parc", store=True, cope=True)
     creador = fields.Float(string="Creador", compute="calc_tot_parc")
     devedor = fields.Float(string="Devedor", compute="calc_tot_parc")
     numero = fields.Char('Numero')
     name = fields.Char(string='Nome/Razão', related="terceiro_id.name")
     street = fields.Char(related="terceiro_id.street")
     phone = fields.Integer('Telefone', related="terceiro_id.phone")
     fax = fields.Integer('Fax', related="terceiro_id.fax")
     nif = fields.Integer('NIF', related="terceiro_id.nif")

     def _comput_line(self, line):
          return {
               'displlay_type': line.displlay_type,
               'state': 'draft',
          }

     @api.multi
     @api.onchange('terceiro_id')
     def selecionar_documentos(self):
          domin = [('nome_terc', '=', self.terceiro_id.id), ('prest_zerro', '=', False)]
          docum = self.env['reg.docum'].search(domin)
          list_of_docum = []
          for line in docum:
               data = self._comput_line(line)
               data.update(
                    {'data_documento': line.data_documento, 'movimen_docum': line.movimen_docum,
                     'tipo_docum': line.tipo_docum,
                     'numeros_docum': line.numeros_docum, 'cod_documento': line.cod_documento,
                     'nome_terc': line.nome_terc, 'valorAsc': line.valorAsc,
                     'saldo_ord': line.saldo_ord, 'saldar': line.saldar,
                     'total': line.total, 'valorPago': line.valorPago, 'ldocaut': line.ldocaut,
                     'valor_ordpag': line.valor_ordpag, 'credito': line.credito, 'encontro': line.encontro,
                     'saldo': line.saldo, 'sequence': line.sequence, 'ordem_pago': line.ordem_pago,
                     'control_op': line.control_op, 'desting_doc_op': line.desting_doc_op,
                     'pago': line.pago, 'documentos': line.documentos, 'data_realise': line.data_realise,
                     'desting_doc_desp': line.desting_doc_desp, 'debito': line.debito,
                     'visualizar_no_tesorer': line.visualizar_no_tesorer, 'docPag': line.docPag,
                     'sem_cta_cte': line.sem_cta_cte})
               list_of_docum.append((1, line.id, data))

          return {'value': {"reg_docum_ids": list_of_docum}}

     @api.one
     @api.depends('tot_parc_debito', 'tot_parc_credito', 'reg_docum_ids.debito', 'reg_docum_ids.credito')
     def calc_tot_parc(self):
          self.tot_parc_debito = sum(line.debito for line in self.reg_docum_ids)
          self.tot_parc_credito = sum(line.credito for line in self.reg_docum_ids)
          self.devedor = self.tot_parc_credito - self.tot_parc_debito
          self.creador = self.tot_parc_debito - self.tot_parc_credito

     @api.model
     def create(self, vals):
         vals['numero'] = self.env['ir.sequence'].next_by_code('conta.corente.numero') or _('New')
         res = super(contcore, self).create(vals)

         return res