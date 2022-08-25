#-*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_demo_master(models.Model):
    _name = 'kki_demo.master'
    _description = 'kki_demo.kki_demo'

    name = fields.Char('name')
    product = fields.Char('product')
    factory = fields.Char('factory')
    responsible = fields.Char('responsible')
    image = fields.Binary('image')
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
