# -*- coding: utf-8 -*-
from odoo import http

# class StaticResourcesDemo(http.Controller):
#     @http.route('/static_resources_demo/static_resources_demo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/static_resources_demo/static_resources_demo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('static_resources_demo.listing', {
#             'root': '/static_resources_demo/static_resources_demo',
#             'objects': http.request.env['static_resources_demo.static_resources_demo'].search([]),
#         })

#     @http.route('/static_resources_demo/static_resources_demo/objects/<model("static_resources_demo.static_resources_demo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('static_resources_demo.object', {
#             'object': obj
#         })