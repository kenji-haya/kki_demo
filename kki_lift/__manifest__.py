# -*- coding: utf-8 -*-
{
    'name': "kki_lift",

    'summary': """
        forklift management""",

    'description': """
        Long description of module's purpose
    """,

    'author': "KKI",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/forklift.xml',
        'views/templates.xml',
        'views/size.xml',
        'views/check_history.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
