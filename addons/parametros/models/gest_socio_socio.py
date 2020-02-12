# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class socio(models.Model):
    _name = 'socios.socios'
    _rec_name = 'name'
    _description = 'Sócios'

    name = fields.Char(string="Nome")
    nif = fields.Integer()
    numero_socio = fields.Integer(string="Numero")
    telefone = fields.Integer()
    movel = fields.Integer()
    e_mail = fields.Char()
    tipo = fields.Many2one('tipo.socio', string="Tipo Socio")
    incricao = fields.Date()
    activo = fields.Boolean(string="Selec")
    sequence = fields.Integer(default=10, help="Dá a seqüência desta linha ao exibir a fatura.")
    gerar_conta_corente_id = fields.Many2one('gerar.conta.corente')

    # campos do controlo
    type = fields.Selection(
        [('out_invoice', 'Fatura do cliente'), ('in_invoice', 'Vendor Bill'), ('out_refund', 'Customer Credit Note'),
         ('in_refund', 'Vendor Credit Note'), ('out_notdeb', 'Debit note'), ], readonly=True, index=True,
        change_default=True, default=lambda self: self._context.get('type', 'out_invoice'), track_visibility='always')
    displlay_type = fields.Selection([('line_section', 'section'), ('line_note', 'nota')], string='displlay')
    state = fields.Selection([('draft', 'Draft'), ('open', 'Open'), ('paid', 'Paid'), ('cancel', 'Cancelled'), ],
                             string='Status', index=True, readonly=True, default='draft', track_visibility='onchange',
                             copy=False)
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)


    @api.model
    def _get_doc_cobrar(self, numero_socio, name, tipo, activo):
        return {}
