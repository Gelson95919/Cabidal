# -*- coding: utf-8 -*-
{
    'name': "Estudo Odoo",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/library_book.xml',
        'views/library_loan_wizard_form.xml',
        'views/listview_templates.xml',


    ],
    # only loaded in demonstration moderesourse
    'demo': [
        'demo/demo.xml',
    ],
    "images": ["static/description/screen1.png"],
    'license': 'LGPL-3',
    'qweb': [
        'static/src/xml/base.xml',
    ],
}
