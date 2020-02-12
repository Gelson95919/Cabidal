# -*- coding: utf-8 -*-
from odoo import http

# class AgenciaMaritima(http.Controller):
#     @http.route('/agencia_maritima/agencia_maritima/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/agencia_maritima/agencia_maritima/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('agencia_maritima.listing', {
#             'root': '/agencia_maritima/agencia_maritima',
#             'objects': http.request.env['agencia_maritima.agencia_maritima'].search([]),
#         })

#     @http.route('/agencia_maritima/agencia_maritima/objects/<model("agencia_maritima.agencia_maritima"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('agencia_maritima.object', {
#             'object': obj
#         })