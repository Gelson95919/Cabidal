# -*- coding: utf-8 -*-
from odoo import http

# class GestaoSocios(http.Controller):
#     @http.route('/gestao_socios/gestao_socios/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestao_socios/gestao_socios/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestao_socios.listing', {
#             'root': '/gestao_socios/gestao_socios',
#             'objects': http.request.env['gestao_socios.gestao_socios'].search([]),
#         })

#     @http.route('/gestao_socios/gestao_socios/objects/<model("gestao_socios.gestao_socios"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestao_socios.object', {
#             'object': obj
#         })