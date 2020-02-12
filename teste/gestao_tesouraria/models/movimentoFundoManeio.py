# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class fundomaneio(models.Model):
     _name = 'fundomaneio.fundomaneio'
     _description = 'Movimento Fundo Maneio'
     _rec_name = 'numero'

     monetario_id = fields.Many2one('monetario.monetario', string='Fundo Maneio')
     encaregado = fields.Char(string="Encaregado", copy=True, store=True, related='monetario_id.encaregado')
     tipo_docum = fields.Char(string="Tipo Documento", default='Ordem de Pagamento')
     documentos = fields.Char(string="Documento", default="Tesouraria/Fundo Maneio")
     data_fechp = fields.Date('Data Fecho',  default=fields.Date.today)
     numero = fields.Char(string='Numero', readonly=True)
     fundo = fields.Float(string='Fundo', related='monetario_id.saldo_inicial', store=True, readonly=True)
     gasto = fields.Float(string='Gasto', compute="_compute_gasto", store=True)
     em_caixa = fields.Float(string='Em Caixa', compute="_compute_gasto", store=True)
     contabilizado = fields.Boolean(string='Contabilizado')
     diario = fields.Integer(string='Diario')
     numero_contab = fields.Integer(string='Numero')
     movimento_fundo_maneio_ids = fields.One2many('movimento.fundo.maneio', 'fundomaneio_fundomaneio_di', string='Movimento Fundo Maneio Tree', oldname='detal_line')
     cria_op = fields.Boolean(string="Criar Ordem Pagamento")
     n_documento = fields.Char(string="Numero/Abrev")
     desting_doc_tesoura = fields.Boolean(string="Documento/Tesouraria", default=True)
     sequence_id = fields.Many2one('ir.sequence', string='Sequência de entrada', required=False, copy=False)

     tot_mont = fields.Float(string='Total Montante', compute="calc_total", store=True)
     tot_iva = fields.Float(string='Total Iva', compute="calc_total", store=True)
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

     @api.one
     @api.depends('movimento_fundo_maneio_ids.montante')
     def _compute_gasto(self):
          self.gasto = sum(line.montante for line in self.movimento_fundo_maneio_ids)
          self.em_caixa = self.fundo - self.gasto

     @api.one
     @api.depends('movimento_fundo_maneio_ids.montante', 'movimento_fundo_maneio_ids.taxa')
     def calc_total(self):
         self.tot_mont = sum(line.montante for line in self.movimento_fundo_maneio_ids)
         self.tot_iva = sum(line.taxa for line in self.movimento_fundo_maneio_ids)

     @api.model
     def create(self, vals):
         vals['n_documento'] = self.env['ir.sequence'].next_by_code('mov.fund.mane.abrev') or _('New')
         vals['numero'] = self.env['ir.sequence'].next_by_code('fund.mane.num') or _('New')
         obg = super(fundomaneio, self).create(vals)
         obg.create_docum()
         return obg

     #@api.multi
     #def write(self, vals):
     #    vals['control_estad_docum'] = 'ordenado'
     #    vals['n_documento'] = self.env['ir.sequence'].next_by_code('mov.fund.mane.abrev') or _('New')
     #    vals['numero'] = self.env['ir.sequence'].next_by_code('fund.mane.num') or _('New')
     #    obg = super(fundomaneio, self).write(vals)
    #     obg.create_docum()
     #    return obg


     def create_docum(self):
         #self.docum_com_ctacte_ids.passar_para_pago()# Na despesas
         #self.write({'control_estad_docum': 'pago'})# No ordem pagamento
         if self.cria_op == True:

             fat_obj = self.env['reg.docum']
             fatur = fat_obj.create({
                    'tipo_docum': self.tipo_docum,
                    'numeros_docum': self.numero,
                    'cod_documento': self.n_documento,
                    'nome_terc': self.encaregado,
                    'total': self.gasto,
                    'valorAsc': self.gasto,
                    'documentos': self.documentos,
                    'desting_doc_desp': self.desting_doc_tesoura,
                    'data_documento': self.data_fechp,
                    #'fornec_tercd': self.encaregado

                     })

             return fatur
         else:
             pass
class movimentoFundoManeio(models.Model):
    _name = 'movimento.fundo.maneio'
    #_rec_name = 'name'
    _description = 'Movimento Fundo Maneio Tree'

    iva_id = fields.Many2one('iva.iva', string='IVA')
    taxa = fields.Float(string="Taxa", related='iva_id.taxa')
    cod_comp_id = fields.Many2one('compras.compras', string='Codigo', required=True)

    codigo_compra = fields.Char('codigo', required=True, related='cod_comp_id.codigo')
    descricao = fields.Char(string="Descrição", related='cod_comp_id.name', store=True, readonly=True)
    data = fields.Date(string='Data')
    montante = fields.Float(string='Montante')
    cod_dep = fields.Many2one('organizacao.organizacao', string='Departamento')
    fundomaneio_fundomaneio_di = fields.Many2one('fundomaneio.fundomaneio', string="Movimento Fundo Maneio")