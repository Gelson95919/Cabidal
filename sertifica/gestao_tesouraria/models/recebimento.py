# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo.exceptions import ValidationError
import datetime

class tesourariaRecebimento(models.Model):
     _name = 'tesouraria.recebimento'
     _description = 'Recebimento'
     _order = 'id desc'
     terceiro_id_doc_conta_corente_receb = fields.Many2one('terceiro.terceiro', string='Cliente', required=True,)#, domain=[('tem_solicitacao', '=', '1')]
     nome_cliente = fields.Char(string='Cliente', related="terceiro_id_doc_conta_corente_receb.name", store=True,
                                readonly=True)
     nif_cliente = fields.Integer(string="Nif", related="terceiro_id_doc_conta_corente_receb.nif")#para remover
     nif_pessoa = fields.Char(string="NIF", related="terceiro_id_doc_conta_corente_receb.nif_pessoa", store=True)

     documentot = fields.Selection(
          [('1', 'Documento Conta Corrente'),
           ('2', 'Documento de Tesouraria')],
          'Documento', Widget="radio", default='1')
     tipo_pagamento_receb = fields.Selection(
          [('1', 'Dinheiro'),
           ('2', 'Cheque'),
           ('3', 'Transferência'), ('4', 'Deposito')],
          'Tipo', required=True, default='1', store=True)
     type_docum = fields.Selection(
          [('recebimento', 'Recebimento'), ('pagamento', 'Pagamento'), ('movimento', 'Movimento')], readonly=True,
          index=True, change_default=True, default=lambda self: self._context.get('type_docum', 'recebimento'),
          track_visibility='always', store=True)

     n_cheque = fields.Char(string='Numero Cheque')
     nossa_conta = fields.Many2one('monetario.monetario', string='Nossa Conta', domain="[('tipo_meio','=','2')]")#

     codigo_conta = fields.Many2one('planconta.planconta', string='Código Conta', related='nossa_conta.conta')
     leva_terce = fields.Boolean(string='Leva Terceiro', related='codigo_conta.leva_terce')
     centro_custo = fields.Many2one('planteso.planteso', string='Centro Custo', related='nossa_conta.centro_custo')
     codigo_entidade = fields.Many2one('entbanc.entbanc', string='Codigo Entidade')
     fluxo_caixa = fields.Many2one('planteso.planteso', string='Fluxo Caixa')
     codigo_iva = fields.Many2one('iva.iva', string='Código IVA')
     valor_moeda_estra = fields.Many2one('moeda.moeda', string='Valor Moeda Estrangeira')
     moeda_estra = fields.Many2one('moeda.moeda', string='Moeda Estrangeira')


     data = fields.Date('Data')
     banco = fields.Many2one('entbanc.entbanc', string='Banco')
     conta_caicha = fields.Float(string='Conta Caixa')
     refe = fields.Char(string='Referência')
     n_recibo = fields.Char(string='Recebimento Nº', store=True, copy=False, readonly=True, index=True, default=lambda self: self._get_next_cod())
     reg_docum_ids_receb = fields.Many2many('reg.docum', string="Reg Docum", store=True, copy=True)# 'recebimento_id',
     reg_docum_ids = fields.One2many('reg.docum',  'recebimento_id', string="Reg Docum", store=True, copy=True)
     contabilizado = fields.Boolean(string='Contabilizado')
     diario = fields.Char(string='Diario', related='nossa_conta.codigo_diario')
     name_diario = fields.Char(string="Nome Diario", related="nossa_conta.name_diario")
     numero = fields.Char(string='Numero', related='nossa_conta.numero_documento_inicial')
     detalhes = fields.Char(string='Detalhes Documento', readonly=False, store=True, compute="add_detal",)#
     det_obs_doc_tesora = fields.Char(string="Detalhes")
     doc_teso = fields.One2many('documento.tesoraria.recebimento', 'recebimento_id', string='detalt',
                                oldname='detal_lin')
     descricao_conta = fields.Char(string="Descrição Conta", related="nossa_conta.name", )
     cod_cliente = fields.Char(string="Codigo", related="terceiro_id_doc_conta_corente_receb.codigo")
     tem_solicitacao = fields.Selection([('1', 'Sim'), ('2', 'Não')], string="Tem Fatura",
                                        related="terceiro_id_doc_conta_corente_receb.tem_solicitacao")

     nif = fields.Integer(string="Nif", related="terceiro_id_doc_conta_corente_receb.nif")#para remover
     telefone_fixo = fields.Integer(string="Telefone Fixo", related="terceiro_id_doc_conta_corente_receb.fax",
                                    store=True)#para remover
     telemovel = fields.Integer(string="Telemovel", related="terceiro_id_doc_conta_corente_receb.phone", store=True)#para remover


     nif_pessoareceb = fields.Char(string="NIF", size=9,
                                   related="terceiro_id_doc_conta_corente_receb.nif_pessoa")#
     telefone_pessoa = fields.Char(string="Telefone", size=7,
                                   related="terceiro_id_doc_conta_corente_receb.telefone_pessoa")#required=True,
     fixo_pessoa = fields.Char(string="Fax", size=7,
                               related="terceiro_id_doc_conta_corente_receb.fixo_pessoa")# required=True,

     select = fields.Boolean(string='select', default=True)  # vervalor_total_receb
     vervalor_total_receb = fields.Float(string='Entrada', store=True, copy=True, compute="_compute_val_tot")#, compute="_compute_val_tot",
     montante_receb = fields.Float(string="Montante", store=True, copy=True, compute="_compute_val_tot")#, compute="_compute_val_tot"
     date = fields.Date(string='Data', default=fields.Date.today)#, default=fields.Date.today
     tipo_meio = fields.Selection([('1', 'Caixa'), ('2', 'Desposto a Ordem'), ('3', 'Fundo de Maneio')],
                                  'Tipo', related="nossa_conta.tipo_meio", )
     street_cliente = fields.Char(string="Endereso Cliente", related="terceiro_id_doc_conta_corente_receb.street")
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)
     valor_saldo_total = fields.Float(string="Valor saldo Calculado", store=True, copy=True, compute="_compute_val_tot")#saldo para ser recebido
     resultado  = fields.Float(string="Valor Resultado", store=True, copy=True, compute="_compute_val_tot")#, compute="_compute_val_tot"
     por_partes = fields.Boolean(string="Por partes")
     ata_id = fields.Integer(string="ID Ata", related="terceiro_id_doc_conta_corente_receb.ata_id", store=True)#para ajudar no procedimento de receber
     cod_terceiro = fields.Char(string="Codigo", related="terceiro_id_doc_conta_corente_receb.codigo")

     dados_antigo = fields.Boolean(string="Dados Antigo")  # se True porque os dados são antigo
     tipo_movimento = fields.Selection(
         [('1', 'Pagamento'),
          ('2', 'Recebimento'), ('3', 'Movimento Interno')], store=True, string='Documento', Widget="radio",
         default='2')
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
     CNUMFEC = fields.Char()
     CCODMED = fields.Char()
     CMOVINT2 = fields.Integer()
     CNUMPAG = fields.Char()
     CCODTER = fields.Char()
     CNOMTER = fields.Char()
     CDETPAG = fields.Char()
     CNUMORD = fields.Char()
     DFECPAGDATPAG = fields.Char()

     dfecpag = fields.Char()
     cmovint = fields.Char()
     scmovint1 = fields.Integer()

     # 1111111111111111111111111111111111111111111111111111111111
     def compor_op(self):
         lanca = self.env['lancamento_diario.lancamento_diario'].search([('id', '>=', 1)])
         if lanca:
             for l in lanca:
                 det_lanc = self.env['detalhe.lancamento'].search([('cod_recebmento', '=', l.cod_recebmento)])
                 for dl in det_lanc:
                     dl.lancamento_diario = l.id
         #pass
         #pagamento = self.env['tesouraria.recebimento'].search([('id', '>=', 27806)])
         #for p in pagamento:
         #    if p.id <= 32806:
         #       docum = self.env['pagamento.recebimento'].search([('CMOVINT', '=', p.CMOVINT), ('type_docum', '=', 'recebimento')])
         #       for d in docum:
         #            d.CCODMED = p.CCODMED


         #teso_receb = self.env['tesouraria.recebimento'].search([('id', '<', 9949)])
         #for tp in teso_receb:
         #    if tp.id <= 9949:
         #        pagamento = self.env['pagamento.recebimento']
         #        pagam = pagamento.create({'nossa_conta': tp.nossa_conta.id,
         #                                  'terceiro_id_doc_conta_corente_receb': tp.terceiro_id_doc_conta_corente_receb.id,
         #                                  'banco': tp.banco,
         #                                  'conta_caicha': tp.conta_caicha,
         #                                  'refe': tp.refe,
         #                                  'n_recibo': tp.n_recibo,
         #                                  'vervalor_total_receb': tp.vervalor_total_receb,
         #                                  'vervalor_receb': tp.vervalor_total_receb,
         #                                  'montante_receb': tp.vervalor_total_receb,
         #                                  'recebimento_id': tp.id,
         #                                  'valor_saldo_total': tp.vervalor_total_receb,
         #                                  'detalhes': tp.detalhes,
         #                                  'tipo_pagamento_receb': tp.tipo_pagamento_receb,
         #                                  'documentot': tp.documentot,
         #                                  'diario': tp.diario,
         #                                  'type_docum': 'recebimento',
         #                                  'n_cheque': tp.n_cheque,
         #                                  'numero': tp.numero,
         #                                  'IDTERC': tp.IDTERC,
         #                                  'CMOVINT': tp.CMOVINT,
         #                                  'CMOVINT2': tp.CMOVINT2,
         #                                  'CNUMFEC': tp.CNUMFEC,
         #                                  'CNUMPAG': tp.CNUMPAG,
         #                                  'CCODTER': tp.CCODTER,
         #                                  'CNOMTER': tp.CNOMTER,
         #                                  'CDETPAG': tp.CDETPAG,
         #                                  'CNUMORD': tp.CNUMORD,
         #                                  'DFECPAGDATPAG': tp.DFECPAGDATPAG })


         #terc = self.env['terceiro.terceiro'].search([('clientes', '=', True)])
         #for c in terc:
         #    ord_p = self.env['tesouraria.recebimento'].search([('CCODTER', '=', c.codigo)])
         #    for o in ord_p:
         #        cod = str(o.terceiro_id_doc_conta_corente_receb.id)
         #        if (cod.isnumeric()) == False:
         #           o.terceiro_id_doc_conta_corente_receb = c.id


     def compor_por_int(self):
         #pass
         ct = self.env['pagamento.recebimento'].search([('id', '>=', 1)])
         for c in ct:
            cod = str(c.CNUMFEC)
            if cod.isnumeric() == True:
               c.cnumfec1 = c.CNUMFEC

        #terc = self.env['terceiro.terceiro'].search([('clientes', '=', True)])
        #for c in terc:
        #     ord_p = self.env['tesouraria.pagamento'].search([('CCODTER', '=', c.codigo)])
        #     for o in ord_p:
        #         o.terceiro_id_doc_conta_corente = c.id

     def mod_det(self):
         #pass
         regc = self.env['reg.caja'].search([('id', '>=', 32000)])
         for c in regc:
             if c.id <= 36930:
                 receb = self.env['pagamento.recebimento'].search([('CMOVINT2', '=', c.CMOVINT), ('type_docum', '=', 'recebimento')])
                 for d in receb:
                     d.CCODMED = c.CCODMED

         #regc = self.env['reg.caja'].search([('id', '>=', 35000)])
         #for c in regc:
         #    if c.id <= 37000:
         #        receb = self.env['tesouraria.pagamento'].search([('CMOVINT2', '=', c.CMOVINT)])
         #        for d in receb:
         #            d.CCODMED = c.CCODMED

         #regc = self.env['reg.caja'].search([('id', '>=', 35000)])
         #for c in regc:
         #    if c.id <= 37000:
         #        receb = self.env['tesouraria.pagamento'].search([('CMOVINT2', '=', c.CMOVINT)])
         #        for d in receb:
         #            d.CNUMFEC = c.CNUMFEC

     @api.model
     def _get_next_cod(self):
          sequence_np = self.env['ir.sequence'].search([('code', '=', 'recebimento.num')])
          next_np = sequence_np.get_next_char(sequence_np.number_next_actual)
          return next_np

     @api.model
     def create(self, vals):
          vals['n_recibo'] = self.env['ir.sequence'].next_by_code('recebimento.num')
          res = super(tesourariaRecebimento, self).create(vals)
          res.creat_doc_part()
          res.create_movimento()
          res.valida_pessoa()
          res.creat_det_lanc()

          return res

     def create_movimento(self):
          if self.origem == True:
              raise ValidationError('Este documento ja foi lançado')
          mov = self.env['pagamento.recebimento']
          movimentos = mov.create({'tipo_pagamento_receb': self.tipo_pagamento_receb, 'n_cheque': self.n_cheque,
                                   'nossa_conta': self.nossa_conta.id, 'data': self.data,
                                   'refe': self.refe, 'terceiro_id_doc_conta_corente_receb': self.terceiro_id_doc_conta_corente_receb.id,
                                   'banco': self.banco.id, 'documentot': self.documentot, 'conta_caicha': self.conta_caicha,
                                   'contabilizado': self.contabilizado, 'diario': self.diario, 'numero': self.numero,
                                   'n_recibo': self.n_recibo, 'type_docum':self.type_docum, 'valor_saldo_total':self.valor_saldo_total,
                                   'vervalor_receb': self.vervalor_total_receb, 'montante_receb': self.montante_receb,
                                   'detalhes': self.detalhes, 'recebimento_id': self.id})
          return movimentos

     @api.one
     @api.depends('reg_docum_ids.valorreceb', 'reg_docum_ids.saldo', 'valor_saldo_total', 'vervalor_total_receb')
     def _compute_val_tot(self):
         if self.documentot == '1':
             self.vervalor_total_receb = sum(line.valorreceb for line in self.reg_docum_ids)
             self.valor_saldo_total = sum(line.valor_saldo for line in self.reg_docum_ids)
             self.resultado = self.valor_saldo_total - self. vervalor_total_receb
             if self.resultado > 0:
                 self.por_partes = True
             else:
                 self.por_partes = False
             self.montante_receb = self.vervalor_total_receb
         else:
             self.vervalor_total_receb = sum(line.sub_total for line in self.doc_teso)
             self.montante_receb = self.vervalor_total_receb

     def _comput_line(self, line):
          return {'displlay_type': line.displlay_type, 'state': 'draft', }

     @api.multi
     @api.onchange('terceiro_id_doc_conta_corente_receb')
     def _onchange_reg_docum_receb_ids(self):
          if self.type_docum == 'recebimento':
               if self.documentot == '2':
                    pass
               else:
                    docum = self.env['reg.docum'].search(
                       [('nome_terc', '=', self.terceiro_id_doc_conta_corente_receb.id),  # ('saldo', '!=', 0),
                        ('desting_doc_vend', '=', True), ('aprovado', '=', 'True'), ('encont_docum_client', '=', False),
                        ('cobrado', '=', False), ('renegociado', '=', False)])
                    #if docum:
                    #    raise ValidationError('Opa')
                    list_of_docum = []
                    for line in docum:
                         data = self._comput_line(line)
                         data.update({'data_documento': line.data_documento, 'movimen_docum': line.movimen_docum,
                               'tipo_docum': line.tipo_docum, 'encont_docum_desp': line.encont_docum_desp,
                               'numeros_docum': line.numeros_docum, 'cod_documento': line.cod_documento,
                               'valor_encontro': line.valor_encontro, 'valorreceb': line.valorreceb,
                               'nome_terc': line.nome_terc, 'valorAsc': line.valorAsc,
                               'saldo_ord': line.saldo_ord, 'saldar': line.saldar,
                               'encont_docum_client': line.encont_docum_client,
                               'total': line.total, 'valorPago': line.valorPago, 'ldocaut': line.ldocaut,
                               'valor_ordpag': line.valor_ordpag, 'credito': line.credito, 'encontro': line.encontro,
                               'saldo': line.saldo, 'sequence': line.sequence, 'ordem_pago': line.ordem_pago,
                               'control_op': line.control_op, 'desting_doc_op': line.desting_doc_op,
                               'pago': line.pago, 'documentos': line.documentos, 'data_realise': line.data_realise,
                               'desting_doc_desp': line.desting_doc_desp, 'debito': line.debito, 'valor_saldo': line.valor_saldo,
                               'visualizar_no_tesorer': line.visualizar_no_tesorer, 'docPag': line.docPag,
                               'sem_cta_cte': line.sem_cta_cte})
                         list_of_docum.append((1, line.id, data))
                    return {'value': {"reg_docum_ids": list_of_docum}}


     @api.one  #Adicionar Valor detalhes
     @api.depends('reg_docum_ids.cod_documento')
     def add_detal(self):
        if self.type_docum == 'recebimento':
            if self.documentot != '2':
                 #docum = self.env['reg.docum'].search([('nome_terc', '=', self.terceiro_id_doc_conta_corente_receb.id),  # ('saldo', '!=', 0),
                 #     ('desting_doc_vend', '=', True), ('aprovado', '=', '1'), ('encont_docum_client', '=', False)])

                 list_docum = []
                 for line in self.reg_docum_ids:
                     if line.cobrado==True:
                         if not list_docum:
                            detalhes = 'Recebimento de ' + str(line.cod_documento) + ','
                            list_docum.append(detalhes)
                         else:
                             detalhes=str(line.cod_documento) + ','
                             list_docum.append(detalhes)
                 a = " ".join(list_docum)
                 self.detalhes = a

            else:
                 self.detalhes = 'Documento Tesouraria' + str(self.n_recibo)
        else:
            pass
            #if self.movimento != '':
            #   self.detalhes = 'Transferência. '


     @api.one
     def valida_pessoa(self):
         if self.type_docum == 'recebimento':
             ver_pessoa = self.env['reg.docum'].search([('cobrado', '=', False), ('renegociado', '=', False), ('nome_terc', '=', self.terceiro_id_doc_conta_corente_receb.id), ('aprovado', '=', 'True')])#, ('ata', '=', self.ata_id)
             if ver_pessoa:
                 for ver in ver_pessoa:
                     ver.recebimento_id = 0  #pass Desvincular os documentos não recebidos
             else:

                 pessoar = self.env['pessoas'].search([('ata_id', '=', self.ata_id), ('tem_pedido', '=', '1')])
                 for pr in pessoar:
                     pr.write({'tem_pedido': '2'}) #'tem_solicitacao': '2',
                     pr.write({'fiador': '2'})

                 pessoa_clientr = self.env['terceiro.terceiro'].search(
                     [('ata_id', '=', self.ata_id), ('tem_solicitacao', '=', '1')])
                 if pessoa_clientr:
                     #raise ValidationError('OK2')
                     for pcr in pessoa_clientr:
                         pcr.tem_fatur = False
                         pcr.write({'tem_pedido': '2'})
                         pcr.write({'tem_solicitacao': '2'})

                 #selict = self.env['solicitacao.credito'].search(
                 #    [('nif_pessoa', '=', self.nif_pessoa), ('estado', '=', '3')])
                 #selict.write({'estado': '4'})
                 selict = self.env['credito.aprovado'].search(
                     [('ata_id', '=', self.ata_id), ('estado', '=', '1')])
                 selict.write({'estado': '2'})
                 clien = self.env['clientes'].search([('ata_id', '=', self.ata_id), ('estado', '=', '1')])
                 if clien:
                    for c in clien:
                        c.write({'estado': '2'})



             #Aque encrementa saldo
             if self.tipo_pagamento_receb != '1':
                 meios = self.env['monetario.monetario'].search([('id', '=', self.nossa_conta.id)])
                 if not meios:
                     raise ValidationError('Esta conta não existe!')
                 else:
                     for lin in meios:
                         lin.saldo_inicial += self.vervalor_total_receb
             elif self.tipo_pagamento_receb == '1':
                 meios = self.env['monetario.monetario'].search([('name', '=', 'CAIXA PRINCIPAL')])
                 if not meios:
                     raise ValidationError('Não existe conta com nome CAIXA PRINCIPAL!')
                 else:
                     for lin in meios:
                         lin.saldo_inicial += self.vervalor_total_receb


     def creat_doc_part(self):#este metudo cria novo documento se o documento foi recebido apenas uma parte
         if self.por_partes == True:
            #raise ValidationError('OK1')
            part = self.env['reg.docum']
            for l in self.reg_docum_ids:
                if l.saldo != l.total and l.saldo != 0:
                    l.write({'estado': '2'})
                    docum = part.create({'tipo_docum': l.tipo_docum.id, 'numeros_docum': l.numeros_docum,
                                    'cod_documento': l.cod_documento, 'nome_terc': self.terceiro_id_doc_conta_corente_receb.id,
                                    'visualizar_no_tesorer': l.visualizar_no_tesorer, 'saldo': self.resultado, 'numer_prest': l.numer_prest,
                                    'total': l.total, 'valorAsc': l.valorAsc, 'documentos': l.documentos, 'desting_doc_vend': l.desting_doc_vend,
                                    'data_documento': l.data_documento, 'aprovado': l.aprovado, 'ata': l.ata})
                    return docum

         else:
             #raise ValidationError('OK2')
             ver_pessoa = self.env['reg.docum'].search(
                [('ata', '=', self.ata_id),
                 ('nome_terc', '=', self.terceiro_id_doc_conta_corente_receb.id), ('aprovado', '=', 'True'), ('renegociado', '=', False), ('estado', '=', '2')])
             for v in self.reg_docum_ids:
                 if v.cobrado == True:
                    v.write({'estado': '3'})
                    v.recebido_completo = True
             for d in ver_pessoa:
                 d.write({'estado': '3'})
             cred_aprov = self.env['credito.aprovado'].search([('ata_id', '=', self.ata_id), ('estado', '=', '1')])
             if cred_aprov:
                 for c in cred_aprov:
                     c.valor_em_div -= self.montante_receb
             ver_doc = self.env['reg.docum'].search([('ata', '=', self.ata_id), ('renegociado', '=', False), ('cobrado', '=', False)])
             if ver_doc:
                 pass
             else:
                 for v in ver_doc:
                     v.fechado = True

     def creat_det_lanc(self):

         date = datetime.datetime.today()
         if self.dados_antigo == False:
             diamov = date.day
             mesmov = date.month
             anomov = date.year
             if self.tipo_pagamento_receb == '1':
                 d = self.env['diario.diario'].search([('name', '=', 'DIARIO CAIXA'), ('id', '=', 1)])
                 diario = d.id
             else:
                 diario = self.diario
             new_lancamento = self.env['lancamento_diario.lancamento_diario']
             lanca = new_lancamento.create(
                 {'diario': diario, 'data': self.date, 'valor': self.vervalor_total_receb, 'credito': self.vervalor_total_receb, 'cod_recebmento': self.id,
                  'name_diario': self.name_diario, 'diamov': diamov, 'conta_d': self.codigo_conta.id, 'tipo_movimento': self.tipo_movimento,'mesmov': mesmov, 'anomov': anomov,'obs': 'FastGest Tesouraria Recebimento',
                  'terceiro_id_doc_conta_corente_receb': self.terceiro_id_doc_conta_corente_receb.id})
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
                 {'dados_antigo': 'True', 'diario': diario, 'dfecpag': self.dfecpag, 'valor': self.vervalor_total_receb, 'credito': self.vervalor_total_receb, 'cod_recebmento': self.id,
                  'name_diario': self.name_diario, 'diamov': diamov, 'mesmov': mesmov, 'tipo_movimento': self.tipo_movimento, 'anomov': anomov, 'obs': 'FastGest Tesouraria Recebimento', 'conta_d': self.codigo_conta.id,
                  'terceiro_id_doc_conta_corente_receb': self.terceiro_id_doc_conta_corente_receb.id})
         if self.documentot == '1':
            new_det_lan = self.env['detalhe.lancamento']#A linha do valor recebido
            det_lanca = new_det_lan.create({
                'codigo_conta': self.codigo_conta.id,
                'descritivo': self.detalhes,
                'deb_cred': 'D',
                'cod_recebmento': self.id,
                'centro_custo': self.centro_custo.id,
                'fluxo_caixa': self.fluxo_caixa.id,
                'valor_credito': self.vervalor_total_receb,
                'codigo_iva': self.codigo_iva.id,
                'valor_moeda_estra': self.valor_moeda_estra.id,
                'terceiro_id_doc_conta_corente_receb': self.terceiro_id_doc_conta_corente_receb.id,
                'moeda_estra': self.moeda_estra.id,
            })
            param_pres = self.env['parametros.parametros'].search([('variavel', '=', 'codPrestacao')])
            servi_prest = self.env['produto.produto'].search([('codigo', '=', param_pres.valor)])
            for line in self.reg_docum_ids:
                num_prest = line.numer_prest
                num_cred = line.numero_credito
                new_det_lan_pret = self.env['detalhe.lancamento']  # A linha do valor prestação
                det_lanca_pret = new_det_lan_pret.create({'codigo_conta': servi_prest.conta_artigo.id,
                    'descritivo': 'Prestação Nº ' + str(num_prest)+'/' + 'Credito Nº' + str(num_cred),
                    'deb_cred': 'C',
                    'centro_custo': self.centro_custo.id,
                    #'codigo_entidade': self.cod_terceiro,
                    'fluxo_caixa': self.fluxo_caixa.id,
                    'valor_credito': line.amortizacao,
                    'codigo_iva': self.codigo_iva.id,
                    'valor_moeda_estra': self.valor_moeda_estra.id,
                    'terceiro_id_doc_conta_corente_receb': self.terceiro_id_doc_conta_corente_receb.id,
                    'moeda_estra': self.moeda_estra.id,
                    'cod_recebmento': self.id,
                })
            param_jur = self.env['parametros.parametros'].search([('variavel', '=', 'codjuros')])
            servi_jur = self.env['produto.produto'].search([('codigo', '=', param_jur.valor)])
            for line in self.reg_docum_ids:
                num_prest = line.numer_prest
                num_cred = line.numero_credito

                new_det_lan_pret = self.env['detalhe.lancamento']  # A linha do valor Juros
                det_lanca_pret = new_det_lan_pret.create({
                    'codigo_conta': servi_jur.conta_artigo.id,
                    'descritivo': 'Juros Empres./Prest.Nº ' + str(num_prest)+'/'+'Credito Nº' + str(num_cred),
                    'deb_cred': 'C',
                    'centro_custo': self.centro_custo.id,
                    'fluxo_caixa': self.fluxo_caixa.id,
                    'valor_credito': line.juro_jerado,
                    'codigo_iva': self.codigo_iva.id,
                    'valor_moeda_estra': self.valor_moeda_estra.id,
                    'terceiro_id_doc_conta_corente_receb': self.terceiro_id_doc_conta_corente_receb.id,
                    'moeda_estra': self.moeda_estra.id, 'cod_recebmento': self.id,})
         elif self.documentot == '2':
             new_det_lan = self.env['detalhe.lancamento']  # A linha do valor recebido
             det_lanca = new_det_lan.create({
                 'codigo_conta': self.codigo_conta.id,
                 'descritivo': self.det_obs_doc_tesora,
                 'deb_cred': 'D',
                 'cod_recebmento': self.id,
                 'centro_custo': self.centro_custo.id,
                 'fluxo_caixa': self.fluxo_caixa.id,
                 'valor_credito': self.vervalor_total_receb,
                 'codigo_iva': self.codigo_iva.id,
                 'valor_moeda_estra': self.valor_moeda_estra.id,
                 'terceiro_id_doc_conta_corente_receb': self.terceiro_id_doc_conta_corente_receb.id,
                 'moeda_estra': self.moeda_estra.id,})
             for l in self.doc_teso:
                 new_det_lan = self.env['detalhe.lancamento']
                 det_lanca = new_det_lan.create({
                     'codigo_conta': l.conta_id.id,
                     'descritivo': l.desc_serv,
                     'deb_cred': 'C',
                     'cod_recebmento': self.id,
                     'valor_credito': l.sub_total,
                     'terceiro_id_doc_conta_corente_receb': self.terceiro_id_doc_conta_corente_receb.id, })
         lanca = self.env['lancamento_diario.lancamento_diario'].search([('id', '>=', 1)])
         if lanca:
             for l in lanca:
                 det_lanc = self.env['detalhe.lancamento'].search([('cod_recebmento', '=', l.cod_recebmento)])
                 for dl in det_lanc:
                     dl.lancamento_diario = l.id

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

         pag = self.env['lancamento_diario.lancamento_diario'].search([('cod_recebmento', '=', self.id)])
         ac = self.env['ir.model.data'].xmlid_to_res_id('contabilidade.teste_form', raise_if_not_found=True)
         det_lanc = self.env['detalhe.lancamento'].search([('cod_recebmento', '=', self.id)])
         for dl in det_lanc:
             dl.ver_contab = True

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
                 'context': {
                     'default_diario': diario,
                     'default_name_diario': name_diario,
                     'default_data': data,
                     'default_ordem': ordem,
                     'default_valor': valor,
                     'default_valor1': valor1,
                     'default_nome_conta': nome_conta,
                     'default_entidade_d': entidade_d,
                     'default_ver_contab': True,
                     'default_obs': obs,
                     'default_terceiro_id_doc_conta_corente_receb': terceiro_id_doc_conta_corente_receb,
                 },
                 'type': 'ir.actions.act_window',
                 'target': 'new',
                 'view_mode': 'form'
             }
             return result

     @api.multi
     @api.onchange('origem')  # Add valores na lista
     def most_list_doc(self):
         if self.origem == True:
             if self.documentot == '2':
                 det = self.env['documento.tesoraria.recebimento'].search([('origem', '=', True)])
                 list_of_docum = []
                 for line in det:
                     data = self._comput_line(line)
                     data.update(
                         {'servico_id': line.servico_id.id, 'preco_unit': line.preco_unit,
                          'quant': line.quant, 'taxa': line.taxa, 'desconto': line.desconto,
                          'sub_total': line.sub_total, })
                     list_of_docum.append((1, line.id, data))

                 return {'value': {"doc_teso": list_of_docum}}
             if self.documentot == '1':
                 det_reg = self.env['reg.docum'].search([('origem', '=', True)])
                 list_docum = []
                 for l in det_reg:
                     data = self._comput_line(l)
                     data.update(
                         {'cod_documento': l.cod_documento, 'total': l.total, 'saldo': l.saldo,
                          'cobrado': l.cobrado, 'data_documento': l.data_documento, 'valorreceb': l.valorreceb})
                     list_docum.append((1, l.id, data))

                 return {'value': {"reg_docum_ids": list_docum}}

