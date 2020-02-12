# -*- coding: utf-8 -*-

from odoo import models, fields, api

class encrCodPagame(models.Model):
    _name = 'incr.num.pag'
    _rec_name = 'codigo'
    _description = 'Encriment Num Pagamento'

    codigo = fields.Char(string="Codigo", copy=False, readonly=True,
                         index=True,)
    name = fields.Char(string="Pagamento")

    """@api.model
    def _get_next_cod(self):
        sequence = self.env['ir.sequence'].search([('code', '=', 'incr.num.pag')])
        next = sequence.get_next_char(sequence.number_next_actual)
        return next

    @api.model
    def create(self, vals):
        vals['codigo'] = self.env['ir.sequence'].next_by_code('incr.num.pag')"""


class encrnumreceb(models.Model):
    _name = 'incr.num.receb'
    _rec_name = 'codigo'
    _description = 'Encriment Num Rec'

    codigo = fields.Char(string="Codigo",  copy=False, readonly=True, index=True)
    name = fields.Char(string="Pagamento")

    #@api.model
    #def _get_next_cod(self):
        #sequence = self.env['ir.sequence'].search([('code', '=', 'incr.num.receb')])
        #next = sequence.get_next_char(sequence.number_next_actual)
        #return next

    #@api.model
    #def create(self, vals):
        #vals['codigo'] = self.env['ir.sequence'].next_by_code('incr.num.receb')