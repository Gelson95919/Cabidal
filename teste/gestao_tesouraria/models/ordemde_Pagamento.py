# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ordempag(models.Model):
    _name = 'tesouraria.ordem.pagamento'
    _description = 'Ordem Pagamento'
    _rec_name = 'fornecedor_id'

    date_release = fields.Date('Data')
    # tem despesa falso para não filtrar nada ainda
    fornecedor_id = fields.Many2one('terceiro.terceiro', string='Fornecedor', store=True, domain="[('fornecedores','=',True)]")#
    documentos = fields.Char(string="Documento", default="Tesouraria/OP")
    fornecidor = fields.Char(string="Fornecidor", copy=True, related='fornecedor_id.name', store=True)  # Campo criado parta controlos
    sequence_id = fields.Many2one('ir.sequence', string='Sequência de entrada', copy=False)
    abrev = fields.Char(string="Abreviatura")
    desting_doc_op = fields.Boolean(string="Documento/OP", default=True)
    control_op = fields.Boolean(default=True)  # controlar os OP
    sem_cta_cte = fields.Boolean(string='Sem Cta.Cte.')
    detalhes_ordem = fields.Text(string='Detalhes', copy=True, store=True)
    numerof = fields.Char(string='Numero', store=True, copy=True, readonly=False, )  # numero com prefix
    numero = fields.Char(string='Numero', copy=True, readonly=True, default=lambda self: self._get_next_cod(), store=True)  # numero sequencial
    montante = fields.Float(string="Total", copy=True, store=True, readonly=False, compute="compute_val_tot")#,
    valor_docum_esc = fields.Float(string="Valor Asc", copy=True, store=True, compute="compute_val_tot")# ,
    tipo_docum = fields.Many2one('documento.documento', string="Tipo Documento")
    reg_docum_ids = fields.One2many('reg.docum', 'ordem_pagamento_id', string="Reg Docum", store=True, copy=True)
    displlay_type = fields.Selection([('line_section', 'section'), ('line_note', 'nota')], string='displlay')
    visualizar_no_tesorer = fields.Boolean(string="Visualizar no Tesoura", default=True)
    sem_ctacte_ids = fields.One2many('detalhes.documento.op', 'teso_ordem_pagamento_id', string='detal', oldname='sem_cta_cte')
    detalhes_ids = fields.One2many('detalhes.documento.op', 'teso_ordem_pagamento_id', string='detal')
    control_estad_docum = fields.Selection([('rascunho', 'Rascunho'), ('pago', 'Pago'), ('aberto', 'Aberto'),
                                            ('fechado', 'Fechado')], string='Status', index=True, readonly=True,
                                           default='rascunho', track_visibility='onchange', copy=False, )
    state = fields.Selection([('draft', 'Draft'), ('open', 'Open'), ('paid', 'Paid'), ('cancel', 'Cancelled'), ],
                             string='Status', index=True, readonly=True, default='draft', track_visibility='onchange',
                             copy=False)
    ata_id = fields.Integer(string="Id ata")
    op_solic = fields.Boolean(string="OP Gerado", store=True)
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)
    estado = fields.Selection([('1', 'Aberto'), ('2', 'Fechado')], default="1")
    nif_pessoa = fields.Char(string="NIF", size=9, related='fornecedor_id.nif_pessoa',)
    ata = fields.Integer(string="ID Ata")
    renegociado = fields.Boolean(string="Renegociado")
    mud_id = fields.Boolean(string="Mudar ID", default=True)

    dados_antigo = fields.Boolean(string="Dados Antigo")  # se True porque os dados são antigo


    CDOCINT = fields.Char(string="Cod Int")
    CCODTER = fields.Char(string="Cod Terc")
    CIDEDOC = fields.Char(string="Cod NUN")

    @api.one
    @api.constrains('dados_antigo')
    def val_dados_antig(self):  # Verificar se o dados e antigo ou não
        if self.dados_antigo == True:
           pass#raise ValidationError(
           #    'Dados antigo, ha algumas informações que precisam ser modificado, Contacta o adminstrador de sistema se consideraste que é um erro ')


    @api.model
    def _get_next_cod(self):
        sequence = self.env['ir.sequence'].search([('code', '=', 'tesouraria.ordem.pagamento2')])
        next = sequence.get_next_char(sequence.number_next_actual)
        return next

    @api.model
    def create(self, vals):
        vals['numerof'] = self.env['ir.sequence'].next_by_code('tesouraria.ordem.pagamento') or _('New')
        vals['numero'] = self.env['ir.sequence'].next_by_code('tesouraria.ordem.pagamento2') or _('New')
        res = super(ordempag, self).create(vals)
        # res.lig_detal_op()
        res.create_docum()
        res.reg_docum_ids.passar_para_ordenado()

        # self.create_fatur_op()
        # self.docum_com_ctacte_ids.create(vals)
        return res

    @api.multi
    def write(self, vals):
        self.ensure_one()
        val = {}
        if 'tipo_docum' in vals: val['tipo_docum'] = vals['tipo_docum']
        if 'numero' in vals: val['numeros_docum'] = vals['numero']
        if 'numerof' in vals: val['id_documento'] = vals['numerof']
        if 'fornecedor_id' in vals: val['nome_terc'] = vals['fornecedor_id']
        if 'visualizar_no_tesorer' in vals: val['visualizar_no_tesorer'] = vals['visualizar_no_tesorer']
        if 'montante' in vals: val['total'] = vals['montante']
        if 'valor_docum_esc' in vals: val['valorAsc'] = vals['valor_docum_esc']
        if 'date_release' in vals: val['data_documento'] = vals['date_release']
        campo = self.env['reg.docum'].search([('ata', '=', self.ata_id)])  # primeiro registro de pesquisa
        campo.write(val)  # registro de atualização
        obg = super(ordempag, self).write(vals)
        return obg

    #@api.one
    #@api.depends('sem_ctacte_ids.valor', 'reg_docum_ids.valor_ordpag')
    #def compute_val_tot(self):
    #    self.valor_docum_esc = sum(line.valor for line in self.sem_ctacte_ids)
    #    if self.sem_cta_cte == True:
    #        self.montante = sum(line.valor for line in self.sem_ctacte_ids)  # sem Conta corente

    #    else:
    #        self.montante = sum(line.valor_ordpag for line in self.reg_docum_ids)  # com comta corente"""

    def _comput_line(self, line):
        return {
            'displlay_type': line.displlay_type,
            'state': 'draft',
        }

    @api.one
    @api.depends('sem_ctacte_ids.valor', 'detalhes_ids.valor', 'reg_docum_ids.valor_ordpag')
    def compute_val_tot(self):
        if self.op_solic == True and self.sem_cta_cte == True:
            self.montante = sum(line.valor for line in self.detalhes_ids)
            self.valor_docum_esc = self.montante
        elif self.sem_cta_cte == True:
            self.montante = sum(line.valor for line in self.sem_ctacte_ids)
            self.valor_docum_esc = self.montante
        elif self.sem_cta_cte == False:
            self.montante = sum(line.valor_ordpag for line in self.reg_docum_ids)
            self.valor_docum_esc = self.montante

    @api.multi
    @api.onchange('fornecedor_id')
    def _onchange_reg_docum_ids(self):
        if self.sem_cta_cte == True:
            pass

        else:
            docum = self.env['reg.docum'].search([('nome_terc', '=', self.fornecedor_id.id),  # ('saldo', '!=', 0),
                                                  ('ordem_pago', '=', False), ('desting_doc_desp', '=', True),
                                                  ('pago', '=', False),  ('pagado_completo', '=', False),
                                                  ('encont_docum_desp', '=', False)])  # ('saldo_ord', '!=', 0),
            list_of_docum = []
            for line in docum:
                data = self._comput_line(line)
                data.update(
                    {'data_documento': line.data_documento, 'movimen_docum': line.movimen_docum,
                     'tipo_docum': line.tipo_docum, 'saldo_ord': line.saldo_ord, 'valor_ordpag': line.valor_ordpag,
                     'documentos': line.documentos, 'saldar': line.saldar, 'debito': line.debito,
                     'valor_encontro': line.valor_encontro, 'valorreceb': line.valorreceb,
                     'encont_docum_desp': line.encont_docum_desp, 'encont_docum_client': line.encont_docum_client,
                     'numeros_docum': line.numeros_docum, 'cod_documento': line.cod_documento, 'pago': line.pago,
                     'data_realise': line.data_realise, 'credito': line.credito, 'encontro': line.encontro,
                     'nome_terc': line.nome_terc, 'valorAsc': line.valorAsc,
                     'total': line.total, 'valorPago': line.valorPago, 'ldocaut': line.ldocaut,
                     'saldo': line.saldo, 'sequence': line.sequence, 'ordem_pago': line.ordem_pago,
                     'visualizar_no_tesorer': line.visualizar_no_tesorer, 'docPag': line.docPag})
                list_of_docum.append((1, line.id, data))

            return {'value': {"reg_docum_ids": list_of_docum}}

    @api.multi
    def gerar_ord_pg(self, vals):
        # self.docum_com_ctacte_ids.control == False
        self.docum_com_ctacte_ids.passar_para_pago()
        # self.docum_com_ctacte_ids.write(vals)

   

    def create_docum(self):
        if self.op_solic == False:
            if self.sem_cta_cte == False:#como ordem ja esta feito, vai marcar esses documento ordenado com pago
                docum = self.env['reg.docum'].search([('nome_terc', '=', self.fornecedor_id.id),
                                                      ('pagado_completo', '=', False), ('renegociado', '=', False), ('encont_docum_desp', '=', False)])  # ('saldo_ord', '!=', 0),
                for rec in docum:
                    rec.pagado_completo = True
            fat_obj = self.env['reg.docum']
            fatur = fat_obj.create({
                'tipo_docum': self.tipo_docum,
                'numeros_docum': self.numero,
                'cod_documento': self.numerof,
                'nome_terc': self.fornecedor_id.id,
                'visualizar_no_tesorer': self.visualizar_no_tesorer,
                'total': self.montante,
                'valorAsc': self.valor_docum_esc,
                'documentos': self.documentos,
                'saldo_pagamento': self.montante,
                'control_op': self.control_op,
                'data_documento': self.date_release,
                'desting_doc_op': self.desting_doc_op,
                'receb_solici': self.op_solic,
                'desting_doc_desp': self.desting_doc_op,
            })

            pessoa = self.env['terceiro.terceiro'].search([('id', '=', self.fornecedor_id.id)])
            for rec in pessoa:
                rec.tem_despesas = True
            return fatur



    @api.one
    def lig_detal_op(self):
        self.ensure_one()
        if self.op_solic == True:
            det_op = self.env['detalhes.documento.op'].search([('ata_id', '=', self.ata_id)])
            det_op.ordem_pagamento_id = self.ids


    @api.one
    def fechar(self):
        # if self.pago == True:
        # vals['control_estad_docum'] = 'fechado'
        self.write({'control_estad_docum': 'fechado'})
        # else:
        # pass #raise ValidationError('AS FACTURAS PENDESTES NÃO DEVE SER FECHADO!')
        # return super(ordempag, self).write(vals)

    @api.one
    def abrir(self):
        self.write({'control_estad_docum': 'aberto'})


