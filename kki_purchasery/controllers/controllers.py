# -*- coding: utf-8 -*-
# from odoo import http


# class KkiPurchasery(http.Controller):
#     @http.route('/kki_purchasery/kki_purchasery/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kki_purchasery/kki_purchasery/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kki_purchasery.listing', {
#             'root': '/kki_purchasery/kki_purchasery',
#             'objects': http.request.env['kki_purchasery.kki_purchasery'].search([]),
#         })

#     @http.route('/kki_purchasery/kki_purchasery/objects/<model("kki_purchasery.kki_purchasery"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kki_purchasery.object', {
#             'object': obj
#         })
