# -*- coding: utf-8 -*-
from odoo import http

# class Mymodel(http.Controller):
#     @http.route('/mymodel/mymodel/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mymodel/mymodel/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mymodel.listing', {
#             'root': '/mymodel/mymodel',
#             'objects': http.request.env['mymodel.mymodel'].search([]),
#         })

#     @http.route('/mymodel/mymodel/objects/<model("mymodel.mymodel"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mymodel.object', {
#             'object': obj
#         })