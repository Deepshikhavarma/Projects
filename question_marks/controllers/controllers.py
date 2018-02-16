# -*- coding: utf-8 -*-
from odoo import http

# class QuestionMarks(http.Controller):
#     @http.route('/question_marks/question_marks/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/question_marks/question_marks/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('question_marks.listing', {
#             'root': '/question_marks/question_marks',
#             'objects': http.request.env['question_marks.question_marks'].search([]),
#         })

#     @http.route('/question_marks/question_marks/objects/<model("question_marks.question_marks"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('question_marks.object', {
#             'object': obj
#         })