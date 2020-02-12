# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions, _


class fundos(models.Model):
    _name = 'fundos.fundos'
    _rec_name = 'name'
    _description = 'Financiamento'
    codigo = fields.Char(string="Código", required=True, copy=False, readonly=True, index=True,
                         default=lambda self: self._get_next_cod(), store=True, )
    name = fields.Char(tring="Nome")
    meio_monetario = fields.Many2one('monetario.monetario', string="Meioos",)
    codigo_servico = fields.Many2one('produto.produto')
    centro_custo= fields.Many2one('planconta.planconta')
    modelo = fields.Text()
    modelo_confecao = fields.Text()
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

    @api.model
    def _get_next_cod(self):
        sequence = self.env['ir.sequence'].search([('code', '=', 'fundos.fundos')])
        next = sequence.get_next_char(sequence.number_next_actual)
        return next

    @api.model
    def create(self, vals):
        vals['codigo'] = self.env['ir.sequence'].next_by_code('fundos.fundos') or _('New')
        obg = super(fundos, self).create(vals)
        return obg
