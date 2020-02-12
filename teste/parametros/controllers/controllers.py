# -*- coding: utf-8 -*-
from odoo import http

# class Parametros(http.Controller):
#     @http.route('/parametros/parametros/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/parametros/parametros/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('parametros.listing', {
#             'root': '/parametros/parametros',
#             'objects': http.request.env['parametros.parametros'].search([]),
#         })

#     @http.route('/parametros/parametros/objects/<model("parametros.parametros"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('parametros.object', {
#             'object': obj
#         })