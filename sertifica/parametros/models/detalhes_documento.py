# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class semContaCorente(models.Model):
    # _name = 'sem.ctacte'
    _name = "detalhes.documento.op"
    # _rec_name = 'name'
    _description = 'Detalhes Documento'

    codigo_id = fields.Many2one('compras.compras', string='Codigo Compra')
    descrecao = fields.Char(string='Descrição/Conceito/Compras', store=True)
    descrecao_desp = fields.Char(string='Descrição', related='codigo_id.name', store=True)
    codigo_dep = fields.Many2one('organizacao.organizacao', string='Departamento/Area')
    valor = fields.Float(string='Valor')
    iva_id = fields.Many2one('iva.iva', string='IVA')
    leva_terce = fields.Boolean(string='Leva Terceiro', related='codigo_id.leva_terce', store=True)
    terceiro_id = fields.Many2one('terceiro.terceiro', string='id Terceiro')
    codigo_cliente = fields.Char(string="Codico Terceiro")
    valor_auxiliar = fields.Float(string='Valor Auxiliar')
    ata_id = fields.Integer(string="Id ata")
    desting_doc_op = fields.Boolean(string="Documento/OP", default=True)
    sequence = fields.Integer(widget="handle", string=" ", help="Dá a seqüência desta linha ao exibir a fatura.")
    teso_ordem_pagamento_id = fields.Many2one('tesouraria.ordem.pagamento', string="Ordem de Pagamento")
    despesa_despesa_id = fields.Many2one('despesa.despesa', string="Despesa")
    control_IVA = fields.Boolean(string="Control de Iva", related='codigo_id.control_IVA', store=True)
    ata = fields.Integer(string="ID Ata")
    renegociado = fields.Boolean(string="Renegociado")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)
    mud_id = fields.Boolean(string="Mudar ID", default=True)
    CDOCINT = fields.Char()


    #Substetui cod compra
    def compor_op(self):
          plano = self.env['tesouraria.ordem.pagamento'].search([('mud_id', '=', True)])
          for c in plano:
               codcon = self.env['detalhes.documento.op'].search([('CDOCINT', '=', c.CDOCINT)])
               for o in codcon:
                   o.teso_ordem_pagamento_id = c.id