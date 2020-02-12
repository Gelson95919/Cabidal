# -*- coding: utf-8 -*-
{
    'name': "Despachos",

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
    'category': 'despacho',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'parametros', 'gestao_compras'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/factura_previsorias.xml',
        'views/factura_definitiva.xml',
        'views/base_despachante_difinitiva.xml',
        'views/base_desopesa_definitiva.xml',
        'views/listagem_livros_deve_haber.xml',
        'views/livros_honorarios_iva_iur.xml',
        'views/listagem_honorarios.xml',
        'views/listagem_rubricas_alfandiga.xml',
        'views/rubricas.xml',
        'views/listagem_despachos.xml',
        'views/guia_deposito.xml',
        'views/declaracao_valor.xml',
        'views/autorizacao_saida.xml',
        'views/requerimento_de_saida.xml',
        'views/veiculos_requerimento.xml',
        'views/titulo_rectificativo.xml',
        'views/titulo_comercio_externo.xml',
        'views/selagem_mercadoria.xml',
        'security/despacho_security.xml',
        'security/ir.model.access.csv',

    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
