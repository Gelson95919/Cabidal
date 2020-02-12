# -*- coding: utf-8 -*-
{
    'name': "Compras",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Gestão de Compras
    """,

    'author': "Cabosys",
    'website': "http://www.cabosys.cv",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Gestão de Compras',
    'version': '1.3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'parametros'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',

        'views/acrescentar_docum.xml',
        'views/confirencia_contabilidade.xml',
        'views/consulta_documento_pendentes.xml',
        'views/listagem_documento_compra.xml',
        'security/compras_security.xml',
        'security/ir.model.access.csv',

        'views/qweb_reports.xml',  # para testar o relatorios inda nao funciona
        #'views/project.xml',
        'views/selecaoPai.xml',
        'views/selecaoPFil.xml',

    ],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    # 'post_init_hook': '_auto_install_l10n',
    #'qweb': ['static/src/xml/project_button.xml', ],

   # 'js': 'static/src/js/task_list.js',

}
