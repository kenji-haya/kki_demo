# -*- coding: utf-8 -*-
# from odoo import http


# class KkiLift(http.Controller):
#     @http.route('/kki_lift/kki_lift/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kki_lift/kki_lift/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kki_lift.listing', {
#             'root': '/kki_lift/kki_lift',
#             'objects': http.request.env['kki_lift.kki_lift'].search([]),
#         })

#     @http.route('/kki_lift/kki_lift/objects/<model("kki_lift.kki_lift"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kki_lift.object', {
#             'object': obj
#         })
