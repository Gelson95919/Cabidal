# -*- coding: utf-8 -*-
{
    'name': "Gestão Investimento",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Cabosys",
    'website': "http://www.cabosys.cv",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'investimento',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/adquisicoes.xml',
        'views/processo_amortizacao.xml',
        'views/abate.xml',
        'security/investimento_security.xml',
        'security/ir.model.access.csv',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}