# -*- coding: utf-8 -*-
# from odoo import http


# class KkiLiftExp(http.Controller):
#     @http.route('/kki_lift_exp/kki_lift_exp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kki_lift_exp/kki_lift_exp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kki_lift_exp.listing', {
#             'root': '/kki_lift_exp/kki_lift_exp',
#             'objects': http.request.env['kki_lift_exp.kki_lift_exp'].search([]),
#         })

#     @http.route('/kki_lift_exp/kki_lift_exp/objects/<model("kki_lift_exp.kki_lift_exp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kki_lift_exp.object', {
#             'object': obj
#         })
