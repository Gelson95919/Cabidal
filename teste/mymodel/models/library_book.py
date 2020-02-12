# -*- coding: utf-8 -*-

from odoo import models, fields, api


class libraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _order = 'date_release desc, name'
    name = fields.Char(string="Title", required=True)
    _rec_name = 'short_name'
    short_name = fields.Char('Título abreviado')
    date_release = fields.Date(string="Data")
    autor_ids = fields.Many2many('res.partner', string="Autor")
    notes = fields.Text('Internal Notes')
    state = fields.Selection(
        [('draft', 'Not Available'),
         ('available', 'Available'),
         ('lost', 'Lost')],
        'State')
    description = fields.Html('Description')
    cover = fields.Binary('Book Cover')
    date_updated = fields.Datetime('Last Updated')
    pages = fields.Integer('Number of Pages')
    reader_rating = fields.Float(
        'Reader Average Rating',
        (14, 4),  # Optional precision (total, decimals),
    )
    currency_id = fields.Many2one('res.currency', string='moeda')
    retail_price = fields.Monetary('Preço varejo', currency_field='currency_id', )  # optional:
    library_loan_wizard_id = fields.Many2many('library.loan.wizard')
    library_returns_wizard_id = fields.Many2many('library.returns.wizard')
    publisher_id = fields.Many2one(
        'res.partner', string='Publisher',
        # optional:

    )
    _sql_constraints = [
        ('name_uniq',
         'Nome único)',
         'O título do livro deve ser único.')
    ]

    # passar a data no topo
    def name_get(self):
        result = []
        for record in self:
            result.append(
                (record.id,
                 u"%s (%s)" % (record.name, record.date_release)
                 ))
        return result

    # validaçao
    @api.constrains('date_release')
    def _check_release_date(self):
        for r in self:
            if r.date_release > fields.Date.today():
                raise models.ValidationError(
                    'A data de lançamento deve estar no passado')




class LibraryLoanWizard(models.TransientModel):
    _name = 'library.loan.wizard'
    member_id = fields.Many2one('library.member', 'Member')
    book_ids = fields.Many2many('library.book', 'library_loan_wizard_id', string='Books')

    @api.multi
    def record_loans(self):
        for wizard in self:
            member = wizard.member_id
            books = wizard.book_ids
            loan = self.env['library.book.loan']
            for book in wizard.book_ids:
                loan.create({'member_id': member.id, 'book_id': book.id})




class LibraryReturnsWizard(models.TransientModel):
    _name = 'library.returns.wizard'
    member_id = fields.Many2one('library.member', 'Member')
    book_ids = fields.Many2many('library.book', 'library_returns_wizard_id')

    @api.multi
    def record_returns(self):
        loan = self.env['library.book.loan']
        for rec in self:
            loans = loan.search(
                [('state', '=', 'ongoing'), ('book_id', 'in', rec.book_ids.ids), ('member_id', '=', rec.member_id.id)])
            loans.write({'state': 'done'})

    @api.onchange('member_id')
    def onchange_member(self):
        loan = self.env['library.book.loan']
        loans = loan.search([('state', '=', 'ongoing'), ('member_id', '=', self.member_id.id)])
        self.book_ids = loans.mapped('book_id')

    #ou avisar o cliente
    @api.onchange('member_id')
    def onchange_member(self):
        loan = self.env['library.book.loan']
        loans = loan.search([('state', '=', 'ongoing'), ('member_id', '=', self.member_id.id)])
        self.book_ids = loans.mapped('book_id')
        result = {'domain': {'book_ids': [('id', 'in', self.book_ids.ids)]}}
        late_domain = [('id', 'in', loans.ids), ('expected_return_date', '<', fields.Date.today())]
        late_loans = loans.search(late_domain)
        if late_loans:
           message = ('Avise o membro que as seguintes ', 'livros estão atrasados:\n')
           titles = late_loans.mapped('book_id.name')
           result['warning'] = {'title': 'Livros atrasados', 'message': message}#+ '\n'.join('titles')

        return result




class LibraryBookLoan(models.Model):
    _name = 'library.book.loan'
    book_id = fields.Many2one('library.book', 'Book', required=True)
    expected_return_date = fields.Char(string='Data', default='03-04-2019')
    member_id = fields.Many2one('library.member', 'Borrower', required=True)
    state = fields.Selection([('ongoing', 'Ongoing'), ('done', 'Done')], 'State', default='ongoing', required=True)



class LibraryMember(models.Model):
    _name = 'library.member'
    #_inherits = {'res.partner': 'partner_id'}
    partner_id = fields.Many2one('res.partner', ondelete='cascade')
    date_start = fields.Date('Membro desde')
    date_end = fields.Date('Termination Date')
    member_number = fields.Char()
    membe = fields.Char()

    #@api.multi
    #def return_all_books(self):
    #    self.ensure_one
    #    wizard = self.env['library.returns.wizard']
    #    values = {'member_id': self.id, book_ids = False}
    #    specs = wizard._onchange_spec()
    #    updates = wizard.onchange(values, ['member_id'], specs)
    #    value = updates.get('value', {})
    #    for name, val in value.iteritems():
    #        if isinstance(val, tuple):
    #            value[name] = val[0]
    #    values.update(value)
    #    record = wizard.create(values)



class ResPartner(models.Model):
    _inherit = 'res.partner'
    book_ids = fields.One2many('library.book', 'publisher_id', string='Published Books')




