# -*- coding: utf-8 -*-
from odoo import http

# class GestaoRelatorio(http.Controller):
#     @http.route('/gestao_relatorio/gestao_relatorio/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestao_relatorio/gestao_relatorio/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestao_relatorio.listing', {
#             'root': '/gestao_relatorio/gestao_relatorio',
#             'objects': http.request.env['gestao_relatorio.gestao_relatorio'].search([]),
#         })

#     @http.route('/gestao_relatorio/gestao_relatorio/objects/<model("gestao_relatorio.gestao_relatorio"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestao_relatorio.object', {
#             'object': obj
#         })