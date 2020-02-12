# -*- coding: utf-8 -*-
from odoo import http

# class Investimento(http.Controller):
#     @http.route('/investimento/investimento/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/investimento/investimento/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('investimento.listing', {
#             'root': '/investimento/investimento',
#             'objects': http.request.env['investimento.investimento'].search([]),
#         })

#     @http.route('/investimento/investimento/objects/<model("investimento.investimento"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('investimento.object', {
#             'object': obj
#         })