class documentoTesorariaRecebimento(models.Model):
    _name = 'documento.tesoraria.recebimento'
    _description = 'Documento de Tesouraria Recebimento'
    artigo_id = fields.Many2one('artigo.artigo', string='Codigo Artigo')
    servico_id = fields.Many2one('produto.produto', string='Codigo Serviços')# no proximo import trabalhar co esse campo não artigo
    conta_id = fields.Many2one('planconta.planconta', string='Conta', related="servico_id.conta_artigo")
    desc_serv = fields.Char(string="Descrição", store=True, related='servico_id.name')
    name_artigo= fields.Char(string="Descrição")
    preco_unit = fields.Float(string='Preço Unitario')
    quant = fields.Float(string='Quantidade', default=1)
    iva_id = fields.Many2one('iva.iva', string='Iva(%)')
    taxa = fields.Float(string='Iva(%)', related="iva_id.taxa")
    desconto = fields.Float(string='Desconto')
    sub_total = fields.Float(string='Sub-Total', readonly=True, compute='calc_preco')
    sequence = fields.Integer(help="Dá a seqüência desta linha ao exibir a fatura.")
    teso_receb_id = fields.Many2one('pagamento.recebimento', ondele='cascade', index=True)
    recebimento_id = fields.Many2one('tesouraria.recebimento', string="Recebimento")
    dados_antigo = fields.Boolean(string="Dados Antigo")
    origem = fields.Boolean(string="Origem da contabilidade")

    displlay_type = fields.Selection([('line_section', 'section'), ('line_note', 'nota')], string='displlay')
    state = fields.Selection([('draft', 'Draft'), ('open', 'Open'), ('paid', 'Paid'), ('cancel', 'Cancelled'), ],
                             string='Status', index=True, readonly=True, default='draft', track_visibility='onchange',
                             copy=False)


    @api.one
    @api.depends('preco_unit', 'desconto', 'quant', 'taxa')
    def calc_preco(self):
        for line in self:
            line.sub_total = line.preco_unit * (1.0 - line.desconto / 100.0) * line.quant

    CDOCINT = fields.Char()
    CNUMFEC = fields.Char()
    CCODART = fields.Char()
    COTRTER = fields.Char()
    IDART = fields.Char()
    # CDESART = fields.Char()

    def mod_det(self):
        pass

        #tes_receb = self.env['tesouraria.recebimento'].search([('documentot', '=', '2')])
        #for c in tes_receb:
        #    cod = str(c.CMOVINT)
        #    if cod.isnumeric() == True:
        #        det = self.env['documento.tesoraria.recebimento'].search([('CDOCINT', '=', c.CMOVINT)])
        #        for d in det:
        #            d.recebimento_id = c.id


        tes_receb = self.env['pagamento.recebimento'].search([('documentot', '=', '2'), ('type_docum', '=', 'recebimento')])
        for c in tes_receb:
           cod = str(c.CMOVINT)
           if cod.isnumeric() == True:
               det = self.env['documento.tesoraria.recebimento'].search([('CDOCINT', '=', c.CMOVINT)])
               for d in det:
                   d.teso_receb_id = c.id

       #artig = self.env['artigo.artigo'].search([('id', '>', 0)])

       #for c in artig:

       #    cod = str(c.ccodart)
       #    if cod.isnumeric() == True:
       #       c.ccodart1 = c.ccodart
       #       det = self.env['documento.tesoraria.recebimento'].search([('CCODART', '=', c.ccodart1)])
       #       for d in det:
       #           d.artigo_id = c.id

        #det = self.env['documento.tesoraria.recebimento'].search([('id', '>', 0)])
        #for c in det:
        #    c.quant = 1
        #    c.sub_total = c.preco_unit

