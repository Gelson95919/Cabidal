# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import datetime


class tesourariaPagamento(models.Model):
    _name = 'tesouraria.pagamento'
    _description = 'Pagamento'
    _order = 'id desc'

    tipo_pagamento_receb = fields.Selection(
        [('1', 'Dinheiro'),
         ('2', 'Cheque'),
         ('3', 'Transferência')],
        'Tipo', required=True, default='1', store=True)
    n_cheque = fields.Char(string='Numero Cheque')
    nossa_conta_compras = fields.Many2one('monetario.monetario', string='Nossa Conta',
                                          domain="[('tipo_meio','=','2')]")
    data = fields.Date('Data')
    terceiro_id_doc_conta_corente = fields.Many2one('terceiro.terceiro', string='Terceiro',
                                                    required=True, )  # , domain=[('tem_despesas', '=', True)]
    name = fields.Char(string='Documento', related="terceiro_id_doc_conta_corente.name", store=True, readonly=True)
    documentot = fields.Selection(
        [('1', 'Documento Conta Corrente'),
         ('2', 'Documento de Tesouraria')], store=True, string='Documento', Widget="radio", default='1')
    reg_docum_ids = fields.Many2many('reg.docum', string="Reg Docum", store=True, copy=True)  # , 'pagamento_id'
    #proximo importacao temos que trabalhar com eses campos nção o di cima
    det_reg_docum_ids = fields.One2many('reg.docum', 'pagamento_id', string="Reg Docum Det", store=True, copy=True)  # , 'pagamento_id'
    det_reg_docum_ids_contab = fields.One2many('reg.docum', 'pagamento_id', string="Reg Docum Det", store=True, copy=True)  # , 'pagamento_id'


    documentoTesoraria_ids = fields.One2many('documento.tesoraria.pagamento', 'pagamento_id', string='detale')
    n_pagam = fields.Char(string='Pqagamento Nº', copy=False, readonly=True, store=True,
                          index=True, default=lambda self: self._get_next_cod())
    contabilizado = fields.Boolean(string='Contabilizado')
    diario = fields.Many2one('diario.diario', string='Diario', related="nossa_conta_compras.diario")
    name_diario = fields.Char(string="Nome Diario", related="nossa_conta_compras.name_diario")
    conta = fields.Many2one('planconta.planconta', string='Conta', related="nossa_conta_compras.conta")
    leva_terce = fields.Boolean(string='Leva Terceiro', related='conta.leva_terce')
    # diario = fields.Integer(string='Diario', related="nossa_conta_compras.codigo_diario")
    numero = fields.Integer(string='Numero Diario')
    saldo = fields.Float(string='Saldo', related="nossa_conta_compras.saldo_inicial", store=True, readonly=True)
    cheque = fields.Char(string='Cheque')
    cod_terceiro = fields.Char(string="Codigo", related="terceiro_id_doc_conta_corente.codigo")
    nome_terceiro = fields.Char(string='Terceiro', related="terceiro_id_doc_conta_corente.name", store=True,
                                readonly=True)
    valor_total_pag = fields.Float(string='Vlor Total Pago', store=True, copy=True, readonly=False,
                                   compute="_compute_val_tot")  #
    montante_pago = fields.Float(string="Montante", store=True, copy=True, compute="_compute_val_tot")  #
    tipo_meio = fields.Selection([('1', 'Caixa'), ('2', 'Desposto a Ordem'), ('3', 'Fundo de Maneio')],
                                 'Tipo', related="nossa_conta_compras.tipo_meio", )
    date = fields.Date(string='Data', default=fields.Date.today)  #
    detalhes = fields.Char(string='Detalhes Documento', readonly=False, copy=True, store=True, compute="add_detal")  #
    det_obs_doc_tesora = fields.Char(string='OBS')
    type_docum = fields.Selection(
        [('recebimento', 'Recebimento'), ('pagamento', 'Pagamento'), ('movimento', 'Movimento')], readonly=True,
        index=True, change_default=True, default=lambda self: self._context.get('type_docum', 'pagamento'),
        track_visibility='always', store=True)
    nif_benificiario = fields.Integer(string="Nif", related="terceiro_id_doc_conta_corente.nif")  # para remover
    tem_despesas = fields.Boolean(string="Despesa", related="terceiro_id_doc_conta_corente.tem_despesas", )
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

    nif_pessoa = fields.Char(string="NIF", size=9, related="terceiro_id_doc_conta_corente.nif_pessoa")  # required=True,
    telefone_pessoa = fields.Char(string="Telefone", size=7,
                                  related="terceiro_id_doc_conta_corente.telefone_pessoa")  # required=True,
    fixo_pessoa = fields.Char(string="Fax", size=7,
                              related="terceiro_id_doc_conta_corente.fixo_pessoa")  # , required=True
    ata_id = fields.Integer(string="ID Ata", related="terceiro_id_doc_conta_corente.ata_id", store=True)  # para ajudar no procedimento de pagar

    dados_antigo = fields.Boolean(string="Dados Antigo")  # se True porque os dados são antigo
    tipo_movimento = fields.Selection([('1', 'Pagamento'), ('2', 'Recebimento'), ('3', 'Movimento Interno')],
                                      store=True, string='Documento', Widget="radio", default='1')
    origem = fields.Boolean(string="Origem da contabilidade")



    @api.one
    @api.constrains('dados_antigo')
    def val_dados_antig(self):  # Verificar se o dados e antigo ou não
        if self.dados_antigo == True:
            pass
        # raise ValidationError(
        #    'Dados antigo, ha algumas informações que precisam ser modificado, contacta o adminstrador de sistema se consideras-te que é um erro ')

    DADOS_IMPOR = fields.Boolean(string="DADOS IMPOR", default=True)
    IDTERC = fields.Char()
    CMOVINT = fields.Char()
    CMOVINT2 = fields.Integer()
    CNUMFEC = fields.Char()
    CCODMED = fields.Char()
    CNUMPAG = fields.Char()
    CCODTER = fields.Char()
    CNOMTER = fields.Char()
    CDETPAG = fields.Char()
    CNUMORD = fields.Char()

    DFECPAGDATPAG = fields.Char()
    DFECPAG = fields.Char()

    dfecpag = fields.Char()
    cmovint = fields.Char()

    # 1111111111111111111111111111111111111111111111111111111111
    def compor_op(self):
        # pass
        pagamento = self.env['tesouraria.pagamento'].search([('id', '>', 0)])
        for p in pagamento:
            p.cmovint = p.CMOVINT2
        #    docum = self.env['pagamento.recebimento'].search([('CMOVINT', '=', p.CMOVINT), ('type_docum', '=', 'pagamento')])
        #    for d in docum:
        #         d.CCODMED = p.CCODMED
        #        d.tipo_pagamento_receb = p.tipo_pagamento_receb
        #        d.documentot = p.documentot
        #        d.n_cheque = p.n_cheque
        #        d.diario = p.diario
        #        d.numero = p.numero

        # teso_pagamento = self.env['tesouraria.pagamento'].search([('id', '>', 0)])
        # for tp in teso_pagamento:
        #    pagamento = self.env['pagamento.recebimento']
        #    pagam = pagamento.create({'nossa_conta_compras': tp.nossa_conta_compras.id, 'terceiro_id_doc_conta_corente': tp.terceiro_id_doc_conta_corente.id,
        #                                         'n_pagam': tp.n_pagam,
        #                                         'montante_pago': tp.valor_total_pag,
        #                                         'valor_total_pag': tp.valor_total_pag,
        #                                         'valor_pag': tp.valor_total_pag,
        #                                         'pagamento_id': tp.id,
        #                                         'DADOS_IMPOR': tp.DADOS_IMPOR,
        #                                         'IDTERC': tp.IDTERC,
        #                                         'CMOVINT': tp.CMOVINT,
        #                                         'CMOVINT2': tp.CMOVINT2,
        #                                         'CNUMFEC': tp.CNUMFEC,
        #                                         'CNUMPAG': tp.CNUMPAG,
        #                                         'CCODTER': tp.CCODTER,
        #                                         'CNOMTER': tp.CNOMTER,
        #                                         'CDETPAG': tp.CDETPAG,
        #                                         'CNUMORD': tp.CNUMORD,
        #                                         'DFECPAGDATPAG': tp.DFECPAGDATPAG,})
        # =============================================================================
        # ct = self.env['tesouraria.pagamento'].search([('DADOS_IMPOR', '=', True)])
        # for c in ct:
        #   cod = str(c.CMOVINT)
        #   if cod.isnumeric() == True:
        #      c.CMOVINT2 = c.CMOVINT

    # terc = self.env['terceiro.terceiro'].search([('clientes', '=', True)])
    # for c in terc:
    #     ord_p = self.env['tesouraria.pagamento'].search([('CCODTER', '=', c.codigo)])
    #     for o in ord_p:
    #         o.terceiro_id_doc_conta_corente = c.id

    @api.model
    def _get_next_cod(self):
        sequence_np = self.env['ir.sequence'].search([('code', '=', 'tesopagame.num')])
        next_np = sequence_np.get_next_char(sequence_np.number_next_actual)
        return next_np

    @api.model
    def create(self, vals):
        vals['n_pagam'] = self.env['ir.sequence'].next_by_code('tesopagame.num')
        res = super(tesourariaPagamento, self).create(vals)
        res.create_movimento()
        res.valida_pessoa()
        res.creat_lacamento()
        return res
    def ver_contabilidade(self):
        det_lanc = self.env['detalhe.lancamento'].search([('ver_contab', '=', True)])
        for dl in det_lanc:
            dl.ver_contab = False
        diario = False
        name_diario = False
        data = False
        ordem = False
        valor = False
        valor1 = False
        nome_conta = False
        entidade_d = False
        obs = False
        terceiro_id_doc_conta_corente_receb = False

        pag = self.env['lancamento_diario.lancamento_diario'].search([('cod_pagamento', '=', self.id)])
        det_lanc = self.env['detalhe.lancamento'].search([('cod_pagamento', '=', self.id)])
        for dl in det_lanc:
            dl.ver_contab = True

        ac = self.env['ir.model.data'].xmlid_to_res_id('contabilidade.teste_form',
                                                       raise_if_not_found=True)
        if pag:
            for dad in pag:
                diario = dad.diario.id
                name_diario = dad.name_diario
                data = dad.data
                ordem = dad.ordem
                valor = dad.valor
                valor1 = dad.valor1
                nome_conta = dad.nome_conta
                entidade_d = dad.entidade_d
                obs = dad.obs
                terceiro_id_doc_conta_corente_receb = dad.terceiro_id_doc_conta_corente_receb.id
            result = {
                'name': 'Lançamento',
                'view_type': 'form',
                'res_model': 'lancamento_diario.lancamento_diario',
                'view_id': ac,
                #'context': {'form_view_initial_mode': 'edit', 'force_detailed_view': 'false'},
                'context': {
                    'default_diario': diario,
                    'default_name_diario': name_diario,
                    'default_data': data,
                    'default_ordem': ordem,
                    'default_valor': valor,
                    'default_valor1': valor1,
                    'default_obs': obs,
                    'default_nome_conta': nome_conta,
                    'default_entidade_d': entidade_d,
                    'default_ver_contab': True,
                    'default_terceiro_id_doc_conta_corente_receb': terceiro_id_doc_conta_corente_receb,
                },
                'type': 'ir.actions.act_window',
                'target': 'new',
                'view_mode': 'form'
            }
            return result


    def creat_lacamento(self):
        date = datetime.datetime.today()
        if self.leva_terce == True:
            entidade = self.cod_terceiro
        if self.dados_antigo == False:
            diamov = date.day
            mesmov = date.month
            anomov = date.year
            if self.tipo_pagamento_receb == '1':
                d = self.env['diario.diario'].search([('name', '=', 'DIARIO CAIXA'), ('id', '=', 1)])
                diario = d.id
            else:
                diar = self.diario
                diario = int(diar)
            new_lancamento = self.env['lancamento_diario.lancamento_diario']
            lanca = new_lancamento.create(
                {'diario': diario, 'data': self.date, 'valor': self.valor_total_pag, 'debito': self.valor_total_pag, 'tipo_movimento': self.tipo_movimento,
                 'cod_pagamento': self.id, 'obs': 'FastGest Tesouraria Pagamento', 'conta_d': self.conta.id,
                 'name_diario': self.name_diario, 'diamov': diamov, 'mesmov': mesmov, 'anomov': anomov,
                 'terceiro_id_doc_conta_corente_receb': self.terceiro_id_doc_conta_corente.id})
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
            if self.tipo_pagamento_receb == '1':
                d = self.env['diario.diario'].search([('name', '=', 'DIARIO CAIXA'), ('id', '=', 1)])
                diario = d.id
            else:
                diario = self.diario
            new_lancamento = self.env['lancamento_diario.lancamento_diario']
            lanca = new_lancamento.create(
                {'dados_antigo': 'True', 'diario': diario, 'dfecpag': self.dfecpag, 'valor': self.valor_total_pag, 'debito': self.valor_total_pag,
                 'cod_pagamento': self.id, 'obs': 'FastGest Tesouraria Pagamento', 'conta_d': self.conta.id,
                 'name_diario': self.name_diario, 'diamov': diamov, 'mesmov': mesmov, 'anomov': anomov, 'tipo_movimento': self.tipo_movimento,
                 'terceiro_id_doc_conta_corente_receb': self.terceiro_id_doc_conta_corente.id})


        if self.documentot == '1':
            for line in self.det_reg_docum_ids:
               num_cred = line.numeros_docum
               at_com = self.env['acta.comite'].search([('id', '=', line.ata)])
               if at_com.financiamento_taxa == '2':  # Não
                   if at_com.gerar_conta_popanc == True:
                       for item in range(2):
                           if item == 0:
                               param = self.env['parametros.parametros'].search([('variavel', '=', 'codDesembolso')])
                               cod_comp = self.env['compras.compras'].search([('codigo', '=', param.valor)])
                               new_det_lan = self.env['detalhe.lancamento']  # A linha do valor Desemolso
                               det_lanca = new_det_lan.create({
                                   'codigo_conta': cod_comp.conta_id.id,
                                   'descritivo': 'Desembolso Credito Nº ' + str(num_cred),
                                   'deb_cred': 'D',
                                   'cod_pagamento': self.id,
                                   'valor_credito': self.valor_total_pag,
                                   'terceiro_id_doc_conta_corente_receb': self.terceiro_id_doc_conta_corente.id, })

                           if item == 1:
                               param = self.env['parametros.parametros'].search([('variavel', '=', 'codPoupanca')])
                               cod_comp = self.env['compras.compras'].search([('codigo', '=', param.valor)])
                               new_det_lan = self.env['detalhe.lancamento']  # A linha do valor Poupança
                               det_lanca = new_det_lan.create({
                                   'codigo_conta': cod_comp.conta_id.id,
                                   'descritivo': 'Poupança Credito Nº  ' + str(num_cred),
                                   'deb_cred': 'C',  # 'codigo_entidade': self.cod_terceiro,
                                   'cod_pagamento': self.id,
                                   'valor_credito': self.valor_total_pag,
                                   # Verificar este valor ainda nao esta calculado em op
                                   'terceiro_id_doc_conta_corente_receb': self.terceiro_id_doc_conta_corente.id, })
                           item += 1
                   else:

                       num_cheq = self.n_cheque
                       new_det_lan_pret = self.env['detalhe.lancamento']  # A linha do valor OP
                       det_lanca_pret = new_det_lan_pret.create({'codigo_conta': self.conta.id,
                                                                 'descritivo': 'CHQ. Nº ' + str(
                                                                     num_cheq) + 'Pagamento de OP',
                                                                 'deb_cred': 'C', 'valor_credito': self.valor_total_pag,
                                                                 'terceiro_id_doc_conta_corente_receb': self.terceiro_id_doc_conta_corente.id,
                                                                 'cod_pagamento': self.id, })

                       param = self.env['parametros.parametros'].search([('variavel', '=', 'codDesembolso')])
                       cod_comp = self.env['compras.compras'].search([('codigo', '=', param.valor)])
                       new_det_lan = self.env['detalhe.lancamento']  # A linha do valor Desemolso
                       det_lanca = new_det_lan.create({
                           'codigo_conta': cod_comp.conta_id.id,
                           'descritivo': 'Desembolso Credito Nº ' + str(num_cred),
                           'deb_cred': 'D',  # 'codigo_entidade': self.cod_terceiro,
                           'cod_pagamento': self.id,
                           'valor_credito': self.valor_total_pag,
                           'terceiro_id_doc_conta_corente_receb': self.terceiro_id_doc_conta_corente.id, })
               else: # sim
                   if at_com.gerar_conta_popanc == True:
                       for i in range(2):
                           if i == 0:
                               param_com = self.env['parametros.parametros'].search([('variavel', '=', 'codComicao')])
                               cod_comp_com = self.env['compras.compras'].search([('codigo', '=', param_com.valor)])
                               num_cheq = self.n_cheque
                               new_det_lan_pret = self.env['detalhe.lancamento']  # A linha do valor OP
                               det_lanca_pret = new_det_lan_pret.create({'codigo_conta': cod_comp_com.conta_id.id,
                                                                         'descritivo': 'Comição de Credito ' + str(
                                                                             num_cheq) + 'Pagamento de OP',
                                                                         'deb_cred': 'C',
                                                                         'valor_credito': self.valor_total_pag,
                                                                         'terceiro_id_doc_conta_corente_receb': self.terceiro_id_doc_conta_corente.id,
                                                                         'cod_pagamento': self.id, })
                           if i == 1:
                               param_po = self.env['parametros.parametros'].search([('variavel', '=', 'codPoupanca')])
                               cod_comp_po = self.env['compras.compras'].search([('codigo', '=', param_po.valor)])
                               num_cheq = self.n_cheque
                               new_det_lan_pret = self.env['detalhe.lancamento']  # A linha do valor OP
                               det_lanca_pret = new_det_lan_pret.create({'codigo_conta': cod_comp_po.conta_id.id,
                                                                         'descritivo': 'Poupança Credito Nº ' + str(
                                                                             num_cheq) + 'Pagamento de OP',
                                                                         'deb_cred': 'C',
                                                                         'valor_credito': self.valor_total_pag,
                                                                         'terceiro_id_doc_conta_corente_receb': self.terceiro_id_doc_conta_corente.id,
                                                                         'cod_pagamento': self.id, })
                           i += 1
                   else:

                       param = self.env['parametros.parametros'].search([('variavel', '=', 'codDesembolso')])
                       cod_comp = self.env['compras.compras'].search([('codigo', '=', param.valor)])
                       new_det_lan = self.env['detalhe.lancamento']  # A linha do valor Desemolso
                       det_lanca = new_det_lan.create({
                           'codigo_conta': cod_comp.conta_id.id,
                           'descritivo': 'Desembolso Credito Nº ' + str(num_cred),
                           'deb_cred': 'D',  # 'codigo_entidade': self.cod_terceiro,
                           'cod_pagamento': self.id,
                           'valor_credito': self.valor_total_pag,
                           'terceiro_id_doc_conta_corente_receb': self.terceiro_id_doc_conta_corente.id, })


                       param_c = self.env['parametros.parametros'].search([('variavel', '=', 'codComicao')])
                       cod_comp_c = self.env['compras.compras'].search([('codigo', '=', param_c.valor)])
                       num_cheq = self.n_cheque
                       new_det_lan_pret = self.env['detalhe.lancamento']  # A linha do valor OP
                       det_lanca_pret = new_det_lan_pret.create({'codigo_conta': cod_comp_c.conta_id.id,
                                                                 'descritivo': 'Comição de Credito ' + str(
                                                                     num_cheq) + 'Pagamento de OP',
                                                                 'deb_cred': 'C',
                                                                 'valor_credito': self.valor_total_pag,
                                                                 'terceiro_id_doc_conta_corente_receb': self.terceiro_id_doc_conta_corente.id,
                                                                 'cod_pagamento': self.id, })

        elif self.documentot == '2':
            param = self.env['parametros.parametros'].search([('variavel', '=', 'codDesembolso')])
            cod_comp = self.env['compras.compras'].search([('codigo', '=', param.valor)])
            new_det_lan = self.env['detalhe.lancamento']
            det_lanca = new_det_lan.create({
                'codigo_conta': cod_comp.conta_id.id,
                'descritivo': self.det_obs_doc_tesora,
                'deb_cred': 'D',
                'cod_pagamento': self.id,
                'valor_credito': self.valor_total_pag,
                'terceiro_id_doc_conta_corente_receb': self.terceiro_id_doc_conta_corente.id, })
            for l in self.documentoTesoraria_ids:
                new_det_lan = self.env['detalhe.lancamento']
                det_lanca = new_det_lan.create({
                    'codigo_conta': l.conta_id.id,
                    'descritivo': l.desc_conce_compra,
                    'deb_cred': 'C',
                    'cod_pagamento': self.id,
                    'valor_credito': l.valor,
                    'terceiro_id_doc_conta_corente_receb': self.terceiro_id_doc_conta_corente.id, })

        lanca = self.env['lancamento_diario.lancamento_diario'].search([('id', '>=', 1)])
        if lanca:
            for l in lanca:
                det_lanc = self.env['detalhe.lancamento'].search([('cod_pagamento', '=', l.cod_pagamento)])
                for dl in det_lanc:
                    dl.lancamento_diario = l.id

    def create_movimento(self):
        if self.origem == True:
           raise ValidationError('Este documento ja foi lançado')
        mov = self.env['pagamento.recebimento']
        movimentos = mov.create({'tipo_pagamento_receb': self.tipo_pagamento_receb, 'n_cheque': self.n_cheque,
                                 'nossa_conta_compras': self.nossa_conta_compras.id, 'data': self.data,
                                 'type_docum': self.type_docum,
                                 'terceiro_id_doc_conta_corente': self.terceiro_id_doc_conta_corente.id,
                                 'documentot': self.documentot,
                                 'contabilizado': self.contabilizado, 'diario': self.diario, 'numero': self.numero,
                                 'n_pagam': self.n_pagam,
                                 'valor_pag': self.valor_total_pag, 'montante_pago': self.montante_pago,
                                 'detalhes': self.detalhes, 'pagamento_id': self.id})
        return movimentos

    def _comput_line(self, line):
        return {'displlay_type': line.displlay_type, 'state': 'draft', }

    @api.multi
    @api.onchange('terceiro_id_doc_conta_corente')
    def _onchange_reg_docum_pag_ids(self):
        if self.type_docum == 'pagamento':
            if self.documentot == '2':
                pass
            else:
                docum = self.env['reg.docum'].search(
                    [('nome_terc', '=', self.terceiro_id_doc_conta_corente.id),  # ('saldo', '!=', 0),
                     ('control_estad_docum', '!=', 'ordenado'), ('desting_doc_desp', '=', True),
                     ('pagado_completo', '=', False),  # ('pago', '=', False),
                     ('encont_docum_desp', '=', False), ('renegociado', '=', False)])
                list_of_docum = []
                for line in docum:
                    data = self._comput_line(line)
                    data.update(
                        {'data_documento': line.data_documento, 'movimen_docum': line.movimen_docum,
                         'tipo_docum': line.tipo_docum, 'encont_docum_desp': line.encont_docum_desp,
                         'numeros_docum': line.numeros_docum, 'cod_documento': line.cod_documento,
                         'nome_terc': line.nome_terc, 'valorAsc': line.valorAsc,
                         'saldo_ord': line.saldo_ord, 'saldar': line.saldar,
                         'valor_encontro': line.valor_encontro, 'valorreceb': line.valorreceb,
                         'encont_docum_client': line.encont_docum_client, 'credito': line.credito,
                         'total': line.total, 'valorPago': line.valorPago, 'ldocaut': line.ldocaut,
                         'valor_ordpag': line.valor_ordpag, 'encontro': line.encontro,
                         'saldo': line.saldo, 'sequence': line.sequence, 'ordem_pago': line.ordem_pago,
                         'control_op': line.control_op, 'desting_doc_op': line.desting_doc_op,
                         'pago': line.pago, 'documentos': line.documentos, 'data_realise': line.data_realise,
                         'desting_doc_desp': line.desting_doc_desp, 'debito': line.debito,
                         'visualizar_no_tesorer': line.visualizar_no_tesorer, 'docPag': line.docPag,
                         'sem_cta_cte': line.sem_cta_cte})
                    list_of_docum.append((1, line.id, data))
                return {'value': {"det_reg_docum_ids": list_of_docum}}


    @api.multi
    @api.onchange('origem')#Add valores na lista
    def most_list_doc(self):
        if self.origem == True:
            if self.documentot == '2':
               det = self.env['documento.tesoraria.pagamento'].search([('origem', '=', True)])
               list_of_docum = []
               for line in det:
                   data = self._comput_line(line)
                   data.update(
                       {'conceit_compra_id': line.conceit_compra_id.id, 'desc_conce_compra': line.desc_conce_compra,
                        'cod_dp': line.cod_dp.id, 'valor': line.valor, 'iva': line.iva.id, 'terceiro': line.terceiro.id,})
                   list_of_docum.append((1, line.id, data))

               return {'value': {"documentoTesoraria_ids": list_of_docum}}
            if self.documentot == '1':
                det_reg = self.env['reg.docum'].search([('origem', '=', True)])
                list_docum = []
                for l in det_reg:
                    data = self._comput_line(l)
                    data.update(
                        {'cod_documento':l.cod_documento, 'total': l.total, 'saldo_pagamento': l.saldo_pagamento,
                         'docPag':l.docPag, 'data_documento': l.data_documento, 'valorPago': l.valorPago})
                    list_docum.append((1, l.id, data))

                return {'value': {"det_reg_docum_ids_contab": list_docum}}


    @api.one  # Adicionar Valor detalhes
    @api.depends('det_reg_docum_ids_contab.cod_documento')
    def add_detal(self):
        if self.type_docum == 'pagamento':
            if self.documentot != '2':
                # documreg = self.env['reg.docum'].search(
                #    [('nome_terc', '=', self.terceiro_id_doc_conta_corente.id),  # ('saldo', '!=', 0),
                #     ('control_estad_docum', '!=', 'ordenado'), ('desting_doc_desp', '=', True), ('pago', '=', False),
                #     ('encont_docum_desp', '=', False)])

                list_docum = []
                for line in self.det_reg_docum_ids_contab:
                    if line.docPag == True:
                        if not list_docum:
                            detalhes = 'Pagamento de ' + str(line.cod_documento) + ','
                            list_docum.append(detalhes)
                        else:
                            detalhes = str(line.cod_documento) + ','
                            list_docum.append(detalhes)
                a = " ".join(list_docum)
                self.detalhes = a

            else:
                self.detalhes = 'Documento Tesouraria' + str(self.n_pagam)

        else:
            pass
            # if self.movimento != '':
            #   self.detalhes = 'Transferência. '

    @api.one
    @api.depends('det_reg_docum_ids_contab.valorPago', 'saldo', 'documentoTesoraria_ids')
    def _compute_val_tot(self):
           if self.type_docum == 'pagamento':
               if self.documentot != '2':
                   self.valor_total_pag = sum(line.valorPago for line in self.det_reg_docum_ids_contab)
                   self.montante_pago = self.valor_total_pag
               else:
                   self.valor_total_pag = sum(line.valor for line in self.documentoTesoraria_ids)
                   self.montante_pago = self.valor_total_pag


    @api.onchange('valor_total_pag')
    def _tchek_val_tot(self):
        if self.tipo_pagamento_receb == '1':
            meios = self.env['monetario.monetario'].search([('name', '=', 'CAIXA PRINCIPAL')])
            self.saldo = meios.saldo_inicial

        if self.valor_total_pag > self.saldo:  # or self.saldo == 0
            raise ValidationError('ERRO! SALDO INSUFICIENTE.')

    @api.one
    def valida_pessoa(self):
        if self.type_docum == 'pagamento':

            ver_pessoa = self.env['reg.docum'].search([('pagado_completo', '=', False), ('desting_doc_desp', '=', True),
                                                       ('nome_terc', '=', self.terceiro_id_doc_conta_corente.id),
                                                       ('aprovado', '=', 'True'), ('renegociado', '=', False), ])
            if ver_pessoa:
                valid = self.env['reg.docum'].search(
                    [('pagado_completo', '=', False), ('desting_doc_desp', '=', True), ('renegociado', '=', False),
                     ('docPag', '=', False),
                     ('nome_terc', '=', self.terceiro_id_doc_conta_corente.id),
                     ('aprovado', '=', 'True'), ])
                for ver in valid:
                    ver.pagamento_id = 0  # pass desvincular os documento não pagos
                for doc in self.reg_docum_ids:
                    if doc.docPag == True:
                        doc.recebido_completo = True
            else:
                pessoap = self.env['pessoas'].search(
                    [('id', '=', self.terceiro_id_doc_conta_corente.id), ('tem_despesas', '=', True)])
                for pp in pessoap:
                    pp.tem_despesas = False

                pessoa_clientp = self.env['terceiro.terceiro'].search(
                    [('id', '=', self.terceiro_id_doc_conta_corente.id), ('tem_despesas', '=', True)])
                for pcp in pessoa_clientp:
                    pcp.tem_despesas = False

                plano_obj_op = self.env['reg.docum'].search(
                    [('prest_zerro', '=', True), ('renegociado', '=', False), ('estado', '=', '1')])
                for p in plano_obj_op:
                    p.cobrado = True
                    p.recebido_completo = True
                    p.pagado_completo = True
                    p.write({'estado': '3'})
                ver_doc = self.env['reg.docum'].search([('ata_id', '=', self.ata_id), (
                'prest_zerro', '=', True)])  # não esta corecto o campo ata_id nao servi
                if ver_doc:
                    for v in ver_doc:
                        v.fechado = True
                        v.write({'estado': '3'})
                docum_op = self.env['tesouraria.ordem.pagamento'].search([('ata_id', '=', self.ata_id), (
                'estado', '=', '1')])  # não esta corecto o campo ata_id nao servi para isso
                if docum_op:
                    for d in ver_doc:
                        d.write({'estado': '2'})

            # Aque decrimenta saldo
            if self.tipo_pagamento_receb != '1':
                meios = self.env['monetario.monetario'].search([('id', '=', self.nossa_conta_compras.id)])
                if not meios:
                    raise ValidationError('Esta conta não existe!')
                else:
                    for lin in meios:
                        lin.saldo_inicial -= self.valor_total_pag
            elif self.tipo_pagamento_receb == '1':
                meios = self.env['monetario.monetario'].search([('name', '=', 'CAIXA PRINCIPAL')])
                if not meios:
                    raise ValidationError('Não existe conta com nome CAIXA PRINCIPAL!')
                else:
                    for lin in meios:
                        lin.saldo_inicial -= self.valor_total_pag


