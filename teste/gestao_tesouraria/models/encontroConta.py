# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class econtroconta(models.Model):
    _name = 'econtroconta.econtroconta'
    _description = 'Encontro de Conta'
    _rec_name = 'terceiro_id'
    n_documento = fields.Char(string='Numero')
    terceiro_id = fields.Many2one('terceiro.terceiro', string='Terceiro', domain=lambda self:[("id", "in", self.env['reg.docum'].search([
     ('desting_doc_desp', '=', True), ('pago', '=', False), ('encontro', '=', False)], limit=900).mapped("nome_terc").ids)])
    #terceiro_id = fields.Many2one('terceiro.terceiro', string='Terceiro', domain=[('tem_despesas', '=', True)])
    numero = fields.Char('Numero')

    data = fields.Date('Data', default=fields.Date.today)
    doc_tesouraria = fields.Boolean(string='Documento Terceiro')
    doc_autoriz = fields.Boolean(string='Documento Autorizado')
    adiantamento_em_op = fields.Boolean(string='Adiantamento em OP')
    doc_cta_cte = fields.Boolean(string='Documento Cta.Cte.')
    reg_docum_ids = fields.One2many('reg.docum', 'encontro_conta_id', string="Reg Docum")
    anulado = fields.Boolean(string="Anulado")
    tot_parc_credito = fields.Float('Total Credito', compute="calc_tot_parc", store=True, cope=True)
    tot_parc_debito = fields.Float('Total Debito', compute="calc_tot_parc", store=True, cope=True)
    tot_parc_saldar = fields.Float('Total Saldo', compute="calc_tot_parc", store=True, cope=True)

    #campos computados
    selecionado_credito = fields.Float('Credito Selecionado', compute="calc_tot_select", store=True, cope=True)
    selecionado_debito = fields.Float('Debito Selecionado', compute="calc_tot_select", store=True, cope=True)
    selecionado_saldar = fields.Float('Saldo Selecionado', compute="calc_tot_select", store=True, cope=True)
    #campos que armanzena dados
    selecionado_credito1 = fields.Float('Credito Selecionado', store=True, cope=True)
    selecionado_debito1 = fields.Float('Debito Selecionado', store=True, cope=True)
    selecionado_saldar1 = fields.Float('Saldo Selecionado', store=True, cope=True)

    data_movimento = fields.Date('Data Movimento')
    contabilizar = fields.Boolean('Contabilizar')
    contabilizado = fields.Boolean('Contabilizado')
    diario = fields.Float('Diario')
    numero_contab = fields.Char('Numero')

    name = fields.Char(string='Nome/Razão', related="terceiro_id.name")#Nome Terceiro
    street = fields.Char(related="terceiro_id.street")

    phone = fields.Integer('Telefone', related="terceiro_id.phone")#para remover
    fax = fields.Integer('Fax', related="terceiro_id.fax")#para remover
    nif = fields.Integer('NIF', related="terceiro_id.nif")#para remover

    nif_pessoa = fields.Char(string="NIF", required=True, size=9, related="terceiro_id.nif_pessoa")
    telefone_pessoa = fields.Char(string="Telefone", required=True, size=7, related="terceiro_id.telefone_pessoa")
    fixo_pessoa = fields.Char(string="Fax", required=True, size=7, related="terceiro_id.fixo_pessoa")

    cod_terc = fields.Char('Codigo', related="terceiro_id.codigo")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)


    @api.model
    def create(self, vals):
        vals['n_documento'] = self.env['ir.sequence'].next_by_code('econtroconta.econtroconta.numero.abrev') or _('New')
        vals['numero'] = self.env['ir.sequence'].next_by_code('econtroconta.econtroconta.numero') or _('New')
        res = super(econtroconta, self).create(vals)
        #res.despon_doc_for_encontr()
        res.desvenc_doc_nao_enco()
        return res

    def _comput_line(self, line):
        return {
            'displlay_type': line.displlay_type,
            'state': 'draft',
        }

    # Calcula os tptais parciais
    @api.one
    @api.depends('tot_parc_debito', 'tot_parc_credito', 'reg_docum_ids.debito', 'reg_docum_ids.credito')
    def calc_tot_parc(self):
        self.tot_parc_debito = sum(line.debito for line in self.reg_docum_ids)
        self.tot_parc_credito = sum(line.credito for line in self.reg_docum_ids)
        self.tot_parc_saldar = self.tot_parc_debito - self.tot_parc_credito

    # Calcula os totais selecionados
    @api.one
    @api.onchange('reg_docum_ids.encontro')
    @api.depends('selecionado_debito', 'selecionado_credito', 'reg_docum_ids.debito', 'reg_docum_ids.credito')
    def calc_tot_select(self):
        docum = self.env['reg.docum'].search([('nome_terc', '=', self.terceiro_id.id), ('encontro', '=', False)])
        for rec in docum:
            if rec.encontro == True:
                self.selecionado_debito += sum(line.debito for line in rec)
                self.selecionado_credito += sum(line.credito for line in rec)
                self.selecionado_saldar = (self.selecionado_credito) - self.selecionado_debito

    """esse função foi criado para passar os valores do campo select 
    para select1 com objectivo de armanzenar valores no BD
    porque os campos que recebem valores apartir da função onchange não armanzena dados de uma forma simplis"""

    @api.multi
    @api.depends('selecionado_debito', 'selecionado_credito', 'selecionado_saldar')
    @api.onchange('selecionado_debito', 'selecionado_credito', 'selecionado_saldar')
    def atribui_val_selecion(self):
        self.selecionado_debito1 = self.selecionado_debito
        self.selecionado_credito1 = self.selecionado_credito
        if self.tot_parc_debito > self.tot_parc_credito:
           self.selecionado_saldar1 = -1 * (self.selecionado_saldar)
        elif self.tot_parc_debito < self.tot_parc_credito:
            self.selecionado_saldar1 = self.selecionado_saldar

    @api.multi
    @api.onchange('terceiro_id')
    def selecionar_documentos(self):
        domin = [('nome_terc', '=', self.terceiro_id.id), ('encontro', '=', False), ('prest_zerro', '=', True)]
        docum = self.env['reg.docum'].search(domin)
        list_of_docum = []
        for line in docum:
            data = self._comput_line(line)
            data.update(
                {'data_documento': line.data_documento, 'movimen_docum': line.movimen_docum,
                 'tipo_docum': line.tipo_docum,
                 'numeros_docum': line.numeros_docum, 'cod_documento': line.cod_documento,
                 'nome_terc': line.nome_terc, 'valorAsc': line.valorAsc,
                 'saldo_ord': line.saldo_ord, 'saldar': line.saldar,
                 'total': line.total, 'valorPago': line.valorPago, 'ldocaut': line.ldocaut,
                 'valor_ordpag': line.valor_ordpag, 'credito': line.credito, 'encontro': line.encontro,
                 'saldo': line.saldo, 'sequence': line.sequence, 'ordem_pago': line.ordem_pago,
                 'control_op': line.control_op, 'desting_doc_op': line.desting_doc_op,
                 'pago': line.pago, 'documentos': line.documentos, 'data_realise': line.data_realise,
                 'desting_doc_desp': line.desting_doc_desp, 'debito': line.debito,
                 'visualizar_no_tesorer': line.visualizar_no_tesorer, 'docPag': line.docPag,
                 'sem_cta_cte': line.sem_cta_cte})
            list_of_docum.append((1, line.id, data))

        return {'value': {"reg_docum_ids": list_of_docum}}



    @api.constrains('terceiro_id')
    def regular_docum(self):
        if self.terceiro_id:

            if self.tot_parc_credito > self.tot_parc_debito:#Marcar documento de cliente como pago
               docs = self.env['reg.docum'].search([('encontro', '=', True), ('desting_doc_vend', '=', True)])
               for record in docs:
                   record.cobrado = True
                   record.encont_docum_client = True
                   record.pago = True
               docuns = self.env['reg.docum'].search([('encontro', '=', True), ('desting_doc_desp', '=', True)])
               for rec in docuns:
                   rec.valor_encontro = self.selecionado_saldar1
                   #if rec.pago == False:
                      #rec.encontro = False
                      #rec.credito = rec.valor_encontro

               self.reg_docum_ids.compute_saldo()

            elif self.tot_parc_credito < self.tot_parc_debito: #Marcar documento de despesa como pago
                docs = self.env['reg.docum'].search([('encontro', '=', True), ('desting_doc_desp', '=', True)])
                for record in docs:
                    record.docPag = True
                    record.encont_docum_desp = True
                    record.pago = True
                docuns = self.env['reg.docum'].search([('encontro', '=', True), ('desting_doc_vend', '=', True)])
                for rec in docuns:
                    rec.valor_encontro = self.selecionado_saldar1
                self.reg_docum_ids.compute_saldo()

            else:#Marcar documento de cliente e despesa como pago
                domin = [('fornec_tercd', '=', self.terceiro_id.id), ('encontro', '=', True), ('desting_doc_vend', '=', True), ('desting_doc_desp', '=', True)]
                docum = self.env['reg.docum'].search(domin)
                for record in docum:
                    record.docPag = True
                    record.pago = True
                    record.cobrado = True

                self.reg_docum_ids.compute_saldo()
                #raise ValidationError('OK3')

    @api.one
    def despon_doc_for_encontr(self): #Desponibilizar documento para novo encontro
        docuns = self.env['reg.docum'].search([('encontro', '=', True), ('desting_doc_desp', '=', True)])
        for rec in docuns:
           if rec.pago == False:
              rec.encontro = False
              rec.credito = rec.valor_encontro
              #raise ValidationError('OK3')

    def desvenc_doc_nao_enco(self):
        doc_for_enc = self.env['reg.docum'].search([('nome_terc', '=', self.terceiro_id.id), ('encontro', '=', False)])
        if doc_for_enc:
            for doc in doc_for_enc:
                doc.encontro_conta_id = 0  # pass
