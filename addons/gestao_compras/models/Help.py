# -*- coding: utf-8 -*-


from odoo import models, fields, api, tools



class ParentModel(models.Model):
    _name = 'parent.model'
    name = fields.Char(string='Parent Field 1')

    #parent_field_1 = fields.Char(string="Parent Field 1")
    parent_field_2 = fields.Integer(string="Parent Field 2")

    # If you want to display child data, you must create One2many field.
    # The One2many field used for inverse field from Many2one field
    child_field_ids = fields.One2many('child.model', 'parent_field_id', string="Child IDS")


    state =fields.Char(string='Estado')
    namei = fields.Char(string='Nome')
    descriptioni = fields.Text(string='Descricao')


class ChildModel(models.Model):
    _name = 'child.model'
    #child_field_1 = fields.Char(string='Child Field 1', related="id_child.child_field_1", store=True)
    child_field_1 = fields.Char(string="Child Field 1")
    child_field_2 = fields.Integer(string="Child Field 2")
    child_field_3 = fields.Boolean(string="Child Field 3")
    parent_field_id = fields.Many2one('res.users', string="Parent ID", default=lambda self: self.env.user)
