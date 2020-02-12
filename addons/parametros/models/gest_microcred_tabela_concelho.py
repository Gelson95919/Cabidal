# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions, _


class concelho(models.Model):
    _name = 'concelho.concelho'
    _rec_name = 'name'
    _description = 'Concelho'

    codigo = fields.Char(string="Código", copy=False, readonly=True, index=True,
                          store=True, )
    name = fields.Char(tring="Nome")
    #ilha = fields.Many2one('ilha', string="Ilha")
    ilha = fields.Selection([('1', 'Santo Antão'),
                             ('2', 'S.Vicente'),
                             ('3', 'S.Niculao'),
                             ('4', 'Sal'),
                             ('5', 'Boavista'),
                             ('6', 'Maio'),
                             ('7', 'Santiago'),
                             ('8', 'Fogo'),
                             ('9', 'Brava'),
                             ('10', 'Santa Luzia'),], tring="Ilha")
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)
    campos_relacional = fields.Integer(string="Campo relacional")

    """
    @api.model
    def _get_next_cod(self):
        sequence = self.env['ir.sequence'].search([('code', '=', 'concelho.concelho')])
        next = sequence.get_next_char(sequence.number_next_actual)
        return next

   @api.model
    def create(self, vals):
        vals['codigo'] = self.env['ir.sequence'].next_by_code('concelho.concelho') or _('New')
        obg = super(concelho, self).create(vals)
        return obg"""

