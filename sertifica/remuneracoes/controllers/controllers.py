# -*- coding: utf-8 -*-
from odoo import http

# class Remuneracoes(http.Controller):
#     @http.route('/remuneracoes/remuneracoes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/remuneracoes/remuneracoes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('remuneracoes.listing', {
#             'root': '/remuneracoes/remuneracoes',
#             'objects': http.request.env['remuneracoes.remuneracoes'].search([]),
#         })

#     @http.route('/remuneracoes/remuneracoes/objects/<model("remuneracoes.remuneracoes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('remuneracoes.object', {
#             'object': obj
#         })