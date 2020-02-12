# -*- coding: utf-8 -*-
{
    'name': "Agência Marítima",

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
    'category': 'maritima',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'parametros'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/maritima_engresso_bl.xml',
        'views/listagem_pertences.xml',
        'views/registro.xml',
        'views/proforma_plano_carga.xml',
        'views/manifesto.xml',
        'views/titulo_transporte.xml',
        'views/ordem_embarque.xml',
        'views/manifesto_carga_contabilizado.xml',
        'views/manifesto_carga_descritivo.xml',
        'views/passageiro.xml',
        'views/manifesto_passageiros_contabilizado.xml',
        'security/maritima_security.xml',
        'security/ir.model.access.csv',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
