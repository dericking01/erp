# -*- coding: utf-8 -*-
# from odoo import http


# class Azampay(http.Controller):
#     @http.route('/azampay/azampay', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/azampay/azampay/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('azampay.listing', {
#             'root': '/azampay/azampay',
#             'objects': http.request.env['azampay.azampay'].search([]),
#         })

#     @http.route('/azampay/azampay/objects/<model("azampay.azampay"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('azampay.object', {
#             'object': obj
#         })

