# -*- coding: utf-8 -*-


#from odoo import models, fields, api, tools



from datetime import timedelta
from odoo import models, fields, api, exceptions

class Course(models.Model):
    _name = 'openacademy.session'
    name = fields.Char(string='Descricao')
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    start_date = fields.Date(default=fields.Date.today)
    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')
    end_date = fields.Date(string="End Date", store=True, compute='_get_end_date', inverse='_set_end_date')
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    instructor_id = fields.Many2one('res.partner', string="Instructor",
                                    domain=['|', ('instructor', '=', True)])
    color = fields.Integer()
    seats = fields.Integer(string="Number of seats")
    active = fields.Boolean(default=True)

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue

            # Adicionar duração a start_date, mas: segunda + 5 dias = sábado, então
            # subtraia um segundo para chegar na sexta-feira
            start = fields.Datetime.from_string(r.start_date)
            duration = timedelta(days=r.duration, seconds=-1)
            r.end_date = start + duration

    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue

            # Calcule a diferença entre as datas, mas: sexta-feira - segunda-feira = 4 dias,
            # adicione um dia para obter 5 dias
            start_date = fields.Datetime.from_string(r.start_date)
            end_date = fields.Datetime.from_string(r.end_date)
            r.duration = (end_date - start_date).days + 1

    @api.depends('taken_seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            end_date = fields.Datetime.from_string(r.end_date)
            # r.duration = (end_date - self.start_date).days + 1

    @api.depends('duration')
    def _get_hours(self):
        for r in self:
            r.hours = r.duration * 24

    def _set_hours(self):
        for r in self:
            r.duration = r.hours / 24



