# -*- coding: utf-8 -*-

from odoo import models, fields, api

""""""
class first_class(models.Model):
    _name = 'tbl1'
    #_name = 'transport.vehicle'
    code = fields.Char('Code', size=3, required=True)
    description = fields.Char('Description', size=40, required=True)

    """
    name = fields.Char(string="Name", required=True)
    description = fields.Text()
    reg_date = fields.Date()
    department = fields.Char()
    available = fields.Boolean()
    line_ids = fields.Many2one('tbl2', string="Vehicle ref")
    tbl2_ids = fields.Many2one('tbl2', string="Vehicle ref")"""
    """
    @api.multi
    def open_second_class(self):
        ac = self.env['ir.model.data'].xmlid_to_res_id('gestao_tesouraria.view_mymodule_tbl2_form',
                                                       raise_if_not_found=True)
        tbl1 = False
        for o in self:
            tbl1 = o.id
        result = {
            'name': 'second_class',
            'view_type': 'form',
            'res_model': 'tbl2',
            'view_id': ac,
            'context': {'default_id_tbl1': tbl1},
            'type': 'ir.actions.act_window',
            'view_mode': 'form'
        }
        return result"""

    @api.multi
    def open_second_class(self):
        ac = self.env['ir.model.data'].xmlid_to_res_id('gestao_tesouraria.view_mymodule_tbl2_form', raise_if_not_found=True)
        tbl1 = False
        tbl2 = False
        for o in self:
            tbl1 = o.code
            tbl2 = o.description
        result = {
            'name': '2nd class',
            'view_type': 'form',
            'res_model': 'tbl2',
            'view_id': ac,
            'context': {'default_id_tbl1': tbl1, 'default_employee': tbl2},
            'type': 'ir.actions.act_window',
            'view_mode': 'form'
        }
        return result

    def po_generator(self):
        res = {}
        purchase_orders = self.pool.get('tbl2')
        for expense in self.browse(self):
            expense_line = self.pool.get('tbl1.line')
            purchase_orders = self.pool.get('tbl2')
            for line in expense.line_ids:
                purchase_orders.create(self,
                                       {
                                           'name': line.name.id,
                                           'description': line.description,
                                           'reg_date': line.reg_date,
                                           'department': line.department,
                                           'available': line.available,

                                       },

                                       )
        return res

    @api.multi
    def insert_data(self):
        for record in self.env['tbl1'].browse(self._context.get('active_ids', [])):
            # você pode acessar os campos da tabela de destino usando a variável * record *

            #record.field_name = wizard.field_name

            record.tbl2_ids.name = 'name'
            record.tbl2_ids.description = 'description'
            record.tbl2_ids.reg_date = 'reg_date'
            record.tbl2_ids.department = 'department'
            record.tbl2_ids.available = 'available'
            #record.active_ids.member_id = self.member_id


        return True


class second_class(models.Model):
    _name = 'tbl2'
    #_inherits = {'tbl1': 'id_tbl1'}

    id_tbl1 = fields.Many2one('tbl1')
    employee = fields.Char('Name', size=40, required=True)
    """
    #_name = 'od.add.new.vehicle'
    _description = 'Add new vehicle'
    name = fields.Char('vehicle name')
    description = fields.Text('Description')
    reg_date = fields.Date('Reg date')
    department = fields.Char('Department')
    available = fields.Boolean('Available')"""
