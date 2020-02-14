# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions, _


class agentes(models.Model):
    _name = 'agentes.agentes'
    _rec_name = 'name'
    _description = 'Agentes'
    codigo = fields.Char(string="Código", required=True, copy=False, readonly=True, index=True,
                         default=lambda self: self._get_next_cod(), store=True, )
    name = fields.Many2one('terceiro.terceiro', tring="Nome", domain=[('trabalhadores', '=', True)])
    operador = fields.Many2one('res.users', tring="Operador", required=True)
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)


    @api.model
    def _get_next_cod(self):
        sequence = self.env['ir.sequence'].search([('code', '=', 'agentes.agentes')])
        next = sequence.get_next_char(sequence.number_next_actual)
        return next

    @api.model
    def create(self, vals):
        vals['codigo'] = self.env['ir.sequence'].next_by_code('agentes.agentes') or _('New')
        obg = super(agentes, self).create(vals)
        return obg