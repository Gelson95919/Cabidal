# -*- coding: utf-8 -*-
from odoo import http

# class GestaoDespacho(http.Controller):
#     @http.route('/gestao_despacho/gestao_despacho/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestao_despacho/gestao_despacho/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestao_despacho.listing', {
#             'root': '/gestao_despacho/gestao_despacho',
#             'objects': http.request.env['gestao_despacho.gestao_despacho'].search([]),
#         })

#     @http.route('/gestao_despacho/gestao_despacho/objects/<model("gestao_despacho.gestao_despacho"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestao_despacho.object', {
#             'object': obj
#         })