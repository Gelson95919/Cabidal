# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class trataOp(models.Model):
     _name = 'trat.dado.op'
     _description = 'Trata Dados OP'

     CDOCINT = fields.Char()
     DFECDOC = fields.Date()
     CMOVDOC  = fields.Char()
     CTIPDOC  = fields.Char()
     CNUMDOC  = fields.Char()
     CIDEDOC  = fields.Char()
     CCODTER  = fields.Char()
     CNOMTER  = fields.Char()
     NNETDOC  = fields.Char()
     NIMPDOC  = fields.Char()
     NTOTDOC  = fields.Char()
     NVALPAG  = fields.Char()
     LDOCAUT  = fields.Char()
     LDOCPAG  = fields.Char()
     LDOCANU  = fields.Char()
     LDOCCER  = fields.Char()
     CKEYUSE  = fields.Char()
     DFECVEN  = fields.Char()
     MOBS  = fields.Char()
     CIDEINT = fields.Char()
     LPAGUNI = fields.Char()
     LREDDET = fields.Char()
     DDATE   = fields.Char()
     CTIME   = fields.Char()
     COPER   = fields.Char()
     CCODART = fields.Char()
     CCODDIA = fields.Char()
     CNUMORD = fields.Char()
     DFECMOV = fields.Char()
     NVALDES = fields.Char()
     NVALVAR = fields.Char()
     CTIPPAG = fields.Char()
     LDESPOR = fields.Char()
     LCTACTE = fields.Char()
     LTESORE = fields.Char()
     CCODMON = fields.Char()
     IDTER = fields.Char()



     # 1111111111111111111111111111111111111111111111111111111111
     #def compor_op(self):
     #     terc = self.env['terceiro.terceiro'].search([('clientes', '=', True)])
     #     for c in terc:
     #          ord_p = self.env['trat.dado.op'].search([('CCODTER', '=', c.codigo)])
     #          for o in ord_p:
     #              o.CCODTER = c.id

     #22222222222222222222222222222222222222222222222222222
     def creat_terc(self):
          terc = self.env['terceiro.terceiro']#.search([('clientes', '=', True)])
          ord_p = self.env['trat.dado.op'].search([('LDOCAUT', '=', 'True')])
          if ord_p:
               for f in ord_p:
                    cod = str(f.CCODTER)
                    if (cod.isnumeric()) == False:
                       nam_terc = self.env['terceiro.terceiro'].search([('name', '=', f.CNOMTER)])
                       if not nam_terc:
                           fornec = terc.create({'name': f.CNOMTER, 'fornecedores': f.LDOCAUT, 'clientes': f.LDOCAUT, 'cliente_fornecdor': f.LDOCAUT})

     #33333333333333333333333333333333333333333333333333333333333333333333333333333333333333
     def compor_op(self):
          terc = self.env['terceiro.terceiro'].search([('cliente_fornecdor', '=', True)])
          for c in terc:
               ord_p = self.env['trat.dado.op'].search([('CNOMTER', '=', c.name)])
               for o in ord_p:
                    cod = str(o.CCODTER)
                    if (cod.isnumeric()) == False:
                       o.CCODTER = c.id

     #Passo 444444444444444444444444444444444444444444444444444444444444
     def creat_op(self):
          ord_pag = self.env['trat.dado.op'].search([('LDOCAUT', '=', 'True')])
          # self.detales = obs
          docum_op = self.env['tesouraria.ordem.pagamento']
          for p in ord_pag:
               doc_op = docum_op.create(
                    {'fornecedor_id': p.CCODTER, 'sem_cta_cte': p.LDOCAUT, 'op_solic':  p.LDOCAUT,
                     'valor_total': p.NTOTDOC, 'detalhes_ordem': p.MOBS, 'montante': p.NTOTDOC,
                     'date_release': p.DFECDOC,'CDOCINT': p.CDOCINT, 'CCODTER': p.CCODTER, 'CIDEDOC': p.CIDEDOC,})  # , 'nif_pessoa': self.nif_pessoa   'ata': self.id


     #passo55555555555555555555555555555555555555555555555555555
     def link_cred_aprov(self):
          docum_op = self.env['tesouraria.ordem.pagamento'].search([('sem_cta_cte', '=', 'True')])
          cred_aprov = self.env['credito.aprovado'].search([('sem_cta_cte', '=', 'True')])
          for p in docum_op:
               plano_obj_0 = self.env['reg.docum'].search([('CDOCINT', '=',p.CDOCINT)])


