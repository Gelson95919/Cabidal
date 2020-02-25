# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class lancamentoDiario(models.Model):
    _name = 'lancamento_diario.lancamento_diario'
    _rec_name = 'cod_pagamento'
    _description = 'Lançamento'
    name = fields.Char()
    terceiro_id_doc_conta_corente_receb = fields.Many2one('terceiro.terceiro', string='Terceiro', store=True)
    codigo = fields.Char(string='Doc.', copy=False, readonly=True, index=True, default=lambda self: _('New')) #required=True,
    diario = fields.Many2one('diario.diario', string='Diario')
    name_diario = fields.Char('Descrição', related='diario.name')
    data = fields.Date(string='Data')
    ordem = fields.Char(string='Ordem', store=True)# related="diario.numero_documento_inicial",
    valor = fields.Integer(string='Valor')
    valor1 = fields.Integer(string='Valor')
    obs = fields.Text(string='OBS')
    debito = fields.Float(string="Debito")
    credito = fields.Float(string="Credito")
    conta_d = fields.Many2one('planconta.planconta', readonly=True, store=True, domain=[('grupo', '=', False)])#, related="centro_custo.nome"
    nome_conta = fields.Char('Descrição', related="conta_d.nome")
    codigo_conta = fields.Char('Conta', related="conta_d.cod_plan_cont")
    cen_cust_d = fields.Char(string='Centrd Custo', readonly=True, store=True)#, related="centro_custo.nome"
    entidade_d = fields.Char(string='Entidade', readonly=True, store=True, related="terceiro_id_doc_conta_corente_receb.name")#
    cod_terce = fields.Char(string='Terce', readonly=True, store=True, related="terceiro_id_doc_conta_corente_receb.codigo")#

    fluxo_d = fields.Char(string='Fluxo', readonly=True, store=True)#, related="fluxo_caixa.nome"
    tipo_doc_d = fields.Char(string='Tipo Documento', readonly=True)
    moeda_d = fields.Char(string='Moeda', readonly=True, store=True)#related="moeda_estra.name",
    codigo_d = fields.Char(string='Codigo', readonly=True)
    linha_auto = fields.Boolean(string='Linha Automat.')
    lancamento_id = fields.One2many('detalhe.lancamento', 'lancamento_diario')
    cod_recebmento = fields.Integer(string="Codigo Recebimento")
    cod_pagamento = fields.Integer(string="Codigo Pagamento")
    cod_movint = fields.Integer(string="Codigo Pagamento")
    atualizado = fields.Boolean(string="Actualizado")
    dfecpag = fields.Char()
    diamov = fields.Char(string="Dia")
    mesmov = fields.Char(string="Mês")
    anomov = fields.Char(string="Ano")
    dados_antigo = fields.Boolean(string="Dados Antigo")
    tipo_movimento = fields.Selection(
        [('1', 'Pagamento'), ('2', 'Recebimento'), ('3', 'Movimento Interno')], store=True, string='Documento', Widget="radio",)
    ver_contab = fields.Boolean(string="Origem da contabilidade")
    consult_extrat_id = fields.Many2one('consulta.extracto', string="Consulta extrato")

    displlay_type = fields.Selection([('line_section', 'section'), ('line_note', 'nota')], string='displlay')
    state = fields.Selection([('draft', 'Draft'), ('open', 'Open'), ('paid', 'Paid'), ('cancel', 'Cancelled'), ],
                             string='Status', index=True, readonly=True, default='draft', track_visibility='onchange',
                             copy=False)

    @api.model
    def create(self, vals):
        vals['codigo'] = self.env['ir.sequence'].next_by_code('lancamento.codigo') or _('New')
        res = super(lancamentoDiario, self).create(vals)

        return res

    def _comput_line(self, line):
        return {'displlay_type': line.displlay_type, 'state': 'draft', }
    @api.multi
    @api.onchange('data')
    def valida_period(self):
        dat = ''
        if self.data:
          dat = self.data
        d = str(dat)
        if d != "":
           x = d.split('-')
           datefec = x
           list = []
           for a in datefec:
               list.append(a)
           anomov = list[0]
           p = self.env['periodo.periodo'].search([('fecho', '=', False)])
           if anomov != p.codigo:
               warning = {
                   'title': _('ERRO!'),
                   'message': _('Data de um periodo não definido'),
               }
               return {'warning': warning}

    def origem(self):
        if self.tipo_movimento == '1':
            det = self.env['documento.tesoraria.pagamento'].search([('origem', '=', True)])
            for l in det:
                l.origem = False
            det_reg = self.env['reg.docum'].search([('origem', '=',True)])
            for r in det_reg:
                r.origem = False
            tipo_pagamento_receb = False
            n_cheque = False
            nossa_conta_compras = False
            data = False
            terceiro_id_doc_conta_corente = False
            documentot = False
            reg_docum_ids = False
            documentoTesoraria_ids = False
            n_pagam = False
            contabilizado = False
            diario = False
            detalhes = False
            det_obs_doc_tesora = False
            valor_total_pag = False

            pag = self.env['tesouraria.pagamento'].search([('id', '=', self.cod_pagamento)])

            if pag.documentot == '2':
               det = self.env['documento.tesoraria.pagamento'].search([('pagamento_id', '=', pag.id)])
               for l in det:
                   l.origem = True
            else:
                det_reg = self.env['reg.docum'].search([('pagamento_id', '=', pag.id)])
                for r in det_reg:
                    r.origem = True
            ac = self.env['ir.model.data'].xmlid_to_res_id('gestao_tesouraria.pagamento_form',
                                                           raise_if_not_found=True)

            if pag:
                for dad in pag:

                    tipo_pagamento_receb = dad.tipo_pagamento_receb
                    n_cheque = dad.n_cheque
                    nossa_conta_compras = dad.nossa_conta_compras
                    data = dad.data
                    terceiro_id_doc_conta_corente = dad.terceiro_id_doc_conta_corente
                    documentot = dad.documentot#(line.taxa for line in self.fatura_linha_ids)
                    reg_docum_ids = dad.reg_docum_ids
                    documentoTesoraria_ids = dad.documentoTesoraria_ids
                    n_pagam = dad.n_pagam
                    contabilizado = dad.contabilizado
                    diario = dad.diario
                    detalhes = dad.detalhes
                    det_obs_doc_tesora = dad.det_obs_doc_tesora
                    valor_total_pag = dad.valor_total_pag
                result = {
                    'name': 'Pagamento',
                    'view_type': 'form',
                    'res_model': 'tesouraria.pagamento',
                    'view_id': ac,
                    'context': {
                        'default_tipo_pagamento_receb': tipo_pagamento_receb,
                        'default_n_cheque': n_cheque,
                        'default_nossa_conta_compras': nossa_conta_compras.id,
                        'default_data': data,
                        'default_terceiro_id_doc_conta_corente': terceiro_id_doc_conta_corente.id,
                        'default_documentot': documentot,
                        #'default_reg_docum_ids': reg_docum_ids,
                        #'default_documentoTesoraria_ids': documentoTesoraria_ids,#{'value': {"documentoTesoraria_ids": list_det_pag}},
                        'default_origem': True,
                        'default_contabilizado': contabilizado,
                        'default_n_pagam': n_pagam,
                        'default_detalhes': detalhes,
                        'default_det_obs_doc_tesora': det_obs_doc_tesora,
                        'default_diario': diario.id,
                        'default_valor_total_pag': valor_total_pag,
                        },
                    'type': 'ir.actions.act_window',
                    'target': 'new',
                    'view_mode': 'form'
                }
                return result


        elif self.tipo_movimento == '2':
             det = self.env['documento.tesoraria.recebimento'].search([('origem', '=', True)])
             for l in det:
                 l.origem = False
             det_reg = self.env['reg.docum'].search([('origem', '=', True)])
             for r in det_reg:
                 r.origem = False
             terceiro_id_doc_conta_corente_receb = False
             documentot = False
             tipo_pagamento_receb = False
             n_cheque = False
             nossa_conta = False
             data = False
             banco = False
             refe = False
             n_recibo = False
             conta_caicha = False
             reg_docum_ids_receb = False
             reg_docum_ids = False
             contabilizado = False
             diario = False
             detalhes = False
             det_obs_doc_tesora = False

             receb = self.env['tesouraria.recebimento'].search([('id', '=', self.cod_recebmento)])
             ac = self.env['ir.model.data'].xmlid_to_res_id('gestao_tesouraria.recebimento_form',
                                                            raise_if_not_found=True)


             if receb.documentot == '2':
                 det = self.env['documento.tesoraria.recebimento'].search([('recebimento_id', '=', receb.id)])
                 for l in det:
                     l.origem = True
             else:
                 det_reg = self.env['reg.docum'].search([('recebimento_id', '=', receb.id)])
                 for r in det_reg:
                     r.origem = True
             if receb:
                 for dad in receb:
                     terceiro_id_doc_conta_corente_receb = dad.terceiro_id_doc_conta_corente_receb.id
                     documentot = dad.documentot
                     tipo_pagamento_receb = dad.tipo_pagamento_receb
                     n_cheque = dad.n_cheque
                     nossa_conta = dad.nossa_conta.id
                     data = dad.data
                     banco = dad.banco.id
                     refe = dad.refe
                     conta_caicha = dad.conta_caicha
                     n_recibo = dad.n_recibo
                     reg_docum_ids_receb = dad.reg_docum_ids_receb
                     reg_docum_ids = dad.reg_docum_ids
                     contabilizado = dad.contabilizado
                     det_obs_doc_tesora = dad.det_obs_doc_tesora
                     diario = dad.diario
                     detalhes = dad.detalhes
                 result = {
                     'name': 'Recebimento',
                     'view_type': 'form',
                     'res_model': 'tesouraria.recebimento',
                     'view_id': ac,
                     'context': {
                         'default_tipo_pagamento_receb': tipo_pagamento_receb,
                         'default_terceiro_id_doc_conta_corente_receb': terceiro_id_doc_conta_corente_receb,
                         'default_documentot': documentot,
                         'default_n_cheque': n_cheque,
                         'default_nossa_conta': nossa_conta,
                         'default_data': data,
                         'default_banco': banco,
                         'default_refe': refe,
                         'default_n_recibo': n_recibo,
                         'default_conta_caicha': conta_caicha,
                         'default_origem': True,
                         #'default_reg_docum_ids_receb': reg_docum_ids_receb,
                         #'default_reg_docum_ids': reg_docum_ids,
                         'default_contabilizado': contabilizado,
                         'default_det_obs_doc_tesora': det_obs_doc_tesora,
                         'default_diario': diario,
                         'default_detalhes': detalhes,

                     },
                     'type': 'ir.actions.act_window',
                     'target': 'new',
                     'view_mode': 'form'
                 }
                 return result

        elif self.tipo_movimento == '3':
            n_movimento = False
            movimento = False
            date_release = False
            dfecmovint = False
            centro_custo = False
            detalhes = False
            nossa_conta_transfe = False
            saldo_transf = False
            montante_mov = False
            cheque = False
            esc = False
            diario = False
            contabilizado = False
            numero = False
            conta_destino = False
            escd = False
            contabilizadod = False
            diariod = False
            numerod = False
            mov = self.env['pagamento.recebimento'].search([('id', '=', self.cod_movint)])
            ac = self.env['ir.model.data'].xmlid_to_res_id('gestao_tesouraria.movimento_int_form',)
            if mov:
                for dad in mov:
                    n_movimento = dad.n_movimento
                    movimento = dad.movimento.id
                    date_release = dad.date_release
                    dfecmovint = dad.dfecmovint
                    centro_custo = dad.centro_custo.id
                    detalhes = dad.detalhes
                    nossa_conta_transfe = dad.nossa_conta_transfe.id
                    saldo_transf = dad.saldo_transf
                    montante_mov = dad.montante_mov
                    cheque = dad.cheque
                    esc = dad.esc
                    diario = dad.diario
                    contabilizado = dad.contabilizado
                    numero = dad.numero
                    conta_destino = dad.conta_destino.id
                    escd = dad.escd
                    contabilizadod = dad.contabilizadod
                    diariod = dad.diariod
                    numerod = dad.numerod
                result = {
                        'name': 'Movimento Interno',
                        'view_type': 'form',
                        'res_model': 'tesouraria.movimento.interno',
                        'view_id': ac,
                        'context': {
                            'default_n_movimento': n_movimento,
                            'default_movimento': movimento,
                            'default_date_release': date_release,
                            'default_dfecmovint': dfecmovint,
                            'default_centro_custo': centro_custo,
                            'default_detalhes': detalhes,
                            'default_nossa_conta_transfe': nossa_conta_transfe,
                            'default_saldo_transf': saldo_transf,
                            'default_montante_mov': montante_mov,
                            'default_cheque': cheque,
                            'default_esc': esc,
                            'default_diario': diario,
                            'default_contabilizado': contabilizado,
                            'default_numero': numero,
                            'default_conta_destino': conta_destino,
                            'default_escd': escd,
                            'default_origem': True,
                            'default_contabilizadod': contabilizadod,
                            'default_diariod': diariod,
                            'default_numerod': numerod,

                             },
                        'type': 'ir.actions.act_window',
                        'target': 'new',
                        'view_mode': 'form'

                    }
                return result


    @api.multi
    @api.onchange('ver_contab')  # Add valores na lista
    def most_list_doc(self):
        if self.ver_contab == True:
                det_reg = self.env['detalhe.lancamento'].search([('ver_contab', '=', True)])
                list_docum = []
                for l in det_reg:
                    data = self._comput_line(l)
                    data.update(
                        {'codigo_conta': l.codigo_conta.id, 'deb_cred': l.deb_cred, 'descricao_conta': l.descricao_conta,
                         'centro_custo': l.centro_custo, 'codigo_entidade': l.codigo_entidade, 'fluxo_caixa': l.fluxo_caixa,
                         'valor_credito': l.valor_credito, 'codigo_iva': l.codigo_iva.id, 'valor_moeda_estra': l.valor_moeda_estra.id})
                    list_docum.append((1, l.id, data))
                return {'value': {"lancamento_id": list_docum}}




