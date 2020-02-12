# -*- coding: utf-8 -*-
from odoo import http

# class Economato(http.Controller):
#     @http.route('/economato/economato/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/economato/economato/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('economato.listing', {
#             'root': '/economato/economato',
#             'objects': http.request.env['economato.economato'].search([]),
#         })

#     @http.route('/economato/economato/objects/<model("economato.economato"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('economato.object', {
#             'object': obj
#         })