# -*- coding: utf-8 -*-
{
    'name': "Sócios",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Cabosys",
    'website': "http://www.Cabosys.cv",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'socios',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'gestao_vendas', 'parametros'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/consulta_conta_corente.xml',
        'views/gerar_conta_corente.xml',
        'security/socios_security.xml',
        'security/ir.model.access.csv',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
