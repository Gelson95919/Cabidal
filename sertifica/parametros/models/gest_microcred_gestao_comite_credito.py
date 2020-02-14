# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions, _


class comiteCredito(models.Model):
    _name = 'comite.credito'
    _rec_name = 'name'
    _description = 'Comite Credito'
    codigo = fields.Char(string="Código", required=True, copy=False, readonly=True, index=True,
                         default=lambda self: self._get_next_cod(), store=True, )
    name = fields.Char(string="Nome")
    cargo = fields.Many2one('profissoes.profissoes')
    acta_id = fields.Many2one('acta.comite', string="Acta")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

    @api.model
    def _get_next_cod(self):
        sequence = self.env['ir.sequence'].search([('code', '=', 'comite.credito')])
        next = sequence.get_next_char(sequence.number_next_actual)
        return next

    @api.model
    def create(self, vals):
        vals['codigo'] = self.env['ir.sequence'].next_by_code('comite.credito') or _('New')
        obg = super(comiteCredito, self).create(vals)
        return obg