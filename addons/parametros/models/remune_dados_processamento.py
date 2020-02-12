# -*- coding: utf-8 -*-

from odoo import models, fields, api

class instrumento(models.Model):
    _name = 'instromento.instromento'
    _rec_name = 'name'
    _description = 'Instromento'
    name = fields.Char(string="Descrição")
    data_tab = fields.Date(string="Data", default=fields.Date.today)
    numero_meses = fields.Integer(string="N Messes")
    horas_semanas = fields.Float(string="Hora Semanais")
    ins_reg_trab = fields.Char(string="Inst.rseg.trab")
    modo_process = fields.Selection([('diasUteisVar', 'Dias Úteis Var'), ('diasFixos', 'Dias Fixo'), ('diasUteisFixo', 'Dias Úteis Fixo'), ('valorHoraFixa', 'Valor Hora Fixa')], string="Modo Process", default = 'diasUteisVar')
    cod_comp_rem_id = fields.Many2one('compras.compras', string="Despesa/Remun")
    cod_comp_desc_id = fields.Many2one('compras.compras', string="Despesa/descont")
    plano_conta_id = fields.Many2one('planconta.planconta', string="Conta")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

class impostioIur(models.Model):
    _name = 'impostio.iur'
    _rec_name = 'name'
    _description = 'Imposto IUR'
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

    name = fields.Char(string="Descrição")
    descont_asoc_id = fields.Many2one('desconto.desconto', string="Desconto Asocido")
    taxaret = fields.One2many('taxa.retencao', 'id')
    rend_coletavel= fields.Many2many('rcir.rcir', string="Rend.Colet")
    imposto_reter = fields.Many2many('rcir.rcir', string="Imposto Reter")
    valor_minimo = fields.Integer(string="Valor Minimo")

class taxaRetencao(models.Model):
    _name = 'taxa.retencao'
    _rec_name = 'name'
    _description = 'Taxa Retencao'
    name = fields.Char(string="Taxas")
    cond = fields.Selection([('=', '='), ('>', '>'), ('<', '<'), ('>=', '>='), ('<=', '<=')], string="Cond")
    remuner= fields.Float(string="Remuneração")
    taxa = fields.Float(string="Taxa (%)")
    parcela_abater = fields.Float(string="Parcela a abater")
    enc_familiar = fields.Float(string="% Enc.Familiar")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

#Controlo de programador
class rcIr(models.Model):
    _name = 'rcir.rcir'
    _rec_name = 'name'
    _description = 'Rend.Colet e Imposto Reter'
    name = fields.Char('tipo rem Imposto')
    sim = fields.Boolean('diferenca')      #deferenciar a escolha de selecao no form Imposto IUR na aba Formulas de retencao
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)




#class rendimpost(models.Model):
#    _name = 'rendimpost.rendimpost'
#    _rec_name = 'name'
#    _description = 'New Description'  #Nao Vale a penas para remover

#    name = fields.Char()



class remuneracoes(models.Model):
    _name = 'remuneracoes.remuneracoes'
    _rec_name = 'id'
    _description = 'Remunerações'
    name = fields.Char(string="Descrição")
    tipo = fields.Selection([('valorTotal', 'Valor Total'), ('valorUnitario', 'Valor Unitario')], string="Tipo")
    valor = fields.Float(string="Montante")
    basico = fields.Boolean(string="Basico")
    percentual = fields.Boolean(string="Percentual")
    percent = fields.Selection([('valorBase', 'Valor Base'), ('valorliquido', 'Valor Liquido')], default = 'valorBase')
    selec_desconto = fields.Many2many('desconto.desconto', string="Select Descont")
    proces_desc_form_depen = fields.Boolean(string="Processar desconto de forma independente")
    cod_comp_desc_id = fields.Many2one('compras.compras', string="Despesa/Gasto")
    plano_conta_id = fields.Many2one('planconta.planconta', string="Conta")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)


