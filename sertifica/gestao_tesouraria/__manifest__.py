# -*- coding: utf-8 -*-
{
    'name': "Tesouraria",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
         Gestão a tesouraria
    """,

    'author': "Cabosys",
    'website': "http://www.cabosys.cv",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Gestão tesouraria',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['parametros', 'gestao_vendas', 'gestao_compras', 'base', 'web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',

        'views/pagamento_recebimento.xml',
        'views/pagamento.xml',
        'views/recebimento.xml',
        'views/movimento_interno.xml',
        'views/movimento_fundo_maneio.xml',
        'views/listagem_registro_pagamento.xml',
        'views/listagem_registro_recibimento.xml',
        'views/listagem_ordem_pagamento.xml',
        'views/listagem_movimento_interno.xml',
        'views/listagem_encontro_conta.xml',
        'views/listagem_folha_tesoura.xml',
        'views/ordem_pagamento.xml',
        'views/tesouraria_conta_corente.xml',
        'views/encontr_conta.xml',
        'views/diario_tesouraria.xml',
        # 'views/orcamento_tesouraria.xml',
        'views/tree_view_asset.xml',
        'views/folha_tesouraria.xml',
        'security/tesouraria_security.xml',
        'views/increment_receb_pag.xml',
        'views/reports_recibo.xml',
        'views/reports_encontro_conta.xml',
        'views/reports_ordem_pagamento.xml',
        'views/reports_conta_corente.xml',
        'views/reports_fundo_maneio.xml',
        'views/reports_diarios.xml',
        'views/reports_listagem_pagamento.xml',
        'views/reports_listagem_recebimento.xml',
        'views/reports_listagem_ordem_pagamento.xml',
        # 'views/reports_listagem_previsao.xml',
        'views/reports_listagem_encontro_conta.xml',
        'views/reports_listagem_folha_tesouira.xml',
        'views/listagem_folha_tesoura.xml',

        'security/ir.model.access.csv',

        # 'views/teste.xml',
        # 'views/modulo_teste.xml',
        # 'views/product_sub_category.xml',

    ],
    'qweb': ['static/src/xml/tree_view_button.xml'],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
