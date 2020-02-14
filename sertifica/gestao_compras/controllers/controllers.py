# -*- coding: utf-8 -*-
from odoo import http

# class GestaoCompras(http.Controller):
#     @http.route('/gestao_compras/gestao_compras/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestao_compras/gestao_compras/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestao_compras.listing', {
#             'root': '/gestao_compras/gestao_compras',
#             'objects': http.request.env['gestao_compras.gestao_compras'].search([]),
#         })

#     @http.route('/gestao_compras/gestao_compras/objects/<model("gestao_compras.gestao_compras"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestao_compras.object', {
#             'object': obj
#         })