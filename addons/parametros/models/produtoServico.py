# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class produto(models.Model):
    _name = 'produto.produto'
    _description = 'Produtos/Servico'
    # date_release = fields.Date('Data de lançamento')
    name = fields.Char('Descrição', required=True)
    _rec_name = 'codigo'
    # codigo_optativo = fields.Char(string='Codigo Optativo')
    codigo = fields.Char(string="Codigo", copy=False, readonly=False, index=True, # required=True,
                         default=lambda self: _('New'))
    montante = fields.Float(string='Montante')
    iva = fields.Many2one('iva.iva', string='IVA')
    faturacao_conta_outrem = fields.Boolean(string='Facturação por Canta de Outrem')
    adiantamento_cliente = fields.Boolean(string='Adiantamento de Cliente')
    utilizar_conf_processo = fields.Boolean(string='Utilizar Conf.De Processo')
    conta_artigo = fields.Many2one('planconta.planconta', string='Conta Artigo', domain=[('grupo', '=', False)])
    centro_custo = fields.Many2one('planconta.planconta.analitica', string='Centro Custo')
    conta_iva = fields.Many2one('planconta.planconta', string='Conta Iva')
    fluxo_caixa = fields.Many2one('planteso.planteso', string='Fluxo de Caixa')
    codigo_iva = fields.Many2one('planiva.planiva', string='Codigo Iva')
    mudar_tipo_movimento = fields.Boolean(string='Mudar Tipo Movimento se Negativo')
    detalhes = fields.Text('Detalhes', sanitize=True, strip_style=False)
    sem_provistos = fields.Boolean(string="Sem Proveitos")
    rubrica_conta_escala = fields.Boolean(string="Rubrica Conta escala")
    tipo = fields.Selection([('1', 'Despesas Navio Nacional'), ('2', 'Despesas Navio Estrangeiro'), ('3', 'Receitas')])
    rubrica = fields.Many2one('agenc.rubrica.conta.escala')
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

    ccodart = fields.Char()
    ccodart1 = fields.Integer()
    ccodcon = fields.Char()


    # campo de controlo
    type = fields.Selection([('1', 'Produtos/Servico'), ('2', 'Faturação/Conceito'),
         ('3', 'Conceito Recebimento'), ('4', 'Microcredito/Serviço')],
        readonly=True, index=True, change_default=True,
        default=lambda self: self._context.get('type', '1'),
        track_visibility='always')
    _sql_constraints = [
        ('codigo', 'unique(codigo)', 'Codigo already exists'),
    ]

    @api.model
    def create(self, vals):
        vals['codigo'] = self.env['ir.sequence'].next_by_code('produt.codigo') or _('New')
        codigo = vals.get('codigo')# obter codigo da forma
        if codigo:
            pass  # você pode fazer algo com ele, por exemplo, pesquisando
        res = super(produto, self).create(vals)
        # res.gerar()
        return res # finalmente, chame o método create da superclasse e crie o registro depois que você terminar

