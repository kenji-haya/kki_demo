# -*- coding: utf-8 -*-
# from odoo import http


# class KkiLift2(http.Controller):
#     @http.route('/kki_demo/kki_demo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kki_demo/kki_demo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kki_demo.listing', {
#             'root': '/kki_demo/kki_demo',
#             'objects': http.request.env['kki_demo.kki_demo'].search([]),
#         })

#     @http.route('/kki_demo/kki_demo/objects/<model("kki_demo.kki_demo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kki_demo.object', {
#             'object': obj
#         })