class trataDocu(models.Model):
     _name = 'docum'
     _description = 'Trata Dados Docum'

     CDOCINT = fields.Char()
     DFECDOC = fields.Date()
     CMOVDOC  = fields.Char()
     CTIPDOC  = fields.Char()
     CNUMDOC  = fields.Char()
     CIDEDOC  = fields.Char()
     CCODTER  = fields.Char()
     CNOMTER  = fields.Char()
     NNETDOC  = fields.Char()
     NIMPDOC  = fields.Char()
     NTOTDOC  = fields.Char()
     NVALPAG  = fields.Char()
     LDOCAUT  = fields.Char()
     LDOCPAG  = fields.Char()
     LDOCANU  = fields.Char()
     LDOCCER  = fields.Char()
     CKEYUSE  = fields.Char()
     DFECVEN  = fields.Char()
     MOBS  = fields.Char()
     CIDEINT = fields.Char()
     LPAGUNI = fields.Char()
     LREDDET = fields.Char()
     DDATE   = fields.Char()
     CTIME   = fields.Char()
     COPER   = fields.Char()
     CCODART = fields.Char()
     CCODDIA = fields.Char()
     CNUMORD = fields.Char()
     DFECMOV = fields.Char()
     NVALDES = fields.Char()
     NVALVAR = fields.Char()
     CTIPPAG = fields.Char()
     LDESPOR = fields.Char()
     LCTACTE = fields.Char()
     LTESORE = fields.Char()
     CCODMON = fields.Char()
     IDTER = fields.Char()
     IDCRED = fields.Char()

     mud_id = fields.Boolean(string="Mudar ID", default=True)
     compl = fields.Boolean(string="Complimento", default=False)
     outro = fields.Boolean(string="outro")
     a_outro = fields.Boolean(string="Aoutro")
     outro_1 = fields.Boolean(string="outro_1")
     outro_2 = fields.Boolean(string="outro_2")
     outro_3 = fields.Boolean(string="outro_3")
     outro_4 = fields.Boolean(string="outro_4")
     outro_5 = fields.Boolean(string="outro_5")
     outro_6 = fields.Boolean(string="outro_6")
     outro_7 = fields.Boolean(string="outro_7")
     outro_8 = fields.Boolean(string="outro_8")
     outro_9 = fields.Boolean(string="outro_9")
     outro_10 = fields.Boolean(string="outro_10")
     outro_11 = fields.Boolean(string="outro_11")
     outro_12 = fields.Boolean(string="outro_12")
     outro_13 = fields.Boolean(string="outro_13")
     outro_14 = fields.Boolean(string="outro_14")
     outro_15 = fields.Boolean(string="outro_15")
     outro_16 = fields.Boolean(string="outro_16")
     outro_17 = fields.Boolean(string="outro_17")
     outro_18 = fields.Boolean(string="outro_18")
     outro_19 = fields.Boolean(string="outro_19")
     outro_20 = fields.Boolean(string="outro_20")




     id_cred_post = fields.Char(string="ID CREDITO POST")
     id_op = fields.Char(string="ID OP")

     CD_PAG_RECEB = fields.Char()
     NUMEROCRED = fields.Char()
     ESTADO = fields.Char()
     PAGOTOTAL = fields.Char()
     DIVIDA = fields.Char()
     cont = fields.Char()


     # 1111111111111111111111111111111111111111111111111111111111
     def compor_op(self):
          terc = self.env['terceiro.terceiro'].search([('mud_id', '=', True)])
          for c in terc:
               ord_p = self.env['docum'].search([('CCODTER', '=', c.codigo)])
               for o in ord_p:
                   o.IDTER = c.id

     # 2222222222222222222222222222222222222222222222222222222222222222222222
     def compor_id_credito(self):
          terc = self.env['credito.aprovado'].search([('vd', '=', '1')])
          for c in terc:
               ord_p = self.env['docum'].search([('IDCRED', '=', c.IDCREDITO)])
               for o in ord_p:
                    o.id_cred_post = c.id

     # 3333333333333333333333333333333333333333333333333333333333333333333333
     def assoc_op(self):
        terc = self.env['credito.aprovado'].search([('vd', '=', '1')])
        for c in terc:
             docum = self.env['docum'].search([('CDOCINT', '=', c.cod_op)])
             for d in docum:
                 cod = str(d.id_cred_post)
                 if cod.isnumeric() == False:
                    d.id_cred_post = c.id

     #44444444444444444444444444444444444444444444444444444444444444444444444444444
     def atualiz_cta_cte(self): #este metudo atualiza o cta cte com alguns campos para mandar para reg docum original
          """docum = self.env['docum'].search([('compl', '=', False), ('outro_19', '=', False)])#passo 1
          cont = 0
          for t in docum:
               if cont <= 2001:
                   #t.outro = True    1  2000
                   #t.outro_1 = True  2  4000
                   #t.outro_2 = True  3  6000
                   #t.outro_3 = True  4  8000
                   #t.outro_4 = True  5  10000
                   #t.outro_5 = True  6  12000
                   #t.outro_6 = True  7  14000
                   #t.outro_7 = True  8  16000
                   #t.outro_8 = True  9  18000
                   #t.outro_9 = True  10 200000
                   #t.outro_10 = True 11 220000
                   #t.outro_11 = True 12 240000
                   #t.outro_12 = True 13 260000
                   #t.outro_13 = True  14 280000
                   #t.outro_14 = True  15 300000
                   #t.outro_15 = True  16 320000
                   #t.outro_16 = True  17 340000
                   #t.outro_17 = True   18 360000
                   #t.outro_18 = True   19 380000
                   #t.outro_19 = True   20 400000
                   t.outro_20 = True
               cont += 1"""

          docum = self.env['docum'].search([('outro_20', '=', True)])#passo 2
          for d in docum:
               cod_d = str(d.CDOCINT)
               if (cod_d.isnumeric()) == True:
                  cta = self.env['cta.cte'].search([('OPACDO', '=', d.CDOCINT)])
                  for c in cta:
                     cod = str(c.JUROS)
                     if (cod.isnumeric()) == False:
                       c.JUROS = d.NIMPDOC
                       c.AMORTIZACAO = d.NNETDOC
                       c.PRESTACAO = d.NTOTDOC

                       c.id_cred_post = d.id_cred_post
                       c.NUMEROCRED = d.NUMEROCRED
                       c.ESTADO = d.ESTADO
                       c.PAGOTOTAL = d.PAGOTOTAL
                       c.DIVIDA = d.DIVIDA

                       c.CNOMTER = d.CNOMTER
                       c.CIDEDOC = d.CIDEDOC
                       c.DFECVEN = d.DFECVEN
                       c.CNUMDOC = d.CNUMDOC
                       c.MOBS = d.MOBS
                       c.outro = True

          """docum = self.env['docum'].search([('compl', '=', False)])  # passo 3 priencher riba
          cont = 0
          for t in docum:
               if cont <= 40040:
                    t.outro_20 = True
               cont += 1"""


