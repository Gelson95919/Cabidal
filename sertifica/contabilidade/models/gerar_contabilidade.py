# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class gerar_contabilidade(models.Model):
    _name = 'gerar.contabilidade'
    #_rec_name = 'name'
    _description = 'Gerar Contabilidade'

    modulo = fields.Selection([
        ('documentoxpagar', "Documento x Pagar"),('documentoxcobrar', "Documento x Cobrar"),
        ('tesouraria', "Tesouraria"),
        ('remuneracoe', "Remunerações")], string='Modulo')
    selecionar_por = fields.Selection([('tipodocumento', "Tipo Documento"), ('terceiro', "Terceiro")], default='tipodocumento', string='Selecionar Por')
    tipodoc_id = fields.Many2one('documento.documento', string='Tipo Documento')
    terceiro_id = fields.Many2one('terceiro.terceiro', string='Terceiro')
    monetario_id = fields.Many2one('monetario.monetario', string='Meio Monetario')
    ordenar_por = fields.Selection([('data', "Data"), ('numerodocumento', "Numero Documento")], string='Ordenar Por')
    data_inicial = fields.Date('Data Inicio')
    data_final = fields.Date('Data Fim')
    mes = fields.Selection(
        [('janeior', 'Janeiro'), ('fevereiro', 'Fevereiro'), ('marco', 'Março'), ('abril', 'Abril'), ('Maio', 'Maio'),
         ('junho', 'Junho'), ('julho', 'Julho'), ('agosto', 'Agosto'), ('setembro', 'Setembro'), ('outubro', 'Outubro'),
         ('novembro', 'Novembro'), ('dezembro', 'Dezembor'), ], string='Mes')
    solo_gerar = fields.Boolean(string='Solo Gerar os com erros')
    gera_novo_numero_contab = fields.Boolean(string='Gerar Novo Numero da Contabilidade')
    so_os_nao_contabilidado = fields.Boolean(string='So os não Contabilizados')
    processar_document = fields.Boolean(string='Processar Documentos com valor < = 0')
    diario_pro_defeito = fields.Many2one('diario.diario', string='Diario Por Defeito')

    def processar(self):
        if self.modulo == 'tesouraria':
           #====================Lancamento Tesouraria recebimento =======================================
           new_lan_receb = self.env['tesouraria.recebimento'] .search([('id', '>=', 1)])

           #OU
           #import psycopg2
           #con = psycopg2.connect(host='localhost', database='regiao',
           #                       user='postgres', password='postgres123')
           #cur = con.cursor()
           #sql = 'create table cidade (id serial primary key, nome varchar(100), uf varchar(2))'
           #cur.execute(sql)
           #sql = "insert into cidade values (default,'São Paulo,'SP')"
           #cur.execute(sql)
           #con.commit()
           #cur.execute('select * from cidade')
           #recset = cur.fetchall()
           #for rec in recset:
           #    print(rec)
           #con.close()
           for l in new_lan_receb:
               date = datetime.datetime.today()
               if l.dados_antigo == False:
                   diamov = date.day
                   mesmov = date.month
                   anomov = date.year
                   new_lancamento = self.env['lancamento_diario.lancamento_diario']
                   lanca = new_lancamento.create(
                       {'diario': l.diario, 'data': l.date, 'valor': l.vervalor_total_receb,'cod_recebmento': l.id,
                        'name_diario': l.name_diario, 'diamov': diamov, 'mesmov': mesmov, 'anomov': anomov,
                        'terceiro_id_doc_conta_corente_receb': l.terceiro_id_doc_conta_corente_receb.id})
               if l.dados_antigo == True:
                   dat = l.dfecpag
                   x = dat.split('/')
                   datefec = x
                   list = []
                   for a in datefec:
                       list.append(a)
                   mesmov = list[0]
                   diamov = list[1]
                   anomov = list[2]

                   new_lancamento = self.env['lancamento_diario.lancamento_diario']
                   lanca = new_lancamento.create(
                       {'diario': l.diario, 'data': l.date, 'valor': l.vervalor_total_receb, 'cod_recebmento': l.id,
                        'name_diario': l.name_diario, 'diamov': diamov, 'mesmov': mesmov, 'anomov': anomov,
                        'terceiro_id_doc_conta_corente_receb': l.terceiro_id_doc_conta_corente_receb.id})

               new_det_lan = self.env['detalhe.lancamento']  # A linha do valor recebido
               det_lanca = new_det_lan.create({
                   'codigo_conta': l.codigo_conta.id,
                   'descritivo': l.detalhes,
                   'deb_cred': 'D',
                   'centro_custo': l.centro_custo.id,
                   'codigo_entidade': l.codigo_entidade.id,
                   'fluxo_caixa': l.fluxo_caixa.id,
                   'valor_credito': l.vervalor_total_receb,
                   'codigo_iva': l.codigo_iva.id,
                   'valor_moeda_estra': l.valor_moeda_estra.id,
                   'terceiro_id_doc_conta_corente_receb': l.terceiro_id_doc_conta_corente_receb.id,
                   'moeda_estra': l.moeda_estra.id,
                   'cod_recebmento': l.id,
               })
               for line in l.reg_docum_ids:
                   num_prest = line.numer_prest
                   num_cred = line.numero_credito
                   new_det_lan_pret = self.env['detalhe.lancamento']  # A linha do valor prestação
                   det_lanca_pret = new_det_lan_pret.create({
                       'codigo_conta': l.codigo_conta.id,
                       'descritivo': 'Prestação Nº 0' + str(num_prest) + '/' + 'Credito Nº' + str(num_cred),
                       'deb_cred': 'C',
                       'centro_custo': l.centro_custo.id,
                       'codigo_entidade': l.codigo_entidade.id,
                       'fluxo_caixa': l.fluxo_caixa.id,
                       'valor_credito': line.amortizacao,
                       'codigo_iva': l.codigo_iva.id,
                       'valor_moeda_estra': l.valor_moeda_estra.id,
                       'terceiro_id_doc_conta_corente_receb': l.terceiro_id_doc_conta_corente_receb.id,
                       'moeda_estra': l.moeda_estra.id,
                       'cod_recebmento': l.id,
                   })
               for line in l.reg_docum_ids:
                   num_prest = line.numer_prest
                   num_cred = line.numero_credito
                   new_det_lan_pret = self.env['detalhe.lancamento']  # A linha do valor Juros
                   det_lanca_pret = new_det_lan_pret.create({
                       'codigo_conta': l.codigo_conta.id,
                       'descritivo': 'Juros Empres./Prest.Nº 0' + str(num_prest) + '/' + 'Credito Nº' + str(num_cred),
                       'deb_cred': 'C',
                       'centro_custo': l.centro_custo.id,
                       'codigo_entidade': l.codigo_entidade.id,
                       'fluxo_caixa': l.fluxo_caixa.id,
                       'valor_credito': line.juro_jerado,
                       'codigo_iva': l.codigo_iva.id,
                       'valor_moeda_estra': l.valor_moeda_estra.id,
                       'terceiro_id_doc_conta_corente_receb': l.terceiro_id_doc_conta_corente_receb.id,
                       'moeda_estra': l.moeda_estra.id, 'cod_recebmento': l.id})

           lanca = self.env['lancamento_diario.lancamento_diario'].search([('id', '>=', 1)])
           if lanca:
               for l in lanca:
                   det_lanc = self.env['detalhe.lancamento'].search([('cod_recebmento', '=', l.cod_recebmento)])
                   for dl in det_lanc:
                       dl.lancamento_diario = l.id
           #===================================================================================================
