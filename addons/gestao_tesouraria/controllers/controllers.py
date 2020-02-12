# -*- coding: utf-8 -*-
from odoo import http

# class GestaoTesouraria(http.Controller):
#     @http.route('/gestao_tesouraria/gestao_tesouraria/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestao_tesouraria/gestao_tesouraria/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestao_tesouraria.listing', {
#             'root': '/gestao_tesouraria/gestao_tesouraria',
#             'objects': http.request.env['gestao_tesouraria.gestao_tesouraria'].search([]),
#         })

#     @http.route('/gestao_tesouraria/gestao_tesouraria/objects/<model("gestao_tesouraria.gestao_tesouraria"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestao_tesouraria.object', {
#             'object': obj
#         })