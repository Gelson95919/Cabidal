# -*- coding: utf-8 -*-
from odoo import http

# class AgenciaAerea(http.Controller):
#     @http.route('/agencia_aerea/agencia_aerea/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/agencia_aerea/agencia_aerea/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('agencia_aerea.listing', {
#             'root': '/agencia_aerea/agencia_aerea',
#             'objects': http.request.env['agencia_aerea.agencia_aerea'].search([]),
#         })

#     @http.route('/agencia_aerea/agencia_aerea/objects/<model("agencia_aerea.agencia_aerea"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('agencia_aerea.object', {
#             'object': obj
#         })