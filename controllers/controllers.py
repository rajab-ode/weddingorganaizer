# -*- coding: utf-8 -*-
# from odoo import http


# class Weddingorganaizer2(http.Controller):
#     @http.route('/weddingorganaizer2/weddingorganaizer2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/weddingorganaizer2/weddingorganaizer2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('weddingorganaizer2.listing', {
#             'root': '/weddingorganaizer2/weddingorganaizer2',
#             'objects': http.request.env['weddingorganaizer2.weddingorganaizer2'].search([]),
#         })

#     @http.route('/weddingorganaizer2/weddingorganaizer2/objects/<model("weddingorganaizer2.weddingorganaizer2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('weddingorganaizer2.object', {
#             'object': obj
#         })
