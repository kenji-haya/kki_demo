# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_lift_size(models.Model):
    _name = 'kki_lift.size'
    _description = 'kki_lift.size'

    name = fields.Char("name")