class documentoTesorariaPagamento(models.Model):
    _name = 'documento.tesoraria.pagamento'
    # _rec_name = 'name'
    _description = 'Detalhes Documento de Tesouraria'
    conceit_compra_id = fields.Many2one('compras.compras', string='Codigo')
    conta_id = fields.Many2one('planconta.planconta', string='Conta', related="conceit_compra_id.conta_id")
    desc_conce_compra = fields.Char(string="Descrição", store=True, related='conceit_compra_id.name')  # , related='conceit_compra_id.name'
    cod_dp = fields.Many2one('organizacao.organizacao', string='Cod.Dep')
    valor = fields.Float(string='Valor')
    iva = fields.Many2one('iva.iva', string='IVA')
    terceiro = fields.Many2one('terceiro.terceiro', string='Terceiro')
    pagamento_id = fields.Many2one('tesouraria.pagamento', string="Pagamento")
    doc_tesou_pagamento_id = fields.Many2one('pagamento.recebimento', string="Pagamento", store=True)
    displlay_type = fields.Selection([('line_section', 'section'), ('line_note', 'nota')], string='displlay')
    state = fields.Selection([('draft', 'Draft'), ('open', 'Open'), ('paid', 'Paid'), ('cancel', 'Cancelled'), ],
                             string='Status', index=True, readonly=True, default='draft', track_visibility='onchange',
                             copy=False)
    origem = fields.Boolean(string="Origem da contabilidade")

    CDOCINT = fields.Char()
    CCODART = fields.Char()
    COTRTER = fields.Char()

    # CDESART = fields.Char()

    def mod_det(self):
        # tes_pag = self.env['tesouraria.pagamento'].search([('documentot', '=', '2')])
        # for c in tes_pag:
        #     cod = str(c.CMOVINT)
        #     if cod.isnumeric() == True:
        #        det = self.env['documento.tesoraria.pagamento'].search([('CDOCINT', '=', c.CMOVINT)])
        #        for d in det:
        #             d.pagamento_id = c.id

        tes_pag = self.env['pagamento.recebimento'].search([('documentot', '=', '2')])
        for c in tes_pag:
            cod = str(c.CMOVINT)
            if cod.isnumeric() == True:
                det = self.env['documento.tesoraria.pagamento'].search([('CDOCINT', '=', c.CMOVINT)])
                for d in det:
                    d.doc_tesou_pagamento_id = c.id

    def mod_det_lig_terc(self):
        ter = self.env['terceiro.terceiro'].search([('mud_id', '=', True)])
        for c in ter:
            det = self.env['documento.tesoraria.pagamento'].search([('COTRTER', '=', c.codigo)])
            for d in det:
                d.terceiro = c.id

    @api.one
    @api.depends('pagamento_id')
    def add_id(
            self):  # esta função liga o documento da tesouraria com a tabela pagamento_recebimento para que a folgha de tesouraria pode ver
        self.doc_tesou_pagamento_id = self.pagamento_id.id
