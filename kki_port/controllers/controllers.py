# -*- coding: utf-8 -*-
# from odoo import http


# class KkiPort(http.Controller):
#     @http.route('/kki_port/kki_port/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kki_port/kki_port/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kki_port.listing', {
#             'root': '/kki_port/kki_port',
#             'objects': http.request.env['kki_port.kki_port'].search([]),
#         })

#     @http.route('/kki_port/kki_port/objects/<model("kki_port.kki_port"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kki_port.object', {
#             'object': obj
#         })
