# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class despesa(models.Model):
    _name = 'despesa.despesa'
    _description = 'Despesas'
    _rec_name = 'fornec_tercd'
    documentos = fields.Char(string="Documento", default="Compras/Despesas")
    n_documento = fields.Char(string="Documento", store=True, copy=True,  index=True,
                          default=lambda self: self._get_next_cod())
    tipo_docum_id = fields.Many2one('documento.documento', string='Tipo Documento')
    numero_ident = fields.Integer(string='Numero/Ident')
    data_docum = fields.Date(string='Data', default=fields.Date.today)
    forma_pagamento = fields.Many2one('pagamento.pagamento', string='Forma Pagamento')
    fornec_tercd = fields.Many2one('terceiro.terceiro', string='Fornecedor/Terceiro', store=True, domain="[('fornecedores','=',True)]")
    valor_docum_esc = fields.Float(string='Montante', store=True, compute="compute_val_tot", readonly=False)
    nro_processo = fields.Many2one('processo.processo', string='Nro Processo')
    venc = fields.Date(string='Venc', default=fields.Date.today)
    desting_doc_desp = fields.Boolean(string="Documento/Despesa", default=True)
    currency_id = fields.Many2one('res.currency', string='Moeda')
    moeda_id = fields.Many2one('moeda.moeda', string='Moeda')
    valor_outra_moeda = fields.Monetary(string='Valor outra Moeda', currency_field='currency_id', )  # optional:
    val_outra_moeda = fields.Monetary(string="Valor outra moeda")
    codigo = fields.Many2one('compras.compras', string='Codigo')  # para rimover nao tem funcao
    percentagem = fields.Char(string='Percentagem')
    detalhes = fields.Text(string='Obs', store=True)
    date_release = fields.Date(string='Data Movimento', related="tipo_docum_id.date_release", store=True, readonly=True)
    diario = fields.Many2one(string='Diario', related="tipo_docum_id.diario", store=True, readonly=True)
    numero = fields.Integer(string='Numero')
    contabilizado = fields.Boolean(string='Contabilizado')
    display_type = fields.Selection([('line_section', "Section"), ('line_note', "Note")], default=False,
                                    help="Campo técnico para finalidade UX.")
    detal_ids = fields.One2many('detalhes.documento.op', 'despesa_despesa_id', string='detal')  # , index=True, store=True
    sequence = fields.Integer(widget="handle", string=" ", help="Dá a seqüência desta linha ao exibir a fatura.")
    visualizar_no_tesorer = fields.Boolean('Visualizar no Tesorer', related="tipo_docum_id.visualizar_no_tesorer",
                                           store=True)
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)
    sequence_id = fields.Many2one('ir.sequence', string='Sequência de entrada', required=False, copy=False)
    aprovado = fields.Selection([('True', 'Sim'), ('False', 'Não')], default="True")  # Controlo
    # Campos do Controlo
    type = fields.Selection(
        [('base_despachante_definitiva', 'Base Despachante Definitiva'),
         ('despachante_definitiva', 'Base Despachante Definitiva'), ('despesa', 'Despesa'),
         ('base_despesa_definitiva', 'Base Despesa Definitiva')],
        readonly=True, index=True, change_default=True, default=lambda self: self._context.get('type', 'despesa'),
        track_visibility='always')
    total = fields.Integer(string="Total", compute="compute_val_tot", copy=True, store=True, readonly=False)
    displlay_type = fields.Selection([('line_section', 'section'), ('line_note', 'nota')], string='displlay')
    state = fields.Selection([('draft', 'Draft'), ('open', 'Open'), ('paid', 'Paid'), ('cancel', 'Cancelled'), ],
                             string='Status', index=True, readonly=True, default='draft', track_visibility='onchange',
                             copy=False)
    control_estad_docum = fields.Selection(
        [('rascunho', 'Rascunho'), ('ordenado', 'Orden Pag'), ('pago', 'Pago'), ('aberto', 'Aberto'),
         ('fechado', 'Fechado')], string='Status', index=True, readonly=True, default='rascunho',
        track_visibility='onchange', copy=False, store=True)



    @api.model
    def _get_next_cod(self):
        sequence = self.env['ir.sequence'].search([('code', '=', 'despesa.despesa.n_documento')])
        next = sequence.get_next_char(sequence.number_next_actual)
        return next

    @api.model
    def create(self, vals):
        vals['control_estad_docum'] = 'ordenado'
        vals['n_documento'] = self.env['ir.sequence'].next_by_code('despesa.despesa.n_documento') or _('New')
        vals['numero'] = self.env['ir.sequence'].next_by_code('despesa.despesa.numero') or _('New')
        obg = super(despesa, self).create(vals)
        obg.create_docum()
        return obg


    @api.multi
    def write(self, vals):
        self.ensure_one()
        val = {}
        if 'tipo_docum_id' in vals: val['tipo_docum'] = vals['tipo_docum_id']
        if 'numero' in vals: val['numeros_docum'] = vals['numero']
        if 'n_documento' in vals: val['id_documento'] = vals['n_documento']
        if 'fornec_tercd' in vals: val['nome_terc'] = vals['fornec_tercd']
        if 'visualizar_no_tesorer' in vals: val['visualizar_no_tesorer'] = vals['visualizar_no_tesorer']
        if 'total' in vals: val['total'] = vals['total']
        if 'valor_docum_esc' in vals: val['valorAsc'] = vals['valor_docum_esc']
        if 'data_docum' in vals: val['data_documento'] = vals['data_docum']
        campo = self.env['reg.docum'].search([('id_documento', '=', self.n_documento)])  # primeiro registro de pesquisa
        campo.write(val)  # registro de atualização
        obg = super(despesa, self).write(vals)
        return obg


    @api.one
    @api.depends('detal_ids.valor')
    def compute_val_tot(self):
        self.total = sum(line.valor for line in self.detal_ids)
        self.valor_docum_esc = sum(line.valor for line in self.detal_ids)


    def create_docum(self):
        fat_obj = self.env['reg.docum']
        fatur = fat_obj.create({
            'tipo_docum': self.tipo_docum_id.id,
            'numeros_docum': self.numero,
            'cod_documento': self.n_documento,
            'nome_terc': self.fornec_tercd.id,
            'visualizar_no_tesorer': self.visualizar_no_tesorer,
            'total': self.total, 'aprovado': self.aprovado,
            'saldo_pagamento': self.total,
            'valorAsc': self.valor_docum_esc,
            'documentos': self.documentos,
            'desting_doc_desp': self.desting_doc_desp,
            'data_documento': self.data_docum})

        pessoa = self.env['terceiro.terceiro'].search([('id', '=', self.fornec_tercd.id)])
        for p in pessoa:
            p.tem_despesas = True

        return fatur





