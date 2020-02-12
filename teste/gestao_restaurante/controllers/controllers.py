# -*- coding: utf-8 -*-
from odoo import http

# class GestaoRestaurante(http.Controller):
#     @http.route('/gestao_restaurante/gestao_restaurante/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestao_restaurante/gestao_restaurante/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestao_restaurante.listing', {
#             'root': '/gestao_restaurante/gestao_restaurante',
#             'objects': http.request.env['gestao_restaurante.gestao_restaurante'].search([]),
#         })

#     @http.route('/gestao_restaurante/gestao_restaurante/objects/<model("gestao_restaurante.gestao_restaurante"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestao_restaurante.object', {
#             'object': obj
#         })