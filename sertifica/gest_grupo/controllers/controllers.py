# -*- coding: utf-8 -*-
from odoo import http

# class GestGrupo(http.Controller):
#     @http.route('/gest_grupo/gest_grupo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gest_grupo/gest_grupo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gest_grupo.listing', {
#             'root': '/gest_grupo/gest_grupo',
#             'objects': http.request.env['gest_grupo.gest_grupo'].search([]),
#         })

#     @http.route('/gest_grupo/gest_grupo/objects/<model("gest_grupo.gest_grupo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gest_grupo.object', {
#             'object': obj
#         })