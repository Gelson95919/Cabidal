
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class funcionarioRemuneracoes(models.Model):
    _name = 'funcionario.remuneracoes'
    _description = 'Funcionário'
    #_rec_name = 'id'
    name = fields.Char(string="Nome")
    image = fields.Binary('Logo')
    morada = fields.Char(string="Morada")
    localidade = fields.Char(string="Localidade")
    codigo_posta = fields.Integer(string="Código Postal")
    numero = fields.Integer(string="Numero")
    telefone = fields.Integer(string="Telefone")
    telemovel = fields.Integer(string="Telemóvel")
    pai = fields.Char(string="Pai")
    mae = fields.Char(string="Mae")
    data_nascimento = fields.Date(string="data")
    concelho = fields.Char(string="Concelho")
    estado_civil = fields.Selection([('solteiro', 'Solteiro'), ('casado', 'Casado')], default="solteiro")
    sexo = fields.Selection([('feminino', 'Feminino'), ('masculino', 'Masculino')], default="feminino")
    nacionalidade = fields.Many2one('nacionalidade.nacionalidade', string="Nacionalidade")
    numero_dados_fiscais = fields.Integer(string="Numero")
    data = fields.Date(string="Data")
    l_emissao = fields.Char(string="L.Emicao")
    reprticao_financas = fields.Many2one('reposicao.financas', string="Reparticao Financas")
    tabela_iur = fields.Many2one('impostio.iur', string="IUR")
    nif = fields.Integer(string="NIF")
    nif_conjugue = fields.Integer(string="NIF Conjugue")
    conjugue = fields.Char(string="Conjugue")
    entidade_patronal = fields.Char(string="Entidade Patronal")
    filhos_ids = fields.One2many('filhos.dados.fiscais', 'funcionario_id')
    situacoes = fields.Many2one('situacoes.situacoes', string="Situacoes")
    disponibilidade = fields.Selection([('activo', 'Activo'), ('nao_deponivel', 'Não disponível'), ('outro', 'Outro')], default="activo", string="Disponibilidade")
    tipo_docum = fields.Many2one('deocumento.ingresso', string="Tipo Documento")
    numero_arquivo = fields.Integer(string="Numero")
    data_inicio = fields.Date(string="Data Inicio")
    data_fim = fields.Date(string="Data Fim")
    data_emisao = fields.Date(string="Data Emicao")
    motivo = fields.Many2one('motivo.demissao', string="Motivo")
    historial_ids = fields.One2many('historial.arquivos', 'funcionario_id')
    proficao_id = fields.Many2one('profecoes.profecoes', string="Proficoes")
    catigoria_proficional_id = fields.Many2one('categorias.categorias', string="Categoria Proficionais")
    habilitacoes_literaria_id = fields.Many2one('habilitacoes.habilitacoes', string="Categoria Proficionais")
    seguros_id = fields.Many2one('seguros.seguros', string="Seguros")
    segu_social_id = fields.Many2one('seguranca.social', string="Seguranca Social")
    sindicato_id = fields.Many2one('sindicato.sindicato', string="Sindicato")
    numero_seguro = fields.Integer(string="Número")
    intrumento_id = fields.Many2one('instromento.instromento', string="Intromento")
    modo_process = fields.Selection([('dias_uteis_var', 'Dias Úteis Var'), ('dias_fixo', 'Dias Fixos'), ('dias_uteis_fixos', 'Dias Úteis Fixos'), ('valor_hora_fixa', 'Valor Hora Fixa')], string="Modo Process")
    horas_semanas = fields.Float(string="Horas Semanas")
    remuneracoes_salari_ids = fields.One2many('remuneracoes.salario', 'funcionario_id')
    descont_salari_ids = fields.One2many('desconto.salario', 'funcionario_id')
    modo_pagamento = fields.Selection([('cheque', 'Cheque'), ('dinheiro', 'Dinheiro'), ('tranfirencia', 'Transferência')], string="Modo Pagamento")
    meio_monetario_id = fields.Many2one('monetario.monetario', string="Meio")
    conta_trabalhador = fields.Char(string="Conta Trabalhador")
    banco_id = fields.Many2one('entbanc.entbanc', string="Banco")
    departamento_id = fields.Many2one('departamento.area', string="Departamento")
    notas = fields.Text(string="Notas")



class descontoSalario(models.Model):   # Aba Salario
    _name = 'desconto.salario'
    _inherit = 'funcionario.remuneracoes'
    #_rec_name = 'name'
    _description = 'Desconto - Salario'

    valor = fields.Float(string="Montanta")
    descont_id = fields.Many2one('desconto.desconto', string="Código")
    descre_descont = fields.Char(string="Descrição", related="descont_id.name")
    terceiro = fields.Char(string="Terceiro")
    funcionario_id = fields.Many2one('funcionario.remuneracoes')
    processamento_manual_id = fields.Many2one('processamento.manual.remuneracoes', string="Processamento Manualde Remuneracoes")



class remunSalario(models.Model):     # Aba Salario
    _name = 'remuneracoes.salario'
    _inherit = 'funcionario.remuneracoes'
    #_rec_name = 'name'
    _description = 'Remuneracoes - Salario'

    valor = fields.Float(string="Montanta")
    remuneracoes_id = fields.Many2one('remuneracoes.remuneracoes', string="Código")
    descre_remuner = fields.Char(string="Descrição", related="remuneracoes_id.name")

    funcionario_id = fields.Many2one('funcionario.remuneracoes')
    processamento_manual_id = fields.Many2one('processamento.manual.remuneracoes', string="Processamento Manualde Remuneracoes")
    pagamentos_id = fields.Many2one('processamento.pagamento.remuneracoes')

class filhosDadosFiscais(models.Model): # Aba dados Fiscais
    _name = 'filhos.dados.fiscais'
    _rec_name = 'name'
    _description = 'Filhos Dados Fiscais'

    name = fields.Char(string="Nome")
    data_nascimento = fields.Date(string="Data Nascimento")
    numero_bilhete_identidade = fields.Integer(string="Numero Bilhete Identidade")
    funcionario_id = fields.Many2one('funcionario.remuneracoes')

class historialArquivos(models.Model): # Aba aba arquivos
    _name = 'historial.arquivos'
    _rec_name = 'name'
    _description = 'Historial'

    name = fields.Char(string="Descrição")
    data = fields.Date(string="Data")
    documento = fields.Char(string="Documento")
    notas = fields.Text(string="Notas")
    funcionario_id = fields.Many2one('funcionario.remuneracoes')



