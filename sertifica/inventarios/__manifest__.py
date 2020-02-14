# -*- coding: utf-8 -*-
{
    'name': "inventarios",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Cabosys",
    'website': "http://www.Cabosys.cv",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'inventario',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['gestao_compras', 'gestao_vendas', 'parametros', 'base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/acres_doc_armanzen_guia_entrada.xml',
        'views/acres_doc_armanzen_guia_saida.xml',
        'views/guia_trasnferencia.xml',
        'views/tabela_preco.xml',
        'views/posicao_stok.xml',
        'views/movimento_armazem.xml',
        'views/relatorio_motivo_saida_entrada_stock.xml',
        'security/inventario_security.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}