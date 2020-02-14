# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions,_


class freguesia(models.Model):
    _name = 'freguesia.freguesia'
    _rec_name = 'name'
    _description = 'Freguesia'
    codigo = fields.Char(string="Código", copy=False, readonly=True, index=True, store=True)
    name = fields.Char(tring="Nome")
    concelho_id = fields.Many2one('concelho.concelho', tring="Concelho")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)
    campos_relacional = fields.Integer(string="Campo relacional")


    """@api.model
    def _get_next_cod(self):
        sequence = self.env['ir.sequence'].search([('code', '=', 'freguesia.freguesia')])
        next = sequence.get_next_char(sequence.number_next_actual)
        return next

    @api.model
    def create(self, vals):
        vals['codigo'] = self.env['ir.sequence'].next_by_code('freguesia.freguesia') or _('New')
        obg = super(freguesia, self).create(vals)
        return obg"""
