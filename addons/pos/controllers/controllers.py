# -*- coding: utf-8 -*-
from odoo import http

# class Pos(http.Controller):
#     @http.route('/pos/pos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos/pos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos.listing', {
#             'root': '/pos/pos',
#             'objects': http.request.env['pos.pos'].search([]),
#         })

#     @http.route('/pos/pos/objects/<model("pos.pos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos.object', {
#             'object': obj
#         })