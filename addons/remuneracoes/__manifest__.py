# -*- coding: utf-8 -*-
{
    'name': "Remunerações",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Processamento de remunerações, faltas, horas extras, descontos, obrigações fiscais incluindo os modelos oficiais 111, 112 e 113
    """,

    'author': "Cabosys",
    'website': "http://www.cabosys.cv",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'parametros'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',

        'views/funcionario_remuneracoe.xml',
        'views/alterar_mensal.xml',
        'views/processamento_automatico_remuneracoes.xml',
        'views/processamento_manual_remuneracoes.xml',
        'views/pagamentos.xml',
        'views/remuner_ferias.xml',
        'views/mapa_oficiais_seguros.xml',
        'views/mapa_oficiais_sindicato.xml',
        'views/mapa_oficiais_reparticao.xml',
        'views/mapa_oficiais_seguranca_social.xml',
        'views/mapas_internos_emicao_recibo.xml',
        'views/mapas_internos_mapa_vencimento.xml',
        'views/mapa_interno_dados_processamento.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}