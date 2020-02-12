# -*- coding: utf-8 -*-
from odoo import http

# class GestaoVendas(http.Controller):
#     @http.route('/gestao_vendas/gestao_vendas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestao_vendas/gestao_vendas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestao_vendas.listing', {
#             'root': '/gestao_vendas/gestao_vendas',
#             'objects': http.request.env['gestao_vendas.gestao_vendas'].search([]),
#         })

#     @http.route('/gestao_vendas/gestao_vendas/objects/<model("gestao_vendas.gestao_vendas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestao_vendas.object', {
#             'object': obj
#         })