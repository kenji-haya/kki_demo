# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_product_category(models.Model):
    _name = 'kki_product.categoryid'
    _description = 'kki_product.category'

    category = fields.Char('category')