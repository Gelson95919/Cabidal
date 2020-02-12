# -*- coding: utf-8 -*-


from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

class regDocum(models.Model):
    _name = 'reg.docum'
    _description = "REG DOCUM" #ANTIGO CTA CTE
    _rec_name = 'fornec_tercd'
    _order = 'CDOCINT2'
    documentos = fields.Char(string="Documento")
    #pagamento_id = fields.Many2one('tesopagame.tesopagame', index=True)  # chavi de tesouraria pagamento
    ordem_pagamento_id = fields.Many2one('tesouraria.ordem.pagamento', index=True)  # chavi de tesouraria ordem pagamento
    tesouraria_recebimento_id = fields.Many2one('tesouraria.recebimento', index=True)  # chavi de tesouraria recebimento
    encontro_conta_id = fields.Many2one('econtroconta.econtroconta', index=True)  # chavi de tesouraria encontro de conta
    contcore_contcore_id = fields.Many2one('contcore.contcore', index=True)
    pagamento_recebimento_id = fields.Many2one('pagamento.recebimento')# chavi de tesourariapagamento_recebimento
    pagamento_id = fields.Many2one('tesouraria.pagamento', string="Pagamento")  # chavi de tesouraria pagamento
    recebimento_id = fields.Many2one('tesouraria.recebimento', string="Recebimento")
    id_cred_aprov = fields.Many2one('credito.aprovado', index=True)# chavi de microcredito aprovado
    ata_id = fields.Many2one('acta.comite')  #A chavi para captar relatorios

    codigo = fields.Char(string="Documento", store=True, copy=True, index=True,)#default=lambda self: self._get_next_cod()
    sequence = fields.Integer(string="")
    data_realise = fields.Date(string="Data Realizado",)# default=fields.Date.today
    data_documento = fields.Date(string="Data/Docum", store=True)
    movimen_docum = fields.Char(string="Movimento Docum")
    tipo_docum = fields.Many2one('documento.documento', string="Tipo Docum")
    numeros_docum = fields.Char(string="Numero/Docum")
    cod_documento = fields.Char(string="Documento", strore=True)  # numero de documento com abreviatura
    #terc_id = fields.Char(string="Cod Terc")
    nome_terc = fields.Many2one('terceiro.terceiro', string="Fornecedor/Terceiro", store=True)
    nif = fields.Integer(string="Nif", related="nome_terc.nif")#para remover
    nif_pessoa = fields.Char(string="NIF", related="nome_terc.nif_pessoa")

    codigo_terc = fields.Char(string="Código", copy=False, readonly=True, related="nome_terc.codigo")
    nome_terceiro = fields.Char(string="Nome Terc", copy=False, readonly=True,  related="nome_terc.name")# related="nome_terc.name"

    visualizar_no_tesorer = fields.Boolean('Visualizar Tesorer', store=True)
    valorAsc = fields.Float(string="Valor Doc Desp")  # NNETDOC
    total = fields.Float(string="Montante")  # NTOTDOC
    valorPago = fields.Float(string="A Pagar", force_save="1")  # NVALPAG
    valorreceb = fields.Float(string="A Cobrar")  # NVALPAG
    ldocaut = fields.Boolean(default=True)
    docPag = fields.Boolean(string="Pagar", store=True)
    pago = fields.Boolean(string="Pago", store=True)  # para docmento e de despesa e OP
    cobrado = fields.Boolean(string="Recebido", store=True)  # para docmentoe de venda

    desting_doc_desp = fields.Boolean(string="Documento/Desp")
    desting_doc_vend = fields.Boolean(string="Documento/Venda")
    desting_doc_op = fields.Boolean(string="Documento/OP")
    receb_solici = fields.Boolean(string="Receb Solicitação") #quando eesta preparado para recber solic fica true


    saldo = fields.Float(string="Saldo", store=True, copy=True)  # de recebimento
    saldo_pagamento = fields.Float(string="Saldo", store=True, copy=True)  # de pagamento

    saldo_ord = fields.Float(string="Saldo", store=True, compute="_compute_saldo_ord",)  # na ordem de pagamento
    fornec_tercd = fields.Many2one('terceiro.terceiro', string='Fornecedor/Terceiro', store=True)
    ordem_pago = fields.Boolean(string='Odenar', copy=True, store=True)  # ordenar documento
    sem_cta_cte = fields.Boolean(string='Sem Cta.Cte.')
    control_op = fields.Boolean(string="Control")  # controlar os OP
    displlay_type = fields.Selection([('line_section', 'section'), ('line_note', 'nota')], string='displlay')
    state = fields.Selection([('draft', 'Draft'), ('open', 'Open'), ('paid', 'Paid'), ('cancel', 'Cancelled'), ],
                             string='Status', index=True, readonly=True, default='draft', track_visibility='onchange',
                             copy=False)
    control_estad_docum = fields.Selection(
        [('rascunho', 'Rascunho'), ('ordenado', 'Orden Pag'), ('pago', 'Pago'), ('aberto', 'Aberto'),
         ('fechado', 'Fechado')], string='Estado de Documento', index=True, readonly=True, default='rascunho',
        track_visibility='onchange', copy=False, store=True)

    # campos presentes no encontro de conta
    debito = fields.Float(string="Debito", copy=True, store=True, compute="add_valor_debt_credt")#
    credito = fields.Float(string="Credito", copy=True, store=True, compute="add_valor_debt_credt")#
    encontro = fields.Boolean(string="Encontro", store=True)  # Selecionar documentos para encotro
    saldar = fields.Float(string="Saldar")

    encont_docum_desp = fields.Boolean(string="Encontro docum") #controla os documentos despesa no encontro conta
    encont_docum_client = fields.Boolean(string="Encontro docum") #controla os documentos Cliente no encontro conta
    valor_encontro = fields.Float(string="Valor Encontro", store=True, copy=True)#valor do encontro quando cred e > deb
    valor_ordpag = fields.Float(string="A pagar")  # controla os valores de ordem pag

    #campos plano desembolso
    anulado = fields.Boolean(string="Anulado")
    pedido_id = fields.Many2one('solicitacao.credito', string="Pedido", )
    desting_ata = fields.Boolean(string="Acta", store=True)
    desting_solict = fields.Boolean(string="Solicitação")
    aprovado = fields.Selection([('True', 'Sim'), ('False', 'Não')])
    numero_credito = fields.Char(string="Numero Credito")
    #data = fields.Date(string="Data", default=fields.Date.today)
    prestacao = fields.Float(string="Prestação")
    juro_jerado = fields.Float(string="Juros")
    amortizacao = fields.Float(string="Amortização")
    divida = fields.Float(string="Divida", store=True)
    valor_desembolso = fields.Float(string="Valor Desembolso", store=True)
    #divid = fields.Float(string="Divida", store=True, compute='calcul_div')
    numer_prest = fields.Integer(string="Nº")
    plano_desembolso_id = fields.Many2one('plano.desembolso')
    submeter = fields.Boolean(string="Submeter")
    prest_zerro = fields.Boolean(string="Submeter")
    agente = fields.Many2one('res.users', tring="Agente")
    plande = fields.Boolean(string="Plano Desembolso")
    ata = fields.Integer(string="ID Ata")
    renegociado = fields.Boolean(string="Renegociado")

    recebido_completo = fields.Boolean(string="Recebido Completo", store=True, copy=True)
    aval_det_docum = fields.Boolean(string="aval det doc na tesoura",  store=True, copy=True, compute="_verif_valor_receber",)  # saldo para ser recebido
    pagado_completo = fields.Boolean(string="Pagado Completo", store=True, copy=True, compute="compute_saldo")#
    valor_saldo = fields.Float(string="Valor saldo Calculado", store=True, copy=True)  # saldo para ser recebido
    estado = fields.Selection([('1', 'Pendente'), ('2', 'Em Andamento'), ('3', 'Fechado')], default='1')
    fechado = fields.Boolean(string="Fechado", default=False)#Este campo so passa ser Verdadeiro quando todu documento do referido cliente ja se encontra recebido
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)
    origem = fields.Boolean(string="Origem da contabilidade",  store=True)
    dados_antigo = fields.Boolean(string="Dados Antigo")  #se True porque os dados são antigo

    CDOCINT = fields.Char()
    CDOCINT2 = fields.Integer()
    CCODTER = fields.Char()
    CDESCRI = fields.Char()
    CMOVINT = fields.Char()
    CNOMTER = fields.Char()
    DFECVEN = fields.Char('Data')
    DFECDOC = fields.Char('Data')
    MOBS = fields.Char()
    CCODCRED = fields.Char()
    CMOVDOC = fields.Char()
    CTIPDOC = fields.Char()
    ctip = fields.Char()
    cmovdoc = fields.Char()
    cdocint_rel = fields.Char()
    cdocint_rel_ass = fields.Integer()


    def assoc__cres(self):#ligar credito com reg_docum
        #pass

        #reg_doc = self.env['reg.docum'].search([('CMOVDOC', '=', 'E'), ('pagado_completo', '=', False)])
        #for o in reg_doc:
        #    o.desting_doc_desp = True
        #    o.encont_docum_desp = False
        #    o.renegociado = False


        reg_doc = self.env['reg.docum'].search([('CMOVDOC', '=', 'I'), ('cobrado', '=', True)])
        for o in reg_doc:

            o.desting_doc_vend = True
        #    o.encont_docum_client = False
        #    o.renegociado = False
        #    o.recebido_completo = False
        #    o.aprovado = 'True'
            #pass
        #terc = self.env['terceiro.terceiro'].search([('clientes', '=', True)])
        #for c in terc:


             #o.desting_doc_desp = True
             #o.encont_docum_desp = False
             #o.renegociado = False

    #ct = self.env['reg.docum'].search([('importado', '=', True), ('CMOVDOC', '=', 'I')])
        #for c in ct:
        #  cod = str(c.CDOCINT)
        #  if cod.isnumeric() == True:
        #     c.CDOCINT2 = c.CDOCINT


        #cred = self.env['credito.aprovado'].search([('vd', '=', '1')])
        #for c in cred:
        #    docum = self.env['reg.docum'].search([('CCODCRED', '=', c.IDCREDITO)])
        #    for d in docum:
        #        #cod = str(d.id_cred_aprov)
        #        #if cod.isnumeric() == False:
        #            d.id_cred_aprov = c.id

    def assoc_op(self):
        #pass
        #terc = self.env['credito.aprovado'].search([('vd', '=', '1')])
        #for c in terc:
        #    cod = str(c.DOCUMOP)
        #    if cod.isnumeric() == True:
        #       c.cod_op = c.DOCUMOP
        docum = self.env['reg.docum'].search([('id', '>=', 1)])
        for d in docum:
            cod = str(d.CDOCINT)
            if cod.isnumeric() == True:
                d.cdocint_rel_ass = d.CDOCINT2

        #for r in recb:
        #    docum = self.env['reg.docum'].search([('CMOVINT', '=', r.CMOVINT)])
        #    for d in docum:
        #        cod = str(d.recebimento_id)
        #        if cod.isnumeric() == False:
        #            d.recebimento_id = r.id



    # reserva os dados
    @api.model
    def _get_fatura_price(self, data_documento, movimen_docum, valor_encontro,valorreceb,
                          tipo_docum, sequence, desting_doc_vend, desting_doc_op, encont_docum_desp, encont_docum_client,
                          numeros_docum, cod_documento, pago, documentos, data_realise, desting_doc_desp, cobrado,
                          nome_terc, valorAsc, total, control_op, saldo_ord, valor_ordpag, debito, valor_saldo,
                          valorPago, ldocaut, visualizar_no_tesorer, docPag, saldo, ordem_pago, sem_cta_cte):
        return {}

    @api.model
    def _get_next_cod(self):
        sequence = self.env['ir.sequence'].search([('code', '=', 'codigo.codigo')])
        next = sequence.get_next_char(sequence.number_next_actual)
        return next

    @api.model
    def create(self, vals):
        for rec in self:
            docs = rec.env['reg.docum'].search([('receb_solici', '=', True)])
            if docs:
                 vals['cod_documento'] = self.env['ir.sequence'].next_by_code('codigo.codigo') or _('New')
        vals['codigo'] = self.env['ir.sequence'].next_by_code('codigo.codigo') or _('New')
        res = super(regDocum, self).create(vals)
        #res.add_valor_debt_credt()
        return res


    """@api.model
    def write(self, vals):
        res = super(regDocum, self).create(vals)
        res.add_valor_debt_credt()
        return res"""



    #Calculo do campo saldo por recebimento (Parcelar)"
    @api.one
    @api.constrains('valor_encontro', 'valorreceb')
    def receb_compute_saldo(self): # Calcula saldo que esta ser recebido
           if self.valor_encontro:
               self.saldo = self.valor_encontro
           else:
               if self.cobrado == False:
                  pass#self.saldo = self.total
               else:
                   if self.valorreceb:
                       if self.saldo == self.total:
                           self.saldo = self.total - self.valorreceb
                       else:
                           self.saldo -= self.valorreceb


           #Calculo do campo saldo por recebimento (Parcelar)"

    @api.one
    @api.constrains('valor_encontro', 'valorPago')
    def compute_saldo_pag(self): #Calcula saldo que esta ser pagar
        if self.valor_encontro:
            self.saldo_pagamento = self.valor_encontro
        else:
            if self.docPag == False:
                pass# self.pagado_completo = self.total
            else:
                if self.valorPago:
                    if self.saldo_pagamento == self.total:
                        self.saldo_pagamento = self.total - self.valorPago
                        if self.saldo_pagamento == 0:
                            self.pagado_completo = True

                    else:
                        self.saldo_pagamento -= self.valorPago
                        if self.saldo_pagamento == 0:
                            self.pagado_completo = True

    # Calculo do campo saldo por ord
    @api.one
    @api.depends('total', 'valor_ordpag')
    def _compute_saldo_ord(self):
        if self.valor_ordpag == 0:
            self.saldo_ord = self.total
        else:
            self.saldo_ord = (self.total) - (self.valor_ordpag)



    # add valor apagar no op
    @api.onchange('docPag')
    def _add_valor_apagar(self):
        if self.docPag == True:
            self.valorPago = self.saldo_pagamento
        else:
            self.valorPago = 0


    # add valor Acobrar
    @api.onchange('cobrado')
    def _add_valor_cobrado(self):

        if self.cobrado == True:
            self.valorreceb = self.saldo
            self.valor_saldo = self.saldo
        else:
            self.valorreceb = 0
            self.valor_saldo = 0

    #@api.constrains('cobrado')
    #def ve_ord(self):#ver ordem recebimento
    #    doc_obj = self.env['reg.docum'].search(
    #        [('saldo', '<', self.saldo), ('numer_prest', '<', self.numer_prest), ('nome_terc', '=', self.nome_terc.id),
    #         ('estado', '!=', '3')])
    #    if doc_obj:
    #        warning = {
    #            'title': _('Atenção!'),
    #            'message': _('O prestação Anterior precisa ser concluida!'),
    #        }
    #        return {'warning': warning}

            # add valor para ordem pag
    @api.onchange('ordem_pago')
    def _add_valor_apagar_ord(self):
        if self.ordem_pago == True:
            self.valor_ordpag = self.saldo_pagamento
        else:
            self.valor_ordpag = 0



    # verificar o valor aplicado para pagamento
    @api.constrains('valorPago')
    def _verif_valor_apagar(self):
        if self.valorPago > self.saldo_pagamento:
            warning = {
                'title': _('Atenção!'),
                'message': _('O VALOR A SER PAGO NÃO PODE SER MAIOR QUE O SALDO!'),
            }
            return {'warning': warning}

    # verificar o valor aplicado para receber
    @api.constrains('valorreceb')
    def _verif_valor_receber(self):
        self.aval_det_docum = True
        if self.valorreceb > self.saldo:

            warning = {
                'title': _('Atenção!'),
                'message': _('O VALOR A SER RECEBIDO NÃO PODE SER MAIOR QUE O SALDO!'),
            }
            return {'warning': warning}



    # Pagar os docum ordenadas quando docmento e de despesa
    #@api.constrains('pago')
    #def _change_docum_status(self):
    #    if self.pago:
    #        docs = self.env['reg.docum'].search([('id', '!=', self.id), ('ordem_pago', '=', True)])
    #        for record in docs:
    #            record.pago = True



    # mudar docum de estado quando foi ordenado muda de estado
    @api.one
    def passar_para_ordenado(self):
        if self.ordem_pago == True:
            self.write({'control_estad_docum': 'ordenado'})



    # mudar estado de docum quando pago e marcar doc OP como pago
    @api.one
    def passar_para_pago(self):
        if self.docPag == True:
            self.write({'control_estad_docum': 'pago'})
            self.pago = True

    # Adicionar valor debido e credito
    @api.one
    def add_valor_debt_credt(self):
        if self.desting_doc_desp == True:
            self.credito = self.total
            if self.encont_docum_desp:
               self.valor_encontro = self.total

        if self.desting_doc_vend == True:
            self.debito = self.total
            if self.encont_docum_client:
               self.valor_encontro = self.total



    # add valor para ordem pag
    @api.onchange('encontro')
    @api.depends('credito', 'debito')
    def add_valor_asaldar(self):
        if self.encontro == True:
            if self.debito != 0:
               self.saldar = self.debito
            else:
                 self.saldar = self.credito
        else:
            self.saldar = 0





