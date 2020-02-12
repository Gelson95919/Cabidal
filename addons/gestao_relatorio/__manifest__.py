# -*- coding: utf-8 -*-
{
    'name': "gestao_relatorio",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Gestão Relatório",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['parametros', 'base'],

    # always loaded
    'data': [

        'views/views.xml',
        'views/templates.xml',
        'views/previsao_reembolso.xml',
        'views/reports_listagem_previsao.xml',
        'views/carteira_em_risco.xml',
        'views/reports_carteira_em_risco.xml',
        'views/historico_reembolso.xml',
        'views/reports_historico_reembolso.xml',
        'views/reembolso_recebido.xml',
        'views/reports_reembolso_recebido.xml',
        'views/relatorio_desembolso.xml',
        'views/reports_relatorio_desembolso.xml',
        'views/report_ficha_cadastral_solicita_credito.xml',
        'views/ficha_credito.xml',
        'views/posicao_tesouraria.xml',
        'views/reports_listagem_folha_tesouira.xml',
        'views/indicadores.xml',
        'views/reports_indicadores_financeiros.xml',
        'views/emprestimo_por_antiguidade.xml',
        'views/reports_emprestimo_por_antiguidade.xml',

        'security/grupo_relatorio_security.xml',
        'security/ir.model.access.csv',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
