# -*- coding: utf-8 -*-
from odoo import http

# class Contabilidade(http.Controller):
#     @http.route('/contabilidade/contabilidade/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contabilidade/contabilidade/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('contabilidade.listing', {
#             'root': '/contabilidade/contabilidade',
#             'objects': http.request.env['contabilidade.contabilidade'].search([]),
#         })

#     @http.route('/contabilidade/contabilidade/objects/<model("contabilidade.contabilidade"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contabilidade.object', {
#             'object': obj
#         })