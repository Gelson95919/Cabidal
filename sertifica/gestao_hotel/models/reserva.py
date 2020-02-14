# -*- coding: utf-8 -*-


#from odoo import models, fields, api, tools

from datetime import timedelta
from odoo import models, fields, api, exceptions
import sys
from odoo.exceptions import ValidationError


class reserva(models.Model):
    _name = 'reserva'
    #_rec_name = 'nome_cliente'
    _description = 'Reserva'


    habitacao_id = fields.Many2one('habitacoes.habitacoes', string="Quarto")
    tarifa_id = fields.Many2one('tarifario.tarifario', string="Tarifa")
    chegada = fields.Date(string="Chegada")
    saida = fields.Date(string="Saida")
    num_noite = fields.Integer(string="Numero Noite")
    cliente_ids = fields.Many2many('clientes.clientes', string="Pessoas")
    nome_cliente = fields.Char(related='cliente_ids.name')
    nume_pessoa = fields.Integer(string="Numero Pessoas")
    num_criancas = fields.Integer(string="Numero Crianças")
    obs =fields.Text(string="OBS")

    #-------------------------------------------------------------------------------------------------------
    #attendee_ids = fields.Many2many('res.partner', string="Attendees")
    start_date = fields.Date(string="Entrada")
    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')
    end_date = fields.Date(string="Saida", store=True, compute='_get_end_date', inverse='_set_end_date')
    duration = fields.Integer(digits=(6, 2), help="Duration in days", compute='_set_end_date')
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    ocupantes_ids = fields.One2many('ocupantes', 'reserva_id')
    consumos_ids = fields.One2many('consumos', 'reserva_id', string="Consumos")
    pagamentos_ids = fields.One2many('pagamentos', 'reserva_id', string="Pagamentos")

    # -------------------------------------------------------------------------------------------------------
    terceiro_id = fields.Many2one('terceiro.terceiro', string="Terceiro")
    tipo_pagamento  = fields.Selection([
        ('pronto_pagamento', 'Pronto Pagamento'),
        ('credito', 'Credito'),
        ('transferir', 'Transferir'),
        ], default="pronto_pagamento")
    hab_id = fields.Many2one('habitacoes.habitacoes', string="HAbitação")
    imprimo_recibo = fields.Boolean(string="Imprimir Recibo")
    gerar_factura = fields.Boolean(string="Gerar Factura")

    active_mostra_btn_chek_in = fields.Boolean(compute='_compute_control', readonly=True, index=True,) # CONTROLA A VIZIBILIDADE DO BOTOM CHECK-IN
    realizar_check_in = fields.Boolean(compute='check_in', readonly=True, index=True,)# FUNCAO REALIZAR CHECK-IN
    check_in_feito = fields.Boolean(string="Check-in")  # CHECK-IN FEITO
    controlo = fields.Boolean(defautl=True, string="Controlo") #controla o BTN confirmar
    feixo_caixa_id = fields.Many2one('feixo.caixa', string="Feixo caixa")
    feixo_dia_id = fields.Many2one('feixo.diua', string="Feixo dia")
    montante_check_kin = fields.Float(string="Montante", compute="_compute_montante") # de form fecho de caixa tree check-in

    """
        Este campo de seleção contém todos os valores possíveis para a barra de status.
        A primeira parte é o valor do banco de dados, o segundo é a string que é mostrada. Exemplo:
        ('finished','Done'). 'finished 'é a chave do banco de dados e' Done 'o valor mostrado para o usuário
    """
    state = fields.Selection([
        ('concept', 'Conceito'),
        ('consumo', 'Consumir'),
        ('pagamento', 'Pagamento'),
        ('checkout', 'Check-out'),
        ('finished', 'Feita'),
        ])

    #Mostra quadro pagamento
    mostra_quadro_pag = fields.Selection([('pagos', 'Pagos'), ('ocultar_quadro_pagou', 'Ocultar Pag'), ])

    # Controlo de mostrar os botoens
    mostra_btn_consumo = fields.Selection([('mostrabtnConsumo', 'Mostra BTN Consumo'), ('ocultarBtnCons', 'Ocultar BTN'), ])

    # Mostra Controlo pagamento
    forma_pagamento = fields.Selection([('contiudos', 'Mostra Contiudos'), ('oculta_itens', 'Ocultar Itens'),],default='oculta_itens')

    # FUNCAO REALIZAR CHECK-IN
    # Esta função é acionada quando o usuário clica no botão
    # 'Definido para o conceito



    @api.one
    @api.depends('consumos_ids.total')
    def _compute_montante(self):
        self.montante_check_kin = sum(line.total for line in self.consumos_ids)


    @api.one
    def check_in(self):
        self.write({'state': 'concept', })
        self.write({'mostra_quadro_pag': 'ocultar_quadro_pagou', })
        self.controlo = False


    @api.multi
    def comfirmar_checkin(self):
       self.write({'mostra_btn_consumo': 'mostrabtnConsumo'})
       # here you have values from form and context
       #if len(self.ocupantes_ids) != len(str(self.nume_pessoa)):
            #raise ValidationError('O ocupantes maior que  numero de pessoas!')
       if self.consumos_ids != '':
           self.write({'state': 'pagamento'})
           self.controlo = True
       return {'type': 'ir.actions.act_window_close'}

    @api.multi
    def comfirmar_pagamento(self):
        if self.pagamentos_ids and self.consumos_ids != '':
            self.write({'state': 'checkout'})
        return {'type': 'ir.actions.act_window_close'}

    @api.multi
    def confirmar_checkout(self):
        if self.terceiro_id != '':
            self.write({'state': 'finished'})
        return {'type': 'ir.actions.act_window_close'}

    @api.one
    def consumo(self):
        self.write({'state': 'consumo', })
        self.write({'mostra_quadro_pag': 'ocultar_quadro_pagou', })
        self.controlo = False


    @api.one
    def pagamentos(self):
        self.write({'mostra_quadro_pag': 'pagos', })

        if self.consumos_ids != '':
            self.write({'state': 'pagamento'})

    @api.one
    def check_out(self):
        self.write({'state': 'checkout'})

    @api.depends('start_date', 'end_date')
    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue

            # adicione um dia para obter 5 dias
            # self.start_date = fields.Date.from_string(r.start_date)
            # self.end_date = fields.Date.from_string(r.end_date)
            r.duration = (self.end_date - self.start_date).days + 1

    # CONTROLA A VIZIBILIDADE DO BOTOM CHECK-IN
    def _compute_control(self):
        if self.cliente_ids != '':
            self.active_mostra_btn_chek_in = True

    @api.model
    def _get_fatura_price(self, habitacao_id, cliente_ids, start_date, end_date, montante_check_kin ,  nume_pessoa, hab_id, num_criancas):
        return {}



