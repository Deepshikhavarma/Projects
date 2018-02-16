# -*- coding: utf-8 -*-
from odoo import http

# class EqualCheck(http.Controller):
#     @http.route('/equal_check/equal_check/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/equal_check/equal_check/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('equal_check.listing', {
#             'root': '/equal_check/equal_check',
#             'objects': http.request.env['equal_check.equal_check'].search([]),
#         })

#     @http.route('/equal_check/equal_check/objects/<model("equal_check.equal_check"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('equal_check.object', {
#             'object': obj
#         })