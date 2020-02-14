# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions, _


class lugares(models.Model):
    _name = 'lugares.lugares'
    _rec_name = 'name'
    _description = 'Lugares'

    name = fields.Char(string="Nome")
    concelho_id = fields.Many2one('concelho.concelho', string="Concelho")
    freguesia_id = fields.Many2one('freguesia.freguesia', string="Freguesia")
    zona_id = fields.Many2one('zonas.zonas', string="Lugares")
    ilha_id = fields.Many2one('ilha', string="Ilha")
    name_ilha = fields.Char(tring="Nome", related="ilha_id.name", store=True)
    codigo = fields.Char(string="Código", required=True, copy=False, index=True,
                         default=lambda self: self._get_next_cod(), store=True, )
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)
    campos_relacional = fields.Integer(string="Campo relacional")


    @api.model
    def _get_next_cod(self):
        sequence = self.env['ir.sequence'].search([('code', '=', 'lugares.lugares')])
        next = sequence.get_next_char(sequence.number_next_actual)
        return next

    @api.model
    def create(self, vals):
        vals['codigo'] = self.env['ir.sequence'].next_by_code('lugares.lugares') or _('New')
        obg = super(lugares, self).create(vals)
        return obg
