# -*- coding: utf-8 -*-
{
    'name': "Vendas",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Gestão de Vendas
    """,

    'author': "Cabosys",
    'website': "http://www.cabosys.cv",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Gestão vendas',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'parametros'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',

        'views/documento_factura.xml',
        'views/listagem_documento_vendas.xml',
        'views/confirencia_contabilidade.xml',
        # 'views/consulta_documento_pendentes.xml',
        'security/vendas_security.xml',
        'security/ir.model.access.csv',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
