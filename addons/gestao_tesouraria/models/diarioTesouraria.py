# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class folhaTesouraria(models.Model):
    _name = 'folha.tesouraria'
    _rec_name = 'movimento'
    _description = 'Folha Tesouraria'

    #descricao = fields.Char(string="Folha", related="monetario_ids.name",)
    folha = fields.Many2one('monetario.monetario', tring='Folha')
    diario = fields.Many2one('diario.diario', string='Diario', related="folha.diario", store=True,
                             readonly=True)
    name_diario = fields.Char('Descrição', related="folha.name_diario", store=True)

    conta = fields.Many2one('planconta.planconta', string='Conta', related="folha.conta", store=True,
                            readonly=True)

    name = fields.Char('Descrição')#, required=True
    codigo = fields.Char(string="Documento", store=True, copy=True)
    fechado = fields.Selection([('1', 'Sim'), ('2', 'Não')], string='Fechado', default='2')

    data = fields.Date(string='Data Fecho', default=fields.Date.today)#
    movimento = fields.Char(string='Movimento', copy=False, )  #required=True,  readonly=True, index=True, default=lambda self: _('New')

    terceiro_id = fields.Many2one('terceiro.terceiro', string='Terceiro')
    tot_parc_entrada = fields.Float(string="Entrada", compute="_compute_val_tot")#
    tot_parc_saida = fields.Float(string="Saida", compute="_compute_val_tot")#

    sald_sigu = fields.Float(string='Saldo Seguinte', compute="_compute_val_tot", store=True)#
    saldo_ant = fields.Float(string='Saldo Anterior', readonly=True, store=True)#

    total_control_entrada = fields.Float(string='Total Entrada', compute="_compute_val_tot", store=True)#
    total_control_saida = fields.Float(string='Total Saida', store=True, compute="_compute_val_tot")#
    pagamento_recebimento_ids = fields.One2many('pagamento.recebimento', 'folha_tesouraria_id', copy=True, store=True)

    detalhes_diario_teso_ids = fields.One2many('detalhes.diario.tesouraria', 'folha_tesouraria_id', copy=True, store=True)

    # controlos
    displlay_type = fields.Selection([('line_section', 'section'), ('line_note', 'nota')], string='displlay')
    state = fields.Selection([('draft', 'Draft'), ('open', 'Open'), ('paid', 'Paid'), ('cancel', 'Cancelled'), ])
    movimentado = fields.Boolean(string="Movimentado")
    fechado_bol = fields.Boolean(string="Fechado Bol")
    valor_movimento = fields.Float(string="Valor") #Valor do movimento "Entrada, Saida, Tranferencia"

    id_meios_monetarios = fields.Integer(string="idmonetarios", related="folha.id")
    terceiro_id_doc_conta_corente_receb = fields.Many2one('terceiro.terceiro', string='Terceiro', store=True)
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

    dados_antigo = fields.Boolean(string="Dados Antigo")  # se True porque os dados são antigo

    @api.one
    @api.constrains('dados_antigo')
    def val_dados_antig(self):  # Verificar se o dados e antigo ou não
        if self.dados_antigo == True:
            pass
           #raise ValidationError(
           #    'Dados antigo, ha algumas informações que precisam ser modificado, contacta o adminstrador de sistema se consideras-te que é um erro ')



    ccodmed = fields.Char()
    cnummov = fields.Char()
    cnummov_int = fields.Integer()
    canocie = fields.Char()
    dfeccie = fields.Char()

    def mod_det(self):
        #pass
        ct = self.env['folha.tesouraria'].search([('id', '>=', 1)])
        for c in ct:
            c.cnummov_int = c.cnummov

        pagamento = self.env['pagamento.recebimento'].search([('id', '>=', 1)])
        for p in pagamento:
            p.cnumfec_int = p.cnumfec1

            #if p.CCODMED == '02':
            #    p.folha_tesouraria_id = 2
            #if p.CCODMED == '03':
            #    p.folha_tesouraria_id = 3
            #if p.CCODMED == '04':
            #    p.folha_tesouraria_id = 4
            #if p.CCODMED == '05':
            #    p.folha_tesouraria_id = 5
            #if p.CCODMED == '06':
            #    p.folha_tesouraria_id = 6
            #if p.CCODMED == '07':
            #    p.folha_tesouraria_id = 7
            #if p.CCODMED == '08':
            #    p.folha_tesouraria_id = 8
            #if p.CCODMED == '09':
            #    p.folha_tesouraria_id = 9
            #if p.CCODMED == '10':
            #    p.folha_tesouraria_id = 10
            #if p.CCODMED == '11':
            #    p.folha_tesouraria_id = 11


        #=================================
             #c.movimento = c.cnummov
             #if c.fechado_bol == True:
             #    c.fechado = '1'
             #else:
             #    c.fechado = '2'
        #===============================
        #    if c.ccodmed == '01':
        #        c.folha = 1
        #    if c.ccodmed == '02':
        #        c.folha = 2
        #    if c.ccodmed == '03':
        #        c.folha = 3
        #    if c.ccodmed == '04':
        #        c.folha = 4
        #    if c.ccodmed == '05':
        #        c.folha = 5
        #    if c.ccodmed == '06':
        #        c.folha = 6
        #    if c.ccodmed == '07':
        #        c.folha = 7
        #    if c.ccodmed == '08':
        #        c.folha = 8
        #    if c.ccodmed == '09':
        #        c.folha = 9
        #    if c.ccodmed == '10':
        #        c.folha = 10
        #    if c.ccodmed == '11':
        #        c.folha = 11


    @api.one
    @api.depends('pagamento_recebimento_ids.vervalor_total_receb', 'pagamento_recebimento_ids.valor_total_pag',
                 'total_control_entrada', 'sald_sigu')
    def _compute_val_tot(self):
        self.tot_parc_entrada = sum(line.vervalor_total_receb for line in self.pagamento_recebimento_ids if line.select == True)
        self.tot_parc_saida = sum(line.valor_total_pag for line in self.pagamento_recebimento_ids)
        self.sald_sigu = self.saldo_ant + self.tot_parc_entrada
        self.total_control_entrada = self.sald_sigu
        self.total_control_saida = self.sald_sigu


    #@api.depends('sald_sigu')
    #def cal_saldo_sigu_tot_co(self):


    @api.one
    @api.onchange('reg_docum_ids.encontro')
    @api.depends('tot_parc_entrada', 'tot_parc_saida', 'sald_sigu')
    def calc_tot_select(self):
        docum = self.env['reg.docum'].search([('nome_terc', '=', self.terceiro_id.id), ('encontro', '=', False)])
        for rec in docum:
            if rec.encontro == True:
                self.selecionado_debito += sum(line.debito for line in rec)
                self.selecionado_credito += sum(line.credito for line in rec)
                self.selecionado_saldar = (self.selecionado_credito) - self.selecionado_debito

    def _comput_line(self, line):
        return {
            'displlay_type': line.displlay_type,
            'state': 'draft',
        }

    @api.one
    def fechar(self):
        self.write({'fechado': '1'})
        #if self.fechado == '1':
        #    new_lancamento = self.env['lancamento_diario.lancamento_diario']
        #    lanca = new_lancamento.create({'diario': self.diario.id, 'data': self.data, 'valor': self.valor_movimento, 'name_diario': self.name_diario,
        #                                   'terceiro_id_doc_conta_corente_receb': self.terceiro_id_doc_conta_corente_receb.id})


        folh_obj = self.env['monetario.monetario'].search([('id', '=', self.folha.id)])
        new_folh_obj = self.env['folha.tesouraria']
        for f in folh_obj:
            folha = new_folh_obj.create({
                'folha': f.id,
                'saldo_ant': f.saldo_inicial,
                'name': f.name,
            })
            return folha



    @api.model
    def create(self, vals):
        vals['movimento'] = self.env['ir.sequence'].next_by_code('folha.tesouraria.mov') or _('New')
        res = super(folhaTesouraria, self).create(vals)
        return res


#Ivalido
class detalhesDiarTesouraria(models.Model):
    _name = 'detalhes.diario.tesouraria'
    #_rec_name = 'name'
    _description = 'Detalhes Diario'

    ordem = fields.Char(string="Ordem")
    data = fields.Date(string="Data")
    detalhes = fields.Char(string="Detalhes")
    entrada = fields.Float(string="Entrada")
    saida = fields.Float(string="Saida")
    selec = fields.Char(string="Selec", default=True)
    folha_tesouraria_id = fields.Many2one('folha.tesouraria')