class ocupantes(models.Model):
    _name = 'ocupantes'
    #_rec_name = 'name'
    _description = 'Ocupantes'

    name = fields.Char(string="Nome")
    idade = fields.Integer(string="Idade")
    tipo = fields.Selection([('crianca', 'Crianças'), ('adulto', 'Adulto'), ('terceira_idade', 'Terceira Idade')])
    doc_ident = fields.Char(string="Doc.Identidade")
    pais_id = fields.Many2one('pais.pais', string="País")
    reserva_id = fields.Many2one('reserva')





class consumos(models.Model):
    _name = 'consumos'
    #_rec_name = 'name'
    _description = 'Consumos'

    data = fields.Date(string="Data", default=fields.Date.today)
    tipo_consumo_id = fields.Many2one('tipo.consumo', string="Descrição")
    montante = fields.Float(string="Montante", related="tipo_consumo_id.montante")
    valor = fields.Float(string="Valor")
    iva = fields.Many2one('iva.iva', string="IVA", related='tipo_consumo_id.iva_percent')
    taxa = fields.Float(string='Taxa', related='iva.taxa')
    total = fields.Float(string="Total", compute='calc_total')
    obs = fields.Text(string="OBS")
    reserva_id = fields.Many2one('reserva')

    taxa_porcent = fields.Float(string="Taxa")#para converter valor de iva

    @api.one
    @api.depends('montante', 'valor')
    def calc_total(self):
        for line in self:
            line.taxa_porcent = line.taxa / 100
            line.total = (line.montante + line.valor) + 0.15



class pagamentos(models.Model):
     _name = 'pagamentos'
     #_rec_name = 'name'
     _description = 'Pagamentos Hoteis'

     tipo_pagamento_id = fields.Many2one('tipo.pagamento', string="Pagamento")
     data = fields.Date(string="Data", default=fields.Date.today)
     montante = fields.Float(string="Montante")
     obs = fields.Text(string="OBS")
     reserva_id = fields.Many2one('reserva')