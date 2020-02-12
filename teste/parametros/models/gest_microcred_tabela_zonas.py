# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions, _


class zonas(models.Model):
    _name = 'zonas.zonas'
    _rec_name = 'name'
    _description = 'Zonas'

    name = fields.Char(tring="Nome")
    concelho = fields.Many2one('concelho.concelho', tring="Concelho")
    freguesia = fields.Many2one('freguesia.freguesia', tring="Freguesia")

    codigo = fields.Char(string="Código", required=True, copy=False, readonly=True, index=True,
                         default=lambda self: self._get_next_cod(), store=True, )
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)
    campos_relacional = fields.Integer(string="Campo relacional")
    @api.model
    def _get_next_cod(self):
        sequence = self.env['ir.sequence'].search([('code', '=', 'zonas.zonas')])
        next = sequence.get_next_char(sequence.number_next_actual)
        return next

    @api.model
    def create(self, vals):
        vals['codigo'] = self.env['ir.sequence'].next_by_code('zonas.zonas') or _('New')
        obg = super(zonas, self).create(vals)
        return obg