class desconto(models.Model):
    _name = 'desconto.desconto'
    _rec_name = 'name'
    _description = 'Desconto'
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

    name = fields.Char(string="Descrição")
    valor = fields.Float(string="Montante")
    percentual = fields.Boolean(string="Percentual")
    aredondamento1 = fields.Selection([('centesimas', 'Centésimas'), ('decimas', 'Decimas'), ('Unidades', 'Unidades'), ('dezenasUnidade', 'Dezenas Unidade'), ('centesimasUnidades', 'Centésimas Unidades'), ('milharesresUnidades', 'Milhares Unidades')], string="Aredondamento")
    aredondamento3 = fields.Selection([('semArredondamento', 'Sem Arredondadmento'), ('defeito', 'Defeito'),
                                       ('imediatamenteInferior', 'Imidiatamente inferior'),
                                       ('imediatamenteSuprerior', 'Imidiatamente Superior')], string="aredond3", default = 'centesimas')
    cod_comp_desc_id = fields.Many2one('compras.compras', string="Despesa/Gasto")
    plano_conta_id = fields.Many2one('planconta.planconta', string="Conta")

    processamento_manual_id = fields.Many2one('processamento.manual.remuneracoes', string="Processamento Manualde Remuneracoes")


class faltas(models.Model):
    _name = 'faltas.faltas'
    _rec_name = 'name'
    _description = 'Faltas'
    name = fields.Char(string="Descrição")
    tipofalta = fields.Selection([('horas', 'Horas'), ('dias', 'Dias')], default = 'horas')
    calculo_em_dia = fields.Boolean()
    estafalta = fields.Selection([('naoAfeta', 'Não afecta nenhuma remuneração'), ('afetasTodas', 'Afetas todas as remuneração (com desconta paricial)'), ('apenasAfecta', 'Apenas afecta remuneração selecionadas')])
    com_desconto_parcial = fields.Many2many('remuneracoes.remuneracoes', string="Com Desconto Parcial")
    com_desconto_total = fields.Many2many('remuneracoes.remuneracoes', string="Com Desconto Parcial")
    aredondamento1 = fields.Selection([('centesimas', 'Centésimas'), ('decimas', 'Decimas'), ('Unidades', 'Unidades'),
                                       ('dezenasUnidade', 'Dezenas Unidade'),
                                       ('centesimasUnidades', 'Centésimas Unidades'),
                                       ('milharesresUnidades', 'Milhares Unidades')], string="Aredondamento", default = 'centesimas')
    aredondamento3 = fields.Selection([('semArredondamento', 'Sem Arredondadmento'), ('defeito', 'Defeito'),
                                       ('imediatamenteInferior', 'Imidiatamente inferior'),
                                       ('imediatamenteSuprerior', 'Imidiatamente Superior')], string="aredond3",  default = 'semArredondamento')
    plano_conta_id = fields.Many2one('planconta.planconta', string="Conta")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)


class horasExtras(models.Model):
    _name = 'horas.extras'
    _rec_name = 'name'
    _description = 'Horas Extras'
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

    name = fields.Char(string="Descrição")
    valor = fields.Float(string="Valor")
    percentual = fields.Boolean(string="Percentual")
    motivo = fields.Selection([('acrescimoInventuais', 'Acrescimo inventuais de trabalho'), ('forcamaior', 'Força Maior')])
    desconto = fields.Many2many('desconto.desconto', string="Desconto")
    aredondamento1 = fields.Selection([('centesimas', 'Centésimas'), ('decimas', 'Decimas'), ('Unidades', 'Unidades'),
                                       ('dezenasUnidade', 'Dezenas Unidade'),
                                       ('centesimasUnidades', 'Centésimas Unidades'),
                                       ('milharesresUnidades', 'Milhares Unidades')], string="Aredondamento",  default = 'centesimas')
    aredondamento3 = fields.Selection([('semArredondamento', 'Sem Arredondadmento'), ('defeito', 'Defeito'),
                                       ('imediatamenteInferior', 'Imidiatamente inferior'),
                                       ('imediatamenteSuprerior', 'Imidiatamente Superior')], string="aredond3",  default = 'semArredondamento')
    plano_conta_id = fields.Many2one('planconta.planconta', string="Conta")
    cod_comp_desc_id = fields.Many2one('compras.compras', string="Despesa")

class processamentoEspeciais(models.Model):
    _name = 'processamento.especiais'
    _rec_name = 'name'
    _description = 'Processamento Especiais'
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

    name = fields.Char(string="Descrição")
    processar_proporcional = fields.Boolean()
    remuneracoes = fields.Many2many('remuneracoes.remuneracoes')
    desconto = fields.Many2many('desconto.desconto')
