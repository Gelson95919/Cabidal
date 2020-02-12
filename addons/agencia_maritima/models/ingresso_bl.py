# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ingressoBl(models.Model):
    _name = 'maritima.ingresso.bl'
    _description = "Ingresso BL"

    navio_id = fields.Many2one('navios.navios')
    data_entrada = fields.Date(string="Data Entrada", default=fields.Date.today)
    conhec_embarque = fields.Char(string="Conhecimento de Embarque")
    contra_marca = fields.Char(string="Contra Marca")
    referencia_manifesto = fields.Char(string="Referência Manifesto")
    #est_aduaneira = fields.Many2one('', string="Est.Aduaneira")
    porto_ori_id = fields.Many2one('portos.escalas', string="Porto Origem")
    desc_porto_orig = fields.Char(string="Descricao Porto Origem", related='porto_ori_id.name', readonly=True, store=True)
    porto_dest_id = fields.Many2one('portos.escalas', string="Porto Destino")
    desc_porto_dest = fields.Char(string="Descricao Porto Destino", related='porto_dest_id.name', readonly=True, store=True)
    terceiro_id = fields.Many2one('terceiro.terceiro', string="Terceiro")
    endereco = fields.Char(string="Endereco", related="terceiro_id.street2", readonly=True, store=True)
    tipo_tt = fields.Many2one('tipott', string="Tipo TT")
    fluxo_tt = fields.Many2one('fluxott', string="Fluxo TT")
    contentor_ids = fields.Many2many('contentor', 'maritima_ingresso_bl_id', string="Contentor")
    cod_ref_carga = fields.Char(string="Cod.Ref.Carga")
    pertences_ids = fields.Many2many('pertences', 'maritima_ingresso_bl_id')
    despesas_origem = fields.Float(string="Despesas Origem")
    despesas_destino_ids = fields.One2many('depesas.destino', 'maritima_ingresso_bl_id')
    taxa_agencia= fields.Float(string="Taxa Agencia")
    taxa_descarga= fields.Float(string="Taxa Descarga")
    taxa_transitario = fields.Float(string="Taxa Transito")
    iva_pertences = fields.Float(string="Iva Pertence")
    criterio_defeirto = fields.Char(string="Credito x Desfeito")#Este campo e um campo relacional, que a sua tabela , ainda nao foi encontrada
    comissao = fields.Integer(string="Comissao")
    tipo_valo = fields.Selection([('valor_percentual', 'Valor Percentual'), ('valor_fixo', 'Valor Fixo'),
                                  ('valor_a_repartir_x_criterio', 'Valor a Repartir x Criterio'),
                                  ('valor_a_repartir_equit', 'Valor a Repartir Equit.')], default="valor_percentual")
    base_arendond = fields.Integer(string="Base Aredondamento")
    aredondamento = fields.Selection([('unidade', 'Unidade'), ('desimas', 'Désimas'), ('centesimas', 'Centésimas'),
                                      ('dezena_unidade', 'Dezena Unidade'), ('centenas_unidade', 'Centenas Unidade'), ('milharis_unidade', 'Milharis Unidade')], default="unidade")



class tipoTt(models.Model):
    _name = 'tipott'
    _rec_name = 'name'
    _description = 'Tipo TT'
    name = fields.Char(string='Descrição')

class fluxoTt(models.Model):
    _name = 'fluxott'
    _rec_name = 'name'
    _description = 'Fluxo TT'

    name = fields.Char(string='Descrição')

class contentor(models.Model):
    _name = 'contentor'
    #_rec_name = 'name'
    _description = 'Contentor'

    titulo_transporte = fields.Char(string='Titulo Transporte')
    numero_sequencia = fields.Char(string='Numero sequencia')
    referencia = fields.Char(string='Referencia')
    tipo = fields.Char(string='Tipo')
    indicador = fields.Char(string='Indicador')
    maritima_ingresso_bl_id = fields.Many2one('maritima.ingresso.bl', string="maritima ingresso bl")
    pertences_id = fields.Many2one('pertences')
    manifesto_carga_id= fields.Many2one('manifesto.carga', string="Manifesto de Carga")
    titulo_transporte_id = fields.Many2one('transporte', string="Titulo Transporte")

class pertences(models.Model):
    _name = 'pertences'
    _rec_name = 'name'
    _description = 'Pertences'

    name = fields.Char(string="Nome")
    ref_pertences = fields.Char(string="Referência Pertences")
    numero_trans = fields.Integer(string="Nº")
    nif = fields.Integer(string="NIF")
    endereco = fields.Text(string="Endereco")
    nome = fields.Char(string="Nome")
    endereco_notif = fields.Text(string="Endereco")
    contentor_ids = fields.Many2many('contentor', 'pertences_id')
    embalagem = fields.Selection([('be', 'BE Atados'), ('bu', 'BU Barrica'), ('ba', 'BA Barril'), ('cx', 'Bidom'), ('bb', 'Babine'), ('bl', 'BL Boioes')])
    volumes = fields.Integer(string="Volume")
    peso = fields.Float(string="Peso(Kg)")
    cubicagem = fields.Float(string="Medida m3")
    marca = fields.Text(string="Marca")
    descr_carga = fields.Text(string="Descricao")
    informacao= fields.Text(string="informacao")
    valor_frete= fields.Float(string="Valor Frete")
    moeda_id = fields.Many2one('unimedida.unimedida', string="Moeda")
    maritima_ingresso_bl_id = fields.Many2one('maritima.ingresso.bl', string="maritima ingresso bl")

class despesaDestino(models.Model):
    _name = 'depesas.destino'
    _rec_name = 'name'
    _description = 'Despesas no Destino'

    name = fields.Char(string='Descrição')
    tom_m3 = fields.Float(string="Tom./m3")
    valor_documento = fields.Float(string="Valor Documento")
    maritima_ingresso_bl_id = fields.Many2one('maritima.ingresso.bl', string="maritima ingresso bl")