class detLanc(models.Model):
    _name = 'detalhe.lancamento'
    #_rec_name = 'name'
    _description = 'Detalhes Lançamento'
    #name = fields.Char()

    codigo_conta = fields.Many2one('planconta.planconta', string='Código Conta', domain=[('grupo', '=', False)])
    deb_cred = fields.Char(string='Deb/Cred')
    descritivo = fields.Char(string='Descritivo')
    descricao_conta = fields.Char(string='Descrição conta', related="codigo_conta.nome")
    centro_custo = fields.Many2one('planteso.planteso', string='Centro Custo')
    codigo_entidade = fields.Char(string='Codigo Entidade',)

    fluxo_caixa = fields.Many2one('planteso.planteso', string='Fluxo Caixa')
    valor_credito = fields.Integer(string='Valor')#Valor de debito e de credito
    codigo_iva = fields.Many2one('iva.iva', string='Código IVA')
    valor_moeda_estra = fields.Many2one('moeda.moeda', string='Valor Moeda Estrangeira')
    moeda_estra = fields.Many2one('moeda.moeda', string='Moeda Estrangeira')
    terceiro_id_doc_conta_corente_receb = fields.Many2one('terceiro.terceiro', string='Terceiro')
    lancamento_diario = fields.Many2one('lancamento_diario.lancamento_diario', string="ID Lançamento")
    cod_recebmento = fields.Integer(string="Codigo Recebimento")
    cod_pagamento = fields.Integer(string="Codigo Pagamento")
    cod_movint = fields.Integer(string="Codigo Pagamento")
    ver_contab = fields.Boolean(string="Origem da contabilidade")
    displlay_type = fields.Selection([('line_section', 'section'), ('line_note', 'nota')], string='displlay')
    state = fields.Selection([('draft', 'Draft'), ('open', 'Open'), ('paid', 'Paid'), ('cancel', 'Cancelled'), ],
                             string='Status', index=True, readonly=True, default='draft', track_visibility='onchange',
                             copy=False)
    leva_terce = fields.Boolean(string="Leva Terceiro", related='codigo_conta.leva_terce')
    leva_moeda_estrangeira = fields.Boolean(string='Leva Moeda Estrangeira', related='codigo_conta.leva_moeda_estrangeira')
    leva_centro_custo = fields.Boolean(string='Leva Centro Custo', related='codigo_conta.leva_centro_custo')
    lev_fluxo_caixa = fields.Boolean(string='Fluxo Caixa', related='codigo_conta.fluxo_caixa')
    control_IVA = fields.Boolean(string='Control IVA', related='codigo_conta.control_IVA')

    @api.model
    def create(self, vals):
        # vals['movimento'] = self.env['ir.sequence'].next_by_code('folha.tesouraria.mov') or _('New')
        res = super(detLanc, self).create(vals)
        return res

    @api.multi
    @api.onchange('leva_terce')
    def add_entidade(self):
        if self.leva_terce == True:
            ent = self.env['terceiro.terceiro'].search([('id', '=', self.terceiro_id_doc_conta_corente_receb.id)])
            self.codigo_entidade = ent.codigo