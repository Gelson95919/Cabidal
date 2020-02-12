# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ordemEmbarque(models.Model):
     _name = 'ordem.embarque'
     _description = 'Ordem Embarque'
     nume = fields.Integer(string="Numero")
     viag = fields.Integer(string="Viagem")
     ano = fields.Date(string="Ano")
     navio_id = fields.Many2one('navios.navios', string="Navios")
     o_e_n = fields.Integer(string="O.E.Numero")
     porto_id_o = fields.Many2one('portos.escalas', string="Origem")
     porto_id_d = fields.Many2one('portos.escalas', string="Destino")
     terceito_id = fields.Many2one('terceiro.terceiro', string="Carregador")
     recebedor = fields.Char(string="Recebetor")
     data_emissao = fields.Date(string="Data Emissao", default=fields.Date.today)
     detalhes_carga_ids = fields.One2many('detalhes.carga', 'ordem_embarque_id', string="Detalhes de Caega")
     frete_liquido = fields.Float(string="Frete Liquido")
     iva_fret_liq = fields.Float(string="Iva Frete Liquido")
     estiva_desestiva = fields.Float(string="Estiva Desativa")
     iva_estiva_desestiva = fields.Float(string="Iva Estiva/Desestiva")
     impresso = fields.Float(string="impresso")
     iva_imprecio = fields.Float(string="iva imprecio")
     agencia = fields.Float(string="agencia")
     iva_agencia = fields.Float(string="iva agencia")
     outros = fields.Float(string="outros")
     total = fields.Float(string="total")
     obuservacao = fields.Text('Obuservação')
     pagamento = fields.Selection(
         [('pendente', 'Pendente'),
          ('cash', 'Cash'),
          ('credito', 'Credito'),
          ('pago_no_destino_conta_armador', 'Pago no destino/Conta do Armador')], default="cash")
     carga_cativa = fields.Boolean(string="Carga Cativa")
     incluir_em_ce = fields.Boolean(string="Incluir em CE")
     frete_liquido_calc = fields.Boolean(string="Frete Liquido")
     agencia_calc = fields.Boolean(string="%Agência")
     peso_calc = fields.Boolean(string="Peso")
     impresso_calc = fields.Boolean(string="Impresso")
     m3_calc = fields.Boolean(string="M3")
     estiva_desastiva_calc = fields.Boolean(string="Estiva/Desestiva")
     calcul_esti_desest = fields.Float()
     peacao_calc = fields.Boolean(string="Peação")
     calcul_peacao = fields.Float()
     taxa_amp = fields.Boolean(string="Taxa AMP")
     calc_equipamento = fields.Float()
     equipamento_calc = fields.Boolean(string="Equipamento")
     calc_trafego_destino = fields.Float()
     trafego_destino_calc = fields.Boolean(string="Tráfego no Destino")
     calcul_traf = fields.Float()
     trafego_calc = fields.Boolean(string="Tráfego")

class detalhesCarga(models.Model):
    _name = 'detalhes.carga'
    #_rec_name = 'name'
    _description = 'Detalhes de Carga'

    volume = fields.Float(string="Volume")
    mercadoria_id = fields.Many2one('mercadoria', string="Descrição de mercadorrias")
    peso_kg = fields.Float(string="Peso Kg", related="mercadoria_id.peso")
    peso_tons = fields.Float(string="Peso Tons")
    cubica_m3 = fields.Float(string="Cubica M³", related="mercadoria_id.cubicagem")
    incrie = fields.Float(string="% Incre.")
    estiva_desest = fields.Float(string="Estiva Deseste")
    total = fields.Float(string="Total ECV")
    ordem_embarque_id = fields.Many2one('ordem.embarque', string="Ordem Embarque")
