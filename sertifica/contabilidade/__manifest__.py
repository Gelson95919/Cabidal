# -*- coding: utf-8 -*-
{
    'name': "Contabilidade",

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
    'category': 'contabilidade',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'parametros', 'gestao_vendas', 'gestao_compras', 'gestao_tesouraria'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/lancamento.xml',
        'views/actualizar_razao.xml',
        'views/extractos_conta.xml',
        'views/balancete.xml',
        'views/diario_auxiliar.xml',
        'views/relatorio_fluxo_caixa.xml',
        'views/consulta_extracto.xml',
        'views/configurar_processo.xml',
        'views/gerar_contabilidade.xml',
        'views/declarcao_period_rendimento.xml',
        'views/declarar_iva_mensal.xml',
        'views/calindar.xml',
        'views/report_balancete.xml',

        'security/contabilidae_security.xml',
        'security/ir.model.access.csv',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
