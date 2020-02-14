# -*- coding: utf-8 -*-

import psycopg2

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

import datetime

class pagamentoRecebimento(models.Model):
    _name = 'pagamento.recebimento'
    _description = 'Pagamento/Recebimento'
    _rec_name = 'n_documento'


    #Campos Pagamento ---------------------------------------------------------------------------------------------------------------
    nossa_conta_compras = fields.Many2one('monetario.monetario', string='Nossa Conta')#, domain="[('tipo_meio','=','2')]"
    terceiro_id_doc_conta_corente = fields.Many2one('terceiro.terceiro', string='Terceiro')#, domain=[('tem_despesas', '=', True)]
    reg_docum_desp_ids = fields.Many2many('reg.docum', string="Reg Docum", store=True, copy=True)#'pagamento_recebimento_id',
    documentoTesoraria_ids = fields.One2many('documento.tesoraria.pagamento', 'doc_tesou_pagamento_id', string='detale')
    n_pagam = fields.Char(string='Pqagamento Nº', copy=False, readonly=True, store=True, index=True,)
    montante_pago = fields.Float(string="Montante", store=True, copy=True)
    valor_total_pag = fields.Float(string='Saida', store=True, copy=True, readonly=False)  # compute="_compute_val_tot",
    valor_pag = fields.Float(string='Saida', store=True, copy=True, readonly=False)
    pagamento_id = fields.Many2one('tesouraria.pagamento', string="Pagamento")
    date = fields.Date(string='Data ', default=fields.Date.today)

    name = fields.Char(string='Documento', related="terceiro_id_doc_conta_corente.name", store=True, readonly=True)
    saldo = fields.Float(string='Saldo', related="nossa_conta_compras.saldo_inicial", store=True, readonly=True)
    cod_terceiro = fields.Char(string="Codigo", related="terceiro_id_doc_conta_corente.codigo")
    nome_terceiro = fields.Char(string='Terceiro', related="terceiro_id_doc_conta_corente.name", store=True, readonly=True)
    tem_despesas = fields.Boolean(string="Despesa", related="terceiro_id_doc_conta_corente.tem_despesas", )
    nif_benificiario = fields.Integer(string="Nif", related="terceiro_id_doc_conta_corente.nif")#para remover
    nif_pessoa = fields.Char(string="NIF", size=9, related="terceiro_id_doc_conta_corente.nif_pessoa")# required=True,
    #-------------------------------------------------------------------------------------------------------------------------------


    # geral-------------------------------------------------------------------------------------------------------------------------
    tipo_pagamento_receb = fields.Selection(
        [('1', 'Dinheiro'),
         ('2', 'Cheque'),
         ('3', 'Transferência'), ('4', 'Deposito')],
        'Tipo')# required=True,  , default='dinheiro'
    documentot = fields.Selection(
        [('1', 'Documento Conta Corrente'),
         ('2', 'Documento de Tesouraria')],
        'Documento', Widget="radio")#, default='1'
    type_docum = fields.Selection(
        [('recebimento', 'Recebimento'), ('pagamento', 'Pagamento'), ('movimento', 'Movimento')], readonly=True,
        index=True, track_visibility='always', store=True)# change_default=True, default=lambda self: self._context.get('type_docum', 'pagamento'),
    n_cheque = fields.Char(string='Numero Cheque')
    cheque = fields.Char(string='Cheque')
    data = fields.Date('Data')
    contabilizado = fields.Boolean(string='Contabilizado')
    diario = fields.Char(string='Diario')
    numero = fields.Integer(string='Numero')
    detalhes = fields.Char(string='Detalhes', readonly=False, store=True)
    tipo_meio = fields.Selection([('1', 'Caixa'), ('2', 'Desposto a Ordem'), ('3', 'Fundo de Maneio')],
                                 'Tipo', related="nossa_conta.tipo_meio", )


    #campos recebimentos -----------------------------------------------------------------------------------------------------------
    terceiro_id_doc_conta_corente_receb = fields.Many2one('terceiro.terceiro', string='Cliente')#, domain=[('tem_fatur', '=', True)]
    nossa_conta = fields.Many2one('monetario.monetario', string='Nossa Conta') #, domain="[('tipo_meio','=','2')]"
    banco = fields.Many2one('entbanc.entbanc', string='Banco')
    conta_caicha = fields.Float(string='Conta Caixa')
    refe = fields.Char(string='Ref')
    n_recibo = fields.Char(string='Recebimento Nº', store=True, copy=False, readonly=True, index=True, )
    reg_docum_ids_receb = fields.Many2many('reg.docum', string="Reg Docum", store=True, copy=True)
    doc_teso = fields.One2many('documento.tesoraria.recebimento', 'teso_receb_id', string='detalt', oldname='detal_lin')
    select = fields.Boolean(string='select', default=True)  # vervalor_total_receb
    vervalor_total_receb = fields.Float(string='Entrada', store=True, copy=True)  # compute="_compute_val_tot",
    vervalor_receb = fields.Float(string='Entrada', store=True, copy=True)
    montante_receb = fields.Float(string="Montante", store=True, copy=True)
    recebimento_id = fields.Many2one('tesouraria.recebimento', string="Recebimento")
    valor_saldo_total = fields.Float(string="Valor saldo Calculado", store=True, copy=True)  # saldo para ser recebido


    nome_cliente = fields.Char(string='Cliente', related="terceiro_id_doc_conta_corente_receb.name", store=True, readonly=True)
    descricao_conta = fields.Char(string="Descrição Conta", related="nossa_conta.name", )
    street_cliente = fields.Char(string="Endereso Cliente", related="terceiro_id_doc_conta_corente_receb.street")
    cod_cliente = fields.Char(string="Codigo", related="terceiro_id_doc_conta_corente_receb.codigo")
    tem_solicitacao = fields.Selection([('1', 'Sim'), ('2', 'Não')], string="Tem Fatura", related="terceiro_id_doc_conta_corente_receb.tem_solicitacao", )
    nif_cliente = fields.Integer(string="Nif", related="terceiro_id_doc_conta_corente_receb.nif")#para remover
    nif = fields.Integer(string="Nif", related="terceiro_id_doc_conta_corente_receb.nif")#para remover
    telefone_fixo = fields.Integer(string="Telefone Fixo", related="terceiro_id_doc_conta_corente_receb.fax", store=True)#para remover
    telemovel = fields.Integer(string="Telemovel", related="terceiro_id_doc_conta_corente_receb.phone", store=True)#para remover
    nif_pessoareceb = fields.Char(string="NIF", size=9, related="terceiro_id_doc_conta_corente_receb.nif_pessoa")# required=True,
    telefone_pessoa = fields.Char(string="Telefone", size=7, related="terceiro_id_doc_conta_corente_receb.telefone_pessoa")#, required=True
    fixo_pessoa = fields.Char(string="Fax", size=7, related="terceiro_id_doc_conta_corente_receb.fixo_pessoa")#required=True,



    #------------------> saõ Controlos -------------------------------------------------------------------------------------------------------------
    n_documento = fields.Char(string='Nº', copy=False, readonly=True,
                              index=True, default=lambda self: _('New'))
    codigo = fields.Char(string="Codigo", copy=False, readonly=True,
                         index=True, store=True, default=lambda self: self._get_next_cod())
    sequence_id = fields.Many2one('ir.sequence', string='Sequência de entrada', required=False, copy=False)
    despesa_id = fields.Many2one('despesa', string="Despesas")
    moeda_impremir_recibo = fields.Many2one('moeda.moeda', string='Moeda Imprimir Recibo')
    control_pa_rece = fields.Boolean(string="Controla siqu")
    displlay_type = fields.Selection([('line_section', 'section'), ('line_note', 'nota')], string='displlay')
    state = fields.Selection([('draft', 'Draft'), ('open', 'Open'), ('paid', 'Paid'), ('cancel', 'Cancelled'), ])
    benificiario_doc_tesso = fields.Many2one('terceiro.terceiro', string='Beneficiário')
    reg_docum_ids = fields.One2many('reg.docum', 'pagamento_recebimento_id', string="Reg Docum", store=True, copy=True)
    #-------------------------------------------------------------------------------------------------------------------------------


    #-Movimento interno------------------------------------------------------------------------------------------------------------------------------
    n_movimento = fields.Char(string='Movimento Nº', copy=False, readonly=True, index=True, )
    nossa_conta_transfe = fields.Many2one('monetario.monetario', string='Conta Origem')  # , domain="[('tipo_meio','=','2')]"
    movimento = fields.Many2one('movinterno.movinterno', string='Movimento')
    date_release = fields.Date('Data', default=fields.Date.today)
    centro_custo = fields.Many2one('planconta.planconta', string='Centro Custo')
    montante_mov = fields.Float(string='Montante')
    esc = fields.Float(string='Esc')
    conta_destino = fields.Many2one('monetario.monetario', string='Conta Destino')
    conta_des = fields.Many2one('planconta.planconta', string='Conta dest Id', related="conta_destino.conta")
    escd = fields.Float(string='Esc')
    diariod = fields.Integer(string='Diario')
    contabilizadod = fields.Boolean(string='Contabilizado')
    numerod = fields.Integer(string='Numero')
    tipo_movimento = fields.Selection([('1', 'Tranfirencia'), ('2', 'Entrada'), ('3', 'Saida')],
                                      'Tipo Movimento', Widget="radio", store=True)
    descricao = fields.Text('Descrição')
    mov_sai_ent = fields.Boolean(string="Transferencia saida e entrada")
    mov_sai = fields.Boolean(string="Mov", default=True)  # permite filtrar apenas um movimento no tree
    movimentado = fields.Boolean(string="Movimentadol")
    anulado = fields.Boolean(string="Anulado")
    folha_tesouraria_id = fields.Many2one('folha.tesouraria')
    cod_movint = fields.Integer(string="Codigo Movimento")
    diario_orig_id = fields.Many2one('diario.diario', string="Diario Origem")

    saldo_transf = fields.Float(string='Saldo', related="nossa_conta_transfe.saldo_inicial", store=True, readonly=True)
    nome_conta_origem = fields.Char(string="Nome Conta Origem", related="nossa_conta_transfe.name")
    nome_conta_dest = fields.Char(string="Nome Conta Destino", related="conta_destino.name")
    desc_mov = fields.Char(string="Desc Movimento", related="movimento.name")
    conta_mei_orig_id = fields.Many2one('planconta.planconta', string='Conta Id',
                                        related="nossa_conta_transfe.conta")  # vem de meio monet
    conta_id = fields.Many2one('planconta.planconta', string='Conta Id',
                               related="movimento.conta")  # vem de conceito mov inter
    tip_movimento = fields.Selection(
        [('1', 'Pagamento'),
         ('2', 'Recebimento'), ('3', 'Movimento Interno')], store=True, string='Documento', Widget="radio",
        default='3')

    dados_antigo = fields.Boolean(string="Dados Antigo")  # se True porque os dados são antigo

    @api.one
    @api.constrains('dados_antigo')
    def val_dados_antig(self):  # Verificar se o dados e antigo ou não
        if self.dados_antigo == True:
            pass
        # raise ValidationError(
        #    'Dados antigo, ha algumas informações que precisam ser modificado, contacta o adminstrador de sistema se consideras-te que é um erro ')


    mov_inter_orig = fields.Boolean(string="Ccntrol mov inter Origen")#controla o movimento interno do origem (02)
    mov_inter_orig_01 = fields.Boolean(string="Ccntrol mov inter Origen")
    mov_inter_orig_02 = fields.Boolean(string="Ccntrol mov inter Origen")
    mov_inter_orig_03 = fields.Boolean(string="Ccntrol mov inter Origen")
    mov_inter_orig_04 = fields.Boolean(string="Ccntrol mov inter Origen")
    mov_inter_orig_05 = fields.Boolean(string="Ccntrol mov inter Origen")
    mov_inter_orig_06 = fields.Boolean(string="Ccntrol mov inter Origen")
    mov_inter_orig_07 = fields.Boolean(string="Ccntrol mov inter Origen")
    mov_inter_orig_08 = fields.Boolean(string="Ccntrol mov inter Origen")
    mov_inter_orig_09 = fields.Boolean(string="Ccntrol mov inter Origen")
    mov_inter_orig_10 = fields.Boolean(string="Ccntrol mov inter Origen")
    mov_inter_orig_11 = fields.Boolean(string="Ccntrol mov inter Origen")




    DADOS_IMPOR = fields.Boolean(string="DADOS IMPOR", default=True)
    IDTERC = fields.Char()
    CMOVINT = fields.Char()
    CMOVINT2 = fields.Integer()
    CNUMFEC = fields.Char()
    cnumfec1 = fields.Char()
    CCODMED = fields.Char()
    ccodmed1 = fields.Char()
    cnumfec_int = fields.Integer()
    CNUMPAG = fields.Char()
    CCODTER = fields.Char()
    CNOMTER = fields.Char()
    CDETPAG = fields.Char()
    CNUMORD = fields.Char()
    DFECPAGDATPAG = fields.Char()

    #Cod movimento interno
    ccodmov = fields.Char()
    dfecmovint = fields.Char()
    ccodint = fields.Char()
    ntipmov = fields.Char()
    cdiariorig = fields.Char()
    cmedori = fields.Char()
    cmedori1 = fields.Integer()
    cmovori = fields.Char()
    cmovori_int = fields.Integer()
    cordori = fields.Char()

    cmeddes = fields.Char()
    cmeddes1 = fields.Integer()
    cdiades = fields.Char()
    cmovdest = fields.Char()
    cordordes = fields.Char()
    lanulado = fields.Boolean()


    @api.model
    def _get_next_cod(self):
        sequence_np = self.env['ir.sequence'].search([('code', '=', 'tesouraria.pag.receb.codigo')])
        next_np = sequence_np.get_next_char(sequence_np.number_next_actual)
        return next_np

    @api.model
    def create(self, vals):

            vals['cod_documento'] = self.env['ir.sequence'].next_by_code('codigo.codigo') or _('New')
            vals['codigo'] = self.env['ir.sequence'].next_by_code('tesouraria.pag.receb.codigo')
            res = super(pagamentoRecebimento, self).create(vals)
            res.creat_lacamento()
            #res.reg_docum_ids.passar_para_pago()
            #res.link_diar()
            return res

    def creat_lacamento(self):#Lancamento de movimento interno
        date = datetime.datetime.today()
        if self.type_docum == 'movimento':
           if self.dados_antigo == False:
                  diamov = date.day
                  mesmov = date.month
                  anomov = date.year

                  if self.mov_sai_ent == True:
                      dear = self.diario_orig_id
                      diario = int(dear)
                  else:
                      dear = self.diariod
                      diario = int(dear)
                  new_lancamento = self.env['lancamento_diario.lancamento_diario']
                  lanca = new_lancamento.create(
                      {'diario': diario, 'data': self.date_release, 'tipo_movimento': self.tip_movimento,'valor': self.montante_mov,'obs': 'FastGest Tesouraria Movimento Interno',
                       'cod_movint': self.id, 'diamov': diamov, 'mesmov': mesmov, 'anomov': anomov,})
           if self.dados_antigo == True:
                  dat = self.dfecpag
                  x = dat.split('/')
                  datefec = x
                  list = []
                  for a in datefec:
                      list.append(a)
                  mesmov = list[0]
                  diamov = list[1]
                  anomov = list[2]
                  if self.mov_sai_ent == True:
                      dear = self.cdiariorig
                      diario = int(dear)
                  else:
                      dear = self.diariod
                      diario = int(dear)
                  new_lancamento = self.env['lancamento_diario.lancamento_diario']
                  lanca = new_lancamento.create({'dados_antigo': 'True','diario': diario, 'tipo_movimento': self.tip_movimento,'data': self.date_release, 'valor': self.montante_mov,
                       'cod_movint': self.id, 'diamov': diamov, 'mesmov': mesmov, 'anomov': anomov, 'obs': 'FastGest Tesouraria Movimento Interno',})

           num_cheq = self.cheque
           #==================SE TIPO MOVIMENTO E TRANFER===========================================================
           if self.tipo_movimento == '1':  # Transfer
              if self.mov_sai_ent == False:
                 new_det_lan_pret = self.env['detalhe.lancamento']
                 det_lanca_pret = new_det_lan_pret.create({'codigo_conta': self.conta_mei_orig_id.id, 'valor_credito': self.montante_mov,
                                                           'descritivo': 'Cheque Nº' + str(num_cheq),
                                                              'deb_cred': 'C', 'cod_movint': self.id, })
                 new_det_lan_pret = self.env['detalhe.lancamento']
                 det_lanca_pret = new_det_lan_pret.create({'codigo_conta': self.conta_id.id, 'valor_credito': self.montante_mov,
                                                           'descritivo': 'Cheque Nº' + str(num_cheq),
                                                           'deb_cred': 'D', 'cod_movint': self.id, })
              else:
                  new_det_lan_pret = self.env['detalhe.lancamento']
                  det_lanca_pret = new_det_lan_pret.create(
                      {'codigo_conta': self.conta_id.id, 'valor_credito': self.montante_mov,
                       'descritivo': 'Cheque Nº' + str(num_cheq),
                       'deb_cred': 'D', 'cod_movint': self.id, })
                  new_det_lan_pret = self.env['detalhe.lancamento']
                  det_lanca_pret = new_det_lan_pret.create(
                      {'codigo_conta': self.conta_mei_orig_id.id, 'valor_credito': self.montante_mov,
                       'descritivo': 'Cheque Nº' + str(num_cheq),
                       'deb_cred': 'C', 'cod_movint': self.id})
           #================================================================================================================

           elif self.tipo_movimento == '2':#ENTRADA
               new_det_lan_pret = self.env['detalhe.lancamento']
               det_lanca_pret = new_det_lan_pret.create(
                   {'codigo_conta': self.conta_des.id, 'valor_credito': self.montante_mov,
                    'descritivo': self.detalhes,
                    'deb_cred': 'D', 'cod_movint': self.id, })
               new_det_lan_pret = self.env['detalhe.lancamento']
               det_lanca_pret = new_det_lan_pret.create(
                   {'codigo_conta': self.conta_id.id, 'valor_credito': self.montante_mov,
                    'descritivo': self.detalhes,
                    'deb_cred': 'C', 'cod_movint': self.id, })

           elif self.tipo_movimento == '3':  # SAIDA
               new_det_lan_pret = self.env['detalhe.lancamento']
               det_lanca_pret = new_det_lan_pret.create(
                   {'codigo_conta': self.conta_id.id, 'valor_credito': self.montante_mov,
                    'descritivo': self.detalhes,
                    'deb_cred': 'C', 'cod_movint': self.id, })
               new_det_lan_pret = self.env['detalhe.lancamento']
               det_lanca_pret = new_det_lan_pret.create(
                   {'codigo_conta': self.conta_mei_orig_id.id, 'valor_credito': self.montante_mov,
                    'descritivo': self.detalhes,
                    'deb_cred': 'D', 'cod_movint': self.id, })

           lanca = self.env['lancamento_diario.lancamento_diario'].search([('id', '>=', 1)])
           if lanca:
               for l in lanca:
                   det_lanc = self.env['detalhe.lancamento'].search(
                       [('cod_movint', '=', l.cod_movint)])
                   for dl in det_lanc:
                       dl.lancamento_diario = l.id



    # ----------------------------------------------------------------------------------------------------------------
    #@api.one
    #@api.depends('montante_mov')
    @api.one
    @api.depends('valor_pag', 'vervalor_receb', 'montante_mov')
    def _compute_val_tot(self):
        if self.type_docum == 'pagamento':
           self.valor_total_pag = self.valor_pag
           self.montante_pago = self.valor_total_pag
        elif self.type_docum == 'recebimento':
            self.vervalor_total_receb = self.vervalor_receb
            self.montante_receb = self.vervalor_total_receb
        elif self.type_docum == 'movimento':
            if self.tipo_movimento == '1': #Transfer
                if self.mov_sai_ent == False: #se eta falso o movimento e de saida
                   self.valor_total_pag = self.montante_mov
                else:
                    self.vervalor_total_receb = self.montante_mov
            elif self.tipo_movimento == '2': #Entrada
                 self.vervalor_total_receb = self.montante_mov
            elif self.tipo_movimento == '3': #Saida
                 self.valor_total_pag = self.montante_mov


    # ----------------------------------------------------------------------------------------------------------------
    #@api.multi #lincar com  diario
    def link_diar(self):
           if self.type_docum == 'recebimento':
               if self.tipo_pagamento_receb != 'dinheiro':
                   diar_teso_receb = self.env['folha.tesouraria'].search([('folha', '=', self.nossa_conta.id), ('fechado', '=', '2')])
                   if diar_teso_receb:
                      for lin in diar_teso_receb:
                          self.folha_tesouraria_id = lin.id
                          lin.valor_movimento = self.vervalor_total_receb
                          lin.terceiro_id_doc_conta_corente_receb = self.terceiro_id_doc_conta_corente_receb.id
                          lin.sald_sigu += self.montante_receb
                   else:
                     raise ValidationError('Este diario não esta aberta')
               elif self.tipo_pagamento_receb == 'dinheiro':
                       diar_teso_recebe = self.env['folha.tesouraria'].search(
                           [('name', '=', 'CAIXA PRINCIPAL'), ('fechado', '=', '2')])
                       if diar_teso_recebe:
                          for linhas in diar_teso_recebe:
                              self.folha_tesouraria_id = linhas.id
                              linhas.valor_movimento = self.vervalor_total_receb
                              linhas.terceiro_id_doc_conta_corente_receb = self.terceiro_id_doc_conta_corente_receb.id
                              linhas.sald_sigu += self.montante_receb
                       else:
                           raise ValidationError('Este diario não esta aberta')
               # lik com det docum tesoura
               if self.documentot == 'documento de tesouraria':
                   ligar = self.env['documento.tesoraria.recebimento'].search(
                       [('recebimento_id', '=', self.recebimento_id.id)])
                   for l in ligar:
                       l.doc_tesou_pagamento_id = self.id

           elif self.type_docum == 'pagamento':
               if self.tipo_pagamento_receb != 'dinheiro':
                   diar_teso_pag_ = self.env['folha.tesouraria'].search(
                       [('folha', '=', self.nossa_conta_compras.id), ('fechado', '=', '2')])
                   if diar_teso_pag_:
                      for linha in diar_teso_pag_:
                          self.folha_tesouraria_id = linha.id
                          linha.valor_movimento = self.valor_total_pag
                          linha.terceiro_id_doc_conta_corente_receb = self.terceiro_id_doc_conta_corente.id
                          linha.sald_sigu -= self.montante_pago
                   else:
                       raise ValidationError('Este diario não esta aberta')
               elif self.tipo_pagamento_receb == 'dinheiro':

                       diar_teso_paga_ = self.env['folha.tesouraria'].search(
                           [('name', '=', 'CAIXA PRINCIPAL'), ('fechado', '=', '2')])
                       if diar_teso_paga_:
                          for linha in diar_teso_paga_:
                              self.folha_tesouraria_id = linha.id
                              linha.valor_movimento = self.valor_total_pag
                              linha.terceiro_id_doc_conta_corente_receb = self.terceiro_id_doc_conta_corente.id
                              linha.sald_sigu -= self.montante_pago
                       else:
                           raise ValidationError('Este diario não esta aberta')
               #lik com det docum tesoura
               if self.documentot == 'documento de tesouraria':
                   ligar = self.env['documento.tesoraria.pagamento'].search([('pagamento_id', '=', self.pagamento_id.id)])
                   for l in ligar:
                       l.doc_tesou_pagamento_id = self.id

           elif self.type_docum == 'movimento':
               # self.mov_sai_ent = True  # este campo controla o movimento interno
               # self.copy()
               # self.write({'confirmar_fecho': '1'})
               self.mov_sai =True #este campo permite que o tree filtra apenas um movimento
               if self.tipo_movimento == '1':
                   # tira de Origem
                   movim_orig = self.env['monetario.monetario'].search([('id', '=', self.nossa_conta_transfe.id)])
                   for l in movim_orig:
                       l.saldo_inicial -= self.montante_mov
                   movim_orig_diar = self.env['folha.tesouraria'].search([('id', '=', self.nossa_conta_transfe.id)])
                   for linha in movim_orig_diar:
                       linha.saldo_ant -= self.montante_mov
                       linha.sald_sigu += self.montante_mov

                   # Add no destino
                   movim_dest = self.env['monetario.monetario'].search([('id', '=', self.conta_destino.id)])
                   for rec in movim_dest:
                       rec.saldo_inicial += self.montante_mov
                   movim_dest_diar = self.env['folha.tesouraria'].search([('id', '=', self.conta_destino.id)])
                   for dados in movim_dest_diar:
                       dados.saldo_ant += self.montante_mov


                   # Movimento de saida
                   diar_teso_destino = self.env['folha.tesouraria'].search(
                       [('folha', '=', self.conta_destino.id), ('fechado', '=', '2')])
                   for lin in diar_teso_destino:
                       if self.mov_sai_ent == True:
                           self.folha_tesouraria_id = lin.id

                   # Movimento de entrada
                   add_mov_saida = self.env['pagamento.recebimento'].search(
                       [('movimentado', '=', False), ('mov_sai_ent', '=', False)])
                   diar_teso_orig = self.env['folha.tesouraria'].search(
                       [('folha', '=', self.nossa_conta_transfe.id), ('fechado', '=', '2')])
                   for lin in diar_teso_orig:
                       for mov in add_mov_saida:
                           mov.folha_tesouraria_id = lin.id

                   normaliz_mov = self.env['pagamento.recebimento'].search([('mov_sai_ent', '=', False)])
                   for r in normaliz_mov:
                       r.movimentado = True

               elif self.tipo_movimento == '2':  # Entrada
                   # Add no destino
                   movim_dest = self.env['monetario.monetario'].search([('id', '=', self.conta_destino.id)])
                   for rec in movim_dest:
                       rec.saldo_inicial += self.montante_mov
                   movim_dest_diar = self.env['folha.tesouraria'].search([('id', '=', self.conta_destino.id)])
                   for dados in movim_dest_diar:
                       dados.saldo_ant += self.montante_mov
                       dados.sald_sigu += self.montante_mov

                   # Movimento de entrada
                   add_mov_saida = self.env['pagamento.recebimento'].search(
                       [('mov_sai_ent', '=', True)])
                   diar_teso_orig = self.env['folha.tesouraria'].search(
                       [('folha', '=', self.conta_destino.id), ('fechado', '=', '2')])
                   for lin in diar_teso_orig:
                       for mov in add_mov_saida:
                           mov.folha_tesouraria_id = lin.id

               elif self.tipo_movimento == '3':  # Saida
                   #Tirar
                   movim_orig = self.env['monetario.monetario'].search([('id', '=', self.nossa_conta_transfe.id)])
                   for l in movim_orig:
                       l.saldo_inicial -= self.montante_mov
                   movim_orig_diar = self.env['folha.tesouraria'].search([('id', '=', self.nossa_conta_transfe.id)])
                   for linha in movim_orig_diar:
                       linha.saldo_ant -= self.montante_mov

                   # Movimento de saida
                   diar_teso_destino = self.env['folha.tesouraria'].search(
                       [('folha', '=', self.nossa_conta_transfe.id), ('fechado', '=', '2')])
                   for lin in diar_teso_destino:
                       if self.mov_sai_ent == False:
                           self.folha_tesouraria_id = lin.id
    # ----------------------------------------------------------------------------------------------------------------








