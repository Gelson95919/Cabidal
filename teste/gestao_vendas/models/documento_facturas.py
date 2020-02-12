# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class documentoFatuclient(models.Model):
    _name = 'fatuclient.fatuclient'

    _description = 'Documento Factura'
    _rec_name = 'tipo_docum_id'

    tipo_docum_id = fields.Many2one('documento.documento', string='Tipo Documento')

    # _order = 'sequence,name'
    armazem_id = fields.Many2one('armanzem.armanzem', string='Armanzem')
    dataf = fields.Date(string="Data", default=fields.Date.today)
    nmuero_prefix = fields.Char(string="Documento", readonly=True)
    nmuero = fields.Char(string="Documento", readonly=True)

    # cliente
    terceiro_id = fields.Many2one('terceiro.terceiro', string='Nome', domain="[('tipo','=','terceiro')]", required=True)
    cliente = fields.Char(string="Fornecidor", copy=True, store=True,
                          related="terceiro_id.name", )  # Manda dados para reg
    documentos = fields.Char(string="Documento", default="Vendas/FAturas")

    nif = fields.Integer(string='NIF', readonly=True, related="terceiro_id.nif", store=True)#para remover
    nif_pessoa = fields.Char(string="NIF", required=True, size=9, related="terceiro_id.nif_pessoa")

    street2 = fields.Char(string='Endereço', readonly=True, related="terceiro_id.street2", store=True)
    tip_paga_id = fields.Many2one('pagamento.pagamento', string='Forma')
    moeda_id = fields.Many2one('moeda.moeda', string='Moeda')
    date = fields.Date(string='Data Fatura', default=fields.Date.today)

    fatuclient_id = fields.Many2one('moeda.moeda')  # ao criar um novo base de dados eliminar este campo
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

    # aba_observacao
    artigoob_id = fields.Many2one('artigo.artigo', string='Artigo')
    ivamo_id = fields.Many2one('iva.iva', string='IVA')
    aredondamento = fields.Boolean(string='Aredondamento')
    obs = fields.Text(string='OBS')
    montante = fields.Float(string='Montante')
    # aba contabilidade
    contabiliza = fields.Boolean(string='Contabilizado')
    diario = fields.Integer(string='Diario')
    numerofact = fields.Integer(string='Numero')
    # Resumo
    iva_resumo_di = fields.Float(string='IVA')
    desconto_resumo = fields.Float(string='Desconto')
    total_resumo = fields.Float(string='Montante', compute="_compute_amount", store=True, readonly=False)
    fatura_linha_ids = fields.One2many('detalhes.line', 'fatuclient_id', string='Detalhes', copy=True)
    sequence = fields.Integer(widget="handle", help="Dá a seqüência desta linha ao exibir a fatura.")
    # ------

    displlay_type = fields.Selection([('line_section', 'section'), ('line_note', 'nota')], string='displlay')
    state = fields.Selection([('draft', 'Draft'), ('open', 'Open'), ('paid', 'Paid'), ('cancel', 'Cancelled'), ],
                             string='Status', index=True, readonly=True, default='draft', track_visibility='onchange',
                             copy=False)
    type_fat = fields.Selection(
        [('fatur_cliente', 'Fatura Cliente'), ('nota_debito', 'Nota Debito'), ('nota_credito', 'Nota Credito')],
        readonly=True, index=True, change_default=True, default=lambda self: self._context.get('type', 'fatur_cliente'),
        track_visibility='always')
    visualizar_no_tesorer = fields.Boolean('Visualizar no Tesorer', related="tipo_docum_id.visualizar_no_tesorer",
                                           store=True)
    # consulta_conta_corrente_id = fields.Many2one('consulta.conta.corrente', ondele='cascade', index=True)
    desting_doc_vend = fields.Boolean(string="Documento/Venda", default=True)
    control_estad_docum = fields.Selection([('rascunho', 'Rascunho'), ('aberto', 'Aberto'), ('fechado', 'Fechado')],
                                           string='Status', index=True, readonly=True, default='rascunho',
                                           track_visibility='onchange', copy=False, )

    saldo = fields.Float(string="Saldo", compute="_compute_saldo", store=True)  # pára remover
    pago = fields.Float(string="Saldo", compute="_compute_saldo", store=True)  # para remover
    aprovado = fields.Selection([('True', 'Sim'), ('False', 'Não')], default="True")#Controlo de
    # _sql_constraints = [
    #    ('unique_code', 'unique(numero)', 'Number of numero recibo must be unique!')
    # ]


    @api.one
    @api.depends('fatura_linha_ids.sub_total', 'fatura_linha_ids.amount_rounding', 'fatura_linha_ids.taxa')
    def _compute_amount(self):

        self.amount_untaxed = sum(line.sub_total for line in self.fatura_linha_ids)
        self.tax = sum(line.taxa for line in self.fatura_linha_ids)
        self.pu = sum(line.preco_unitario for line in self.fatura_linha_ids)
        self.iva = (self.tax / 100) * self.pu

        if self.iva > 0.00:
            self.total_resumo = self.amount_untaxed + self.iva
        else:
            self.total_resumo = self.amount_untaxed

    @api.model
    def create(self, vals):
        vals['control_estad_docum'] = 'aberto'
        vals['nmuero_prefix'] = self.env['ir.sequence'].next_by_code('fatuclient.fatuclient') or _('New')
        vals['nmuero'] = self.env['ir.sequence'].next_by_code('fatuclient.fatuclient.num') or _('New')
        res = super(documentoFatuclient, self).create(vals)
        res.create_docum()
        #res.tem_documento()
        return res

    @api.multi
    def write(self, vals):
        self.ensure_one()
        val = {}
        if 'tipo_docum_id' in vals: val['tipo_docum'] = vals['tipo_docum_id']
        if 'nmuero' in vals: val['numeros_docum'] = vals['nmuero']
        if 'nmuero_prefix' in vals: val['id_documento'] = vals['nmuero_prefix']
        if 'terceiro_id' in vals: val['nome_terc'] = vals['terceiro_id']
        if 'visualizar_no_tesorer' in vals: val['visualizar_no_tesorer'] = vals['visualizar_no_tesorer']
        if 'total_resumo' in vals: val['total'] = vals['total_resumo']
        if 'total_resumo' in vals: val['valorAsc'] = vals['total_resumo']
        if 'date' in vals: val['data_documento'] = vals['date']
        campo = self.env['reg.docum'].search([('id_documento', '=', self.nmuero_prefix)])  # primeiro registro de pesquisa
        campo.write(val)  #registro de atualização
        obg = super(documentoFatuclient, self).write(vals)
        return obg

    def create_docum(self):
        fat_obj = self.env['reg.docum']
        fatur = fat_obj.create({'tipo_docum': self.tipo_docum_id.id, 'numeros_docum': self.nmuero,
                                'cod_documento': self.nmuero_prefix, 'nome_terc': self.terceiro_id.id,
                                'visualizar_no_tesorer': self.visualizar_no_tesorer,'saldo': self.total_resumo,
                                'total': self.total_resumo, 'valorAsc': self.total_resumo,
                                'documentos': self.documentos, 'desting_doc_vend': self.desting_doc_vend,
                                'data_documento': self.date, 'aprovado': self.aprovado, })
        pessoa = self.env['terceiro.terceiro'].search([('nif_pessoa', '=', self.nif_pessoa)])
        for p in pessoa:
            p.tem_fatur = True
            p.write({'tem_solicitacao': '1'})
        return fatur



