# -*- coding: utf-8 -*-

from odoo import api, models, fields
import sys

class _service(models.Model):
    _name = 'se.service'
    _description = "Se Servici"
    _rec_name = "service_name"

    name = fields.Char('Reference', copy=False, readonly=True)
    service_name = fields.Char("Service Name", required=True)
    service_description = fields.Text("Description", required=True)
    service_remarks = fields.Text("Remarks")
    service_methodology = fields.Html(string="Methodology")



    def create_apple(self):
        inv_obj = self.env['se.apple']
        #self.ensure_one()
        invoice = inv_obj.create({
            'apple_name': self.service_name,
            'apple_description': self.service_description,
            'apple_remarks': self.service_remarks
        })
        return invoice



class _apple(models.Model):
    _name = 'se.apple'

    _description = "Se apple"
    apple_name = fields.Char("Apple Name")
    apple_description = fields.Text("Remarks Apple")
    apple_remarks = fields.Text("Remarks Apple")
