# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_port(models.Model):
    _name = 'kki_port.inventory'
    _description = 'kki_port.kki_port'

    partid = fields.Char("partid")
    partname = fields.Char("partname")
    image = fields.Binary("image")
    vendor = fields.Many2one("res.partner", string="vendor")
    price = fields.Integer("price")

    #value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