class NewModule(models.Model):
    _name = 'reg.caja'
    #_rec_name = 'name'
    _description = 'Reg Caja'

    CMOVINT = fields.Char()
    CMOVINT2 = fields.Integer()
    LTIPMOV = fields.Char()
    CNUMPAG = fields.Char()
    CCODTER = fields.Char()
    CNOMTER = fields.Char()
    NVALPAG = fields.Char()
    DFECPAG = fields.Char()
    CDETPAG = fields.Char()
    NTIPPAG = fields.Char()
    CCODMED = fields.Char()
    CNUMCHQ = fields.Char()
    CCODBCO = fields.Char()
    DFECDEP = fields.Char()
    LPAGANU = fields.Char()
    CNUMFEC = fields.Char()
    LSINCTA = fields.Char()
    NTIPMOV = fields.Char()
    CCODCAJ = fields.Char()
    CCODDIA = fields.Char()
    CNUMORD = fields.Char()
    LPENDEN = fields.Char()
    NOTRVAL = fields.Char()
    CMONPRN = fields.Char()
    CKEYUSE = fields.Char()
    CTIME   = fields.Char()
    DDATE   = fields.Char()
    COPER   = fields.Char()

    dfecpag = fields.Char()
    cmovint = fields.Char()
    scmovint1 = fields.Integer()

    def mod_det(self):
       #pass

       ct = self.env['reg.caja'].search([('id', '>', 0)])
       for c in ct:
           #c.dfecpag = c.DFECPAG
           c.scmovint1 = c.CMOVINT2
           c.cmovint = c.CMOVINT2

       ter_rec= self.env['tesouraria.recebimento'].search([('id', '>', 0)])
       for d in ter_rec:
           #d.dfecpag = d.DFECPAG
           d.scmovint1 = d.cmovint


       #artig = self.env['artigo.artigo'].search([('id', '>', 0)])

       #for c in artig:
       #    cod = str(c.ccodart)
       #    if cod.isnumeric() == True:
       #       c.ccodart1 = c.ccodart
       #       det = self.env['documento.tesoraria.recebimento'].search([('CCODART', '=', c.ccodart1)])
       #       for d in det:
       #           d.artigo_id = c.id

        #det = self.env['documento.tesoraria.recebimento'].search([('id', '>', 0)])
        #for c in det:
        #    c.quant = 1
        #    c.sub_total = c.preco_unit

class receb(models.Model):
    _name = 'receb'
    #_rec_name = 'name'
    _description = 'Recebimento'

    cmovint = fields.Char()
    dfecpag = fields.Char()

    def add_estado(self):
        est_sol = self.env['receb'].search([('id', '>=', 1)])
        for esta in est_sol:
            docum = self.env['tesouraria.pagamento'].search([('cmovint', '=', esta.cmovint)])
            for d in docum:
                d.dfecpag = esta.dfecpag