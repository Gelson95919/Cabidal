# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

import datetime

class movInterno(models.Model):
     _name = 'tesouraria.movimento.interno'
     _description = 'Movimento Interno'
     _rec_name = 'n_movimento'

     n_movimento = fields.Char(string='Movimento Nº', copy=False, readonly=True,
                               index=True, default=lambda self: self._get_next_cod())
     nossa_conta_transfe = fields.Many2one('monetario.monetario',
                                           string='Conta Origem', domain="[('tipo_meio','=','2')]")  #
     movimento = fields.Many2one('movinterno.movinterno', string='Movimento')
     date_release = fields.Date('Data', default=fields.Date.today)#
     centro_custo = fields.Many2one('planconta.planconta', string='Centro Custo')
     detalhes = fields.Char(string='Detalhes', readonly=False, store=True)
     montante_mov = fields.Float(string='Montante')
     saldo_transf = fields.Float(string='Saldo', related="nossa_conta_transfe.saldo_inicial", store=True, readonly=True)
     cheque = fields.Char(string='Cheque')
     esc = fields.Float(string='Esc Orig')
     contabilizado = fields.Boolean(string='Contabilizado')
     diario_orig_id = fields.Many2one('diario.diario', string="Diario Origem", related="nossa_conta_transfe.diario")
     diario = fields.Char(string='Diario Origem', related="diario_orig_id.name")#
     numero = fields.Char(string='Numero Origem')

     conta_destino = fields.Many2one('monetario.monetario', string='Conta Destino')
     conta_des = fields.Many2one('planconta.planconta', string='Conta dest Id', related="conta_destino.conta")
     conta_id = fields.Many2one('planconta.planconta', string='Conta Id',  related="movimento.conta")
     nome_conta_dest = fields.Char(string="Nome Conta Destino", related="conta_destino.name")
     escd = fields.Float(string='Esc')
     diariod = fields.Many2one('diario.diario', string='Diario dest',  related="conta_destino.diario")
     contabilizadod = fields.Boolean(string='Contabilizado dest')
     numerod = fields.Char(string='Numero dest')
     descricao = fields.Text('Descrição')
     desc_mov = fields.Char(string="Desc Movimento", related="movimento.name")
     mov_sai_ent = fields.Boolean(string="Mov")  # , compute="create_movimento" permite filtrar apenas um movimento no tree
     mov_sai = fields.Boolean(string="Mov")  # permite filtrar apenas um movimento no tree
     movimentado = fields.Boolean(string="Movimentadol")
     confirmado = fields.Boolean(string="Confirmado")
     anulado = fields.Boolean(string="Anulado")
     tipo_movimento = fields.Selection([('1', 'Tranfirencia'), ('2', 'Entrada'), ('3', 'Saida')],
                                       'Tipo Movimento', Widget="radio",
                                       related="movimento.tipo_movimento",
                                       store=True)
     type_docum = fields.Selection(
          [('recebimento', 'Recebimento'), ('pagamento', 'Pagamento'), ('movimento', 'Movimento')], readonly=True,
          index=True, change_default=True, default=lambda self: self._context.get('type_docum', 'movimento'),
          track_visibility='always', store=True)
     folha_tesouraria_id = fields.Many2one('folha.tesouraria')
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

     dados_antigo = fields.Boolean(string="Dados Antigo")  # se True porque os dados são antigo
     tip_movimento = fields.Selection(
         [('1', 'Pagamento'),
          ('2', 'Recebimento'), ('3', 'Movimento Interno')], store=True, string='Documento', Widget="radio",
         default='3')
     origem = fields.Boolean(string="Origem da contabilidade")
     dfecmovint = fields.Char()

     @api.one
     @api.constrains('dados_antigo')
     def val_dados_antig(self):  # Verificar se o dados e antigo ou não
         if self.dados_antigo == True:
             pass#raise ValidationError(
             #    'Dados antigo, ha algumas informações que precisam ser modificado, Contacta o adminstrador de sistema se consideraste que é um erro ')


     cccodmov = fields.Char()

     ccodint = fields.Char()
     ntipmov = fields.Char()
     cdiariorig = fields.Char()
     cmedori = fields.Char()
     cmedori1 = fields.Integer()
     cmovori = fields.Char()
     cordori = fields.Char()

     cmeddes = fields.Char()
     cmeddes1 = fields.Integer()
     cdiades = fields.Char()
     cmovdest = fields.Char()
     cordordes = fields.Char()
     lanulado = fields.Boolean()

     def ver_contabilidadeorg(self):
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
         cmv= []
         mv = self.env['pagamento.recebimento'].search([('cod_movint', '=', self.id), ('mov_sai_ent', '=', True)])
         for i in mv:
             cmv.append(i.id)
         det_lanc = self.env['detalhe.lancamento'].search([('cod_movint', '=', mv.id)])
         for dl in det_lanc:
             dl.ver_contab = True
         cod = mv[0]
         cod_mov = int(cod)
         l = self.env['lancamento_diario.lancamento_diario'].search([('cod_movint', '=', cod_mov)])
         ac = self.env['ir.model.data'].xmlid_to_res_id('contabilidade.teste_form', raise_if_not_found=True)
         if l:
             for dad in l:
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

     def ver_contabilidadedest(self):
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
         cmv = []
         mv = self.env['pagamento.recebimento'].search([('cod_movint', '=', self.id), ('mov_sai_ent', '=', False)])
         for i in mv:
             cmv.append(i.id)
         det_lanc = self.env['detalhe.lancamento'].search([('cod_movint', '=', mv.id)])
         for dl in det_lanc:
             dl.ver_contab = True

         cod = cmv[0]
         cod_movim = int(cod)
         l = self.env['lancamento_diario.lancamento_diario'].search([('cod_movint', '=', cod_movim)])
         ac = self.env['ir.model.data'].xmlid_to_res_id('contabilidade.teste_form', raise_if_not_found=True)
         if l:
             for dad in l:
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


     def compor_op(self):
         #pass
         mov_int = self.env['pagamento.recebimento'].search([('type_docum', '=', 'movimento')])
         for m in mov_int:
             #m.conta_destino = 3
             m.cmovori_int = m.cmovori
#
         #mov_intk = self.env['pagamento.recebimento'].search([('tipo_movimento', '=', '3')])
         #for n in mov_intk:
         #    #n.conta_destino = 6
         #    n.valor_total_pag = n.montante_mov
#
         #mov_intkdd = self.env['pagamento.recebimento'].search([('tipo_movimento', '=', '1'), ('mov_inter_orig', '=', False)])
         #for r in mov_intkdd:
         #    #r.valor_total_pag = r.montante_mov
         #    r.vervalor_total_receb = r.montante_mov

         #mov_intkdd = self.env['pagamento.recebimento'].search([('cmeddes', '=', '10'), ('tipo_movimento', '=', '2')])
         #for r in mov_intkdd:
         #    r.conta_destino = 10

         #pass
         #mov_inter_orig = self.env['tesouraria.movimento.interno'].search(
         #    [('tipo_movimento', '=', '1'), ('cmeddes', '=', '05')])  # (05) ===> BCN N5270 TRANS CREAT ORIG
         #for tp in mov_inter_orig:
         #    mov_int = self.env['pagamento.recebimento']
         #    mov_in = mov_int.create({'n_movimento': tp.n_movimento, 'mov_inter_orig_05': 'True',
         #                             'nossa_conta_transfe': tp.nossa_conta_transfe.id,
         #                             'movimento': tp.movimento.id,
         #                             'centro_custo': tp.centro_custo.id,
         #                             'montante_mov': tp.montante_mov,
         #                             'esc': tp.esc,
         #                             'cheque': tp.cheque,
         #                             'type_docum': 'movimento',
         #                             'conta_destino': tp.conta_destino.id,
         #                             'escd': tp.escd,
         #                             'diariod': tp.diariod,
         #                             'diario': tp.diario,
         #                             'detalhes': tp.detalhes,
         #                             'contabilizadod': tp.contabilizadod,
         #                             'numerod': tp.numerod,
         #                             'tipo_movimento': tp.tipo_movimento,
         #                             'descricao': tp.descricao,
         #                             'mov_sai_ent': tp.mov_sai_ent,
         #                             'mov_sai': 'True',
         #                             'movimentado': tp.movimentado,
         #                             'anulado': tp.anulado,
         #                             'numero': tp.numero,
         #                             'ccodmov': tp.ccodmov,
         #                             'dfecmovint': tp.dfecmovint,
         #                             'ccodint': tp.ccodint,
         #                             'ntipmov': tp.ntipmov,
         #                             'cdiariorig': tp.cdiariorig,
         #                             'cmedori': tp.cmedori,
         #                             'cmedori1': tp.cmedori1,
         #                             'cmovori': tp.cmovori,
         #                             'cordori': tp.cordori,
         #                             'cmeddes': tp.cmeddes,
         #                             'cmeddes1': tp.cmeddes1,
         #                             'cdiades': tp.cdiades,
         #                             'cmovdest': tp.cmovdest,
         #                             'cordordes': tp.cordordes,
         #                             'lanulado': tp.lanulado})


         #mov_inter_orig = self.env['tesouraria.movimento.interno'].search(
         #    [('tipo_movimento', '=', '1'), ('cmeddes', '=', '03')])  # (03) ===> BCN N5270 TRANS CREAT ORIG
         #for tp in mov_inter_orig:
         #    mov_int = self.env['pagamento.recebimento']
         #    mov_in = mov_int.create({'n_movimento': tp.n_movimento, 'mov_inter_orig_03': 'True',
         #                             'nossa_conta_transfe': tp.nossa_conta_transfe.id,
         #                             'movimento': tp.movimento.id,
         #                             'centro_custo': tp.centro_custo.id,
         #                             'montante_mov': tp.montante_mov,
         #                             'esc': tp.esc,
         #                             'cheque': tp.cheque,
         #                             'type_docum': 'movimento',
         #                             'conta_destino': tp.conta_destino.id,
         #                             'escd': tp.escd,
         #                             'diariod': tp.diariod,
         #                             'diario': tp.diario,
         #                             'detalhes': tp.detalhes,
         #                             'contabilizadod': tp.contabilizadod,
         #                             'numerod': tp.numerod,
         #                             'tipo_movimento': tp.tipo_movimento,
         #                             'descricao': tp.descricao,
         #                             'mov_sai_ent': tp.mov_sai_ent,
         #                             'mov_sai': 'True',
         #                             'movimentado': tp.movimentado,
         #                             'anulado': tp.anulado,
         #                             'numero': tp.numero,
         #                             'ccodmov': tp.ccodmov,
         #                             'dfecmovint': tp.dfecmovint,
         #                             'ccodint': tp.ccodint,
         #                             'ntipmov': tp.ntipmov,
         #                             'cdiariorig': tp.cdiariorig,
         #                             'cmedori': tp.cmedori,
         #                             'cmedori1': tp.cmedori1,
         #                             'cmovori': tp.cmovori,
         #                             'cordori': tp.cordori,
         #                             'cmeddes': tp.cmeddes,
         #                             'cmeddes1': tp.cmeddes1,
         #                             'cdiades': tp.cdiades,
         #                             'cmovdest': tp.cmovdest,
         #                             'cordordes': tp.cordordes,
         #                             'lanulado': tp.lanulado})

         #mov_inter_orig = self.env['tesouraria.movimento.interno'].search(
         #    [('tipo_movimento', '=', '1'), ('cmeddes', '=', '02')])  # (02) ===> BCN N5270 TRANS ORIG
         #for tp in mov_inter_orig:
         #    mov_int = self.env['pagamento.recebimento']
         #    mov_in = mov_int.create({'n_movimento': tp.n_movimento, 'mov_inter_orig': 'True',
         #                             'nossa_conta_transfe': tp.nossa_conta_transfe.id,
         #                             'movimento': tp.movimento.id,
         #                             'centro_custo': tp.centro_custo.id,
         #                             'montante_mov': tp.montante_mov,
         #                             'esc': tp.esc,
         #                             'cheque': tp.cheque,
         #                             'type_docum': 'movimento',
         #                             'conta_destino': tp.conta_destino.id,
         #                             'escd': tp.escd,
         #                             'diariod': tp.diariod,
         #                             'diario': tp.diario,
         #                             'detalhes': tp.detalhes,
         #                             'contabilizadod': tp.contabilizadod,
         #                             'numerod': tp.numerod,
         #                             'tipo_movimento': tp.tipo_movimento,
         #                             'descricao': tp.descricao,
         #                             'mov_sai_ent': tp.mov_sai_ent,
         #                             'mov_sai': 'True',
         #                             'movimentado': tp.movimentado,
         #                             'anulado': tp.anulado,
         #                             'numero': tp.numero,
         #                             'ccodmov': tp.ccodmov,
         #                             'dfecmovint': tp.dfecmovint,
         #                             'ccodint': tp.ccodint,
         #                             'ntipmov': tp.ntipmov,
         #                             'cdiariorig': tp.cdiariorig,
         #                             'cmedori': tp.cmedori,
         #                             'cmedori1': tp.cmedori1,
         #                             'cmovori': tp.cmovori,
         #                             'cordori': tp.cordori,
         #                             'cmeddes': tp.cmeddes,
         #                             'cmeddes1': tp.cmeddes1,
         #                             'cdiades': tp.cdiades,
         #                             'cmovdest': tp.cmovdest,
         #                             'cordordes': tp.cordordes,
         #                             'lanulado': tp.lanulado})

         #mov_inter = self.env['tesouraria.movimento.interno'].search([('tipo_movimento', '=', '1'), ('cmedori', '=', '11')])
         #for tp in mov_inter:
         #    #if tp.id <= 9949:
         #        mov_int = self.env['pagamento.recebimento']
         #        mov_in = mov_int.create({'n_movimento': tp.n_movimento, 'mov_inter_orig_11': 'True',
         #                                  'nossa_conta_transfe': tp.nossa_conta_transfe.id,
         #                                  'movimento': tp.movimento.id, 'mov_sai': 'True', 'mov_inter_orig': 'True',
         #                                  'centro_custo': tp.centro_custo.id,
         #                                  'montante_mov': tp.montante_mov,
         #                                  'esc': tp.esc,
         #                                  'cheque': tp.cheque,
         #                                  'type_docum': 'movimento',
         #                                  'conta_destino': tp.conta_destino.id,
         #                                  'escd': tp.escd,
         #                                  'diariod': tp.diariod,
         #                                  'diario': tp.diario,
         #                                  'detalhes': tp.detalhes,
         #                                  'contabilizadod': tp.contabilizadod,
         #                                  'numerod': tp.numerod,
         #                                  'tipo_movimento': tp.tipo_movimento,
         #                                  'descricao': tp.descricao,
         #                                  'mov_sai_ent': tp.mov_sai_ent,
         #                                  #'mov_sai': tp.mov_sai,
         #                                  'movimentado': tp.movimentado,
         #                                  'anulado': tp.anulado,
         #                                  'numero': tp.numero,
         #                                  'ccodmov': tp.ccodmov,
         #                                  'dfecmovint': tp.dfecmovint,
         #                                  'ccodint': tp.ccodint,
         #                                  'ntipmov': tp.ntipmov,
         #                                  'cdiariorig': tp.cdiariorig,
         #                                  'cmedori': tp.cmedori,
         #                                  'cmedori1': tp.cmedori1,
         #                                  'cmovori': tp.cmovori,
         #                                  'cordori': tp.cordori,
         #                                  'cmeddes': tp.cmeddes,
         #                                  'cmeddes1': tp.cmeddes1,
         #                                  'cdiades': tp.cdiades,
         #                                  'cmovdest': tp.cmovdest,
         #                                  'cordordes': tp.cordordes,
         #                                  'lanulado': tp.lanulado})


     def compor_por_int(self):
         pass

         #ct = self.env['tesouraria.movimento.interno'].search([('id', '>', 0)])
         #for c in ct:
         #  cod = str(c.cmedori)
         #  if cod.isnumeric() == True:
         #     c.cmedori1 = c.cmedori
         #     c.cmeddes1 = c.cmeddes
               # c.diario = c.cdiariorig
               # c.diariod = c.cdiades
               # c.detalhes = c.descricao

         #concmov = self.env['movinterno.movinterno'].search([('id', '>', 0)])
         #for c in concmov:
         #     ord_p = self.env['tesouraria.movimento.interno'].search([('ccodmov', '=', c.ccodigo)])
         #     for o in ord_p:
         #         o.movimento = c.id

         #concmov = self.env['monetario.monetario'].search([('id', '>', 0)])
         #for c in concmov:
         #     ord_p = self.env['tesouraria.movimento.interno'].search([('cmedori1', '=', c.id)])
         #     for o in ord_p:
         #          o.nossa_conta_transfe = c.id

         #concmovq = self.env['monetario.monetario'].search([('id', '>', 0)])
         #for c in concmovq:
         #     ord_p = self.env['tesouraria.movimento.interno'].search([('cmeddes1', '=', c.id)])
         #     for o in ord_p:
         #          o.conta_destino = c.id


     @api.model
     def _get_next_cod(self):
          sequence_np = self.env['ir.sequence'].search([('code', '=', 'fund.mane.num')])
          next_np = sequence_np.get_next_char(sequence_np.number_next_actual)
          return next_np

     @api.model
     def create(self, vals):
          vals['n_movimento'] = self.env['ir.sequence'].next_by_code('fund.mane.num')
          res = super(movInterno, self).create(vals)
          res.create_movimento()
          return res

     def create_movimento(self):
          if self.origem == True:
              raise ValidationError('Este documento ja foi lançado')
          """date = datetime.datetime.today()"""
          if self.tipo_movimento == '1': #Transfer
               cont = 0
               while cont < 2:

                    if cont == 0:
                         self. mov_sai_ent = True
                         mov = self.env['pagamento.recebimento']
                         movimentos = mov.create({'n_movimento': self.n_movimento, 'movimento': self.movimento.id,
                                                  'date_release': self.date_release, 'centro_custo': self.centro_custo.id, 'detalhes': self.detalhes,
                                                  'nossa_conta_transfe': self.nossa_conta_transfe.id, 'saldo_transf': self.saldo_transf,
                                                  'montante_mov': self.montante_mov, 'mov_sai_ent': self.mov_sai_ent,
                                                  'cheque': self.cheque, 'esc': self.esc, 'contabilizado': self.contabilizado,
                                                  'diario': self.diario, 'numerod': self.numerod, 'type_docum': self.type_docum,
                                                  'numero': self.numero, 'diario_orig_id': self.diario_orig_id.id,'cod_movint': self.id,
                                                  'conta_destino': self.conta_destino.id, 'tipo_movimento': self.tipo_movimento,
                                                  'escd': self.escd, 'tip_movimento': self.tip_movimento, 'contabilizadod': self.contabilizadod})

                    elif cont == 1:
                         self. mov_sai_ent = False # Mov dest
                         mov = self.env['pagamento.recebimento']
                         movimentos = mov.create({'n_movimento': self.n_movimento, 'movimento': self.movimento.id,
                                                  'date_release': self.date_release, 'centro_custo': self.centro_custo.id, 'detalhes': self.detalhes,
                                                  'nossa_conta_transfe': self.nossa_conta_transfe.id, 'saldo_transf': self.saldo_transf,
                                                  'montante_mov': self.montante_mov,  'mov_sai_ent': self.mov_sai_ent,
                                                  'cheque': self.cheque, 'esc': self.esc, 'contabilizado': self.contabilizado,
                                                  'numerod': self.numerod,'cod_movint': self.id,
                                                  'numero': self.numero, 'diariod': self.diariod.id,
                                                  'conta_destino': self.conta_destino.id, 'tipo_movimento': self.tipo_movimento,
                                                  'escd': self.escd, 'tip_movimento': self.tip_movimento, 'contabilizadod': self.contabilizadod})

                    cont += 1
               return True

          elif self.tipo_movimento == '2': #Entrada
               self.mov_sai_ent = True
               mov = self.env['pagamento.recebimento']
               movimentos = mov.create({'n_movimento': self.n_movimento, 'movimento': self.movimento.id,
                                        'date_release': self.date_release, 'centro_custo': self.centro_custo.id,
                                        'detalhes': self.detalhes,
                                        'nossa_conta_transfe': self.nossa_conta_transfe.id,
                                        'saldo_transf': self.saldo_transf, 'tip_movimento': self.tip_movimento,
                                        'montante_mov': self.montante_mov, 'mov_sai_ent': self.mov_sai_ent,
                                        'cheque': self.cheque, 'esc': self.esc, 'contabilizado': self.contabilizado,
                                        'diario': self.diario, 'numerod': self.numerod, 'cod_movint': self.id,
                                        'numero': self.numero, 'diariod': self.diariod.id,
                                        'conta_destino': self.conta_destino.id, 'tipo_movimento': self.tipo_movimento,
                                        'escd': self.escd, 'contabilizadod': self.contabilizadod})


               return  movimentos

          elif self.tipo_movimento == '3':  # Saida
               self.mov_sai_ent = False  # Mov Saida
               mov = self.env['pagamento.recebimento']
               movimentos = mov.create({'n_movimento': self.n_movimento, 'movimento': self.movimento.id,
                                        'date_release': self.date_release, 'centro_custo': self.centro_custo.id,
                                        'detalhes': self.detalhes,
                                        'nossa_conta_transfe': self.nossa_conta_transfe.id,
                                        'saldo_transf': self.saldo_transf,
                                        'montante_mov': self.montante_mov, 'mov_sai_ent': self.mov_sai_ent,
                                        'cheque': self.cheque, 'esc': self.esc, 'contabilizado': self.contabilizado,
                                        'diario': self.diario, 'numerod': self.numerod,'cod_movint': self.id,
                                        'numero': self.numero, 'diariod': self.diariod.id,
                                        'conta_destino': self.conta_destino.id, 'tipo_movimento': self.tipo_movimento,
                                        'escd': self.escd, 'contabilizadod': self.contabilizadod})

               return movimentos

