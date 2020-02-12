# -*- coding: utf-8 -*-
from odoo import http

# class GestaoAcademica(http.Controller):
#     @http.route('/gestao_academica/gestao_academica/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestao_academica/gestao_academica/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestao_academica.listing', {
#             'root': '/gestao_academica/gestao_academica',
#             'objects': http.request.env['gestao_academica.gestao_academica'].search([]),
#         })

#     @http.route('/gestao_academica/gestao_academica/objects/<model("gestao_academica.gestao_academica"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestao_academica.object', {
#             'object': obj
#         })