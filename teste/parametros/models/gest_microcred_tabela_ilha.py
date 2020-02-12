# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class ilha(models.Model):
    _name = 'ilha'
    _rec_name = 'name'
    _description = 'Ilha'

    name = fields.Char(tring="Nome")
    pais = fields.Many2one('pais.pais', tring="Pais")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

    codigo = fields.Char(string="Código", required=True, copy=False, readonly=True, index=True,
                         default=lambda self: self._get_next_cod(), store=True, )
    campos_relacional = fields.Integer(string="Campo relacional")

    @api.model
    def _get_next_cod(self):
        sequence = self.env['ir.sequence'].search([('code', '=', 'ilha')])
        next = sequence.get_next_char(sequence.number_next_actual)
        return next


    @api.model
    def create(self, vals):
        vals['codigo'] = self.env['ir.sequence'].next_by_code('ilha') or _('New')
        obg = super(ilha, self).create(vals)
        return obg
