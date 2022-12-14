# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_product(models.Model):
    _inherit = 'product.template'

    name2 = fields.Char()
    marge_name = fields.Char(compute='_get_marge_name', store=True)
    unified_id = fields.Char('unified_id')
    product_category = fields.Many2one('kki_product.categoryid', string='product_category')

    @api.depends('name', 'name2')
    def _get_marge_name(self):
        for record in self:
            if record.name2:
                record.marge_name = record.name + record.name2
            else:
                record.marge_name = record.name