class detalhes(models.Model):
    _name = "detalhes.line"
    _description = "Detalhes Line"
    _order = "fatuclient_id,id"

    @api.one
    @api.depends('preco_unitario', 'discount', 'quantidade', 'taxa')
    def calc_preco(self):
        for line in self:
            line.sub_total = line.preco_unitario * (1.0 - line.discount / 100.0) * line.quantidade

    artigo_id = fields.Many2one('artigo.artigo', string='Descrição')
    preco_unitario = fields.Float(string='Preço Unitario')
    quantidade = fields.Float(string='Quantidade')
    descon = fields.Float(satring='Desconto')
    iva = fields.Many2one('iva.iva', string='IVA (%)', readonly=True, related="artigo_id.iva_id", store=True)
    sub_total = fields.Float(string='Sub-Total', store=True, readonly=True, compute='calc_preco')

    # Relacionamento
    planconta_id = fields.Many2one('planconta.planconta', string='Conta')
    moeda_id = fields.Many2one('moeda.moeda', string='Moeda', related='fatuclient_id.moeda_id', store=True,
                               related_sudo=False)
    terceiro_id = fields.Many2one('terceiro.terceiro', string='Nome', related='fatuclient_id.terceiro_id', store=True,
                                  readonly=True, related_sudo=False)
    fatuclient_id = fields.Many2one('fatuclient.fatuclient', string='Referência fatura', ondelete='cascade', index=True)

    # Para calcular valor de Sub-Total Preciso de:
    discount = fields.Float(string='Desconto (%)', default=0.0)

    # invoice_line_tax_ids = fields.Many2many('account.tax', 'account_invoice_line_tax', 'invoice_line_id', 'tax_id', string='Taxes', domain=[('type_tax_use', '!=', 'none'), '|', ('active', '=', False), ('active', '=', True)], oldname='invoice_line_tax_id')

    fatuclient_line_iva_ids = fields.Many2many('iva.iva', 'conta_fatuclient_line_tax', 'fatuclient_line_id', 'iva_id',
                                               string='IVA')

    price_subtotal_signed = fields.Float(string='Quantidade assinada', store=True, readonly=True,
                                         compute='_compute_price',
                                         help="Valor total na moeda da empresa, negativo para nota de crédito.")

    price_total = fields.Float(string='Montante', store=True, readonly=True, compute='_compute_price',
                               help="Montante total com impostos")

    sequence = fields.Integer(default=10, help="Dá a seqüência desta linha ao exibir a fatura.")

    taxa = fields.Float(related='artigo_id.taxa')
    note = fields.Text('Terms and conditions')
    name1 = fields.Text('Description', translate=True)
    name2 = fields.Text('Description', translate=True)
    display_type = fields.Selection([('line_section', "Section"), ('line_note', "Note")], default=False,
                                    help="Technical field for UX purpose.")

    amount = fields.Float()
    amount_rounding = fields.Float()

    detalhes_id = fields.Many2one('detalhes.line', track_visibility='always')

    @api.onchange('artigo_id')
    def _onchange_artigo_id(self):
        domain = {}
        if not self.fatuclient_id:
            return

        part = self.fatuclient_id.terceiro_id

        if not part:
            warning = {
                'title': _('Warning!'),
                'message': _('Você deve primeiro selecionar um Cliente!'),
            }
            return {'warning': warning}
