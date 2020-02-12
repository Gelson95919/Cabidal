# -*- coding: utf-8 -*-
{
    'name': "Parâmetros",

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
    'category': 'parametros',
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',

        # 'security/user_groups.xml',
        # 'security/ir.model.access.csv',

        'views/uso_geral_terceiro.xml',
        'views/uso_geral_tipoDocum.xml',
        'views/uso_geral_produto_servico.xml',
        'views/uso_geral_iva.xml',
        'views/uso_geral_condicao_pagamento.xml',
        'views/uso_geral_meio_monetario.xml',
        'views/inventa_filiais.xml',
        # 'views/uso_geral_tipo_entidade.xml',
        'views/uso_geral_responsaves.xml',
        'views/uso_geral_Profissoes.xml',
        'views/uso_geral_nacionalidade.xml',
        'views/uso_geral_organizacao.xml',

        'views/comp_codigo_compra.xml',
        'views/comp_processo_compra.xml',

        'views/vend_artigos.xml',
        'views/vend_preco.xml',

        'views/inventa_uni_medida.xml',
        'views/inventa_tipo_propiedade.xml',
        'views/inventa_motivo_movimento_stock.xml',
        'views/inventa_familia.xml',
        'views/inventa_sub_familia.xml',
        'views/inventa_armanzem.xml',

        'views/inventa_detalhes_doc_armazem.xml',

        'views/teso_conceito_movim.xml',
        'views/teso_entidade_bancaria.xml',
        'views/teso_plan_tesoraria.xml',
        'views/teso_moeda.xml',
        'views/teso_moeda.xml',

        'views/contabil_periodo.xml',
        'views/contabil_diario.xml',
        'views/contabil_plano_iva.xml',
        'views/contabil_plano_conta.xml',
        'views/contabil_analitica_plano_conta.xml',
        'views/tesora_orcame_teso.xml',
        'views/teso_conceito_recebimento.xml',
        'views/teso_conceito_pagamento.xml',

        'views/remune_instituicoes.xml',
        'views/remune_dados_processamento.xml',
        'views/remune_dados_funcionarios.xml',
        'views/remune_outras_tabelas.xml',

        'views/investiment_tipo_imobilizado.xml',
        'views/investiment_motivo_abate.xml',
        'views/investiment_departamento_area.xml',
        'views/investiment_amortizacao_portuaria.xml',
        'views/investiment_amortizacao_gestao.xml',

        'views/age_maritima_portos.xml',
        'views/age_maritima_classe_navio.xml',
        'views/age_maritima_tipo_carga.xml',
        'views/age_maritima_combustivel.xml',
        'views/age_maritima_navios.xml',
        'views/age_maritima_motivo_escala.xml',
        'views/age_maritima_passagem_maritima.xml',
        'views/age_maritima_tipo_agenciamento.xml',
        'views/age_maritima_qualidade_carga.xml',
        'views/age_maritima_taxa_descarga.xml',
        'views/age_maritima_frete_cabotagem.xml',
        'views/age_maritima_rubrica_conta_escala.xml',
        'views/age_maritima_tabela_tarifa_enapor.xml',
        'views/age_maritima_mercadoria.xml',
        'views/age_maritima_mercadoria.xml',
        'views/gest_socio_socio.xml',
        # 'views/age_maritima_faturacao.xml',

        'views/gest_academ_alunos.xml',
        'views/gest_academ_matricula.xml',
        'views/gest_academ_ano_lectivo.xml',
        'views/gest_academ_curso.xml',

        'views/gest_microcred_tabela_agentes.xml',
        'views/gest_microcred_tabela_ilha.xml',
        'views/gest_microcred_tabela_concelho.xml',
        'views/gest_microcred_tabela_freguesia.xml',
        'views/gest_microcred_tabela_zonas.xml',
        'views/gest_microcred_tabela_lugares.xml',
        'views/gest_microcred_gestao_comite_credito.xml',
        'views/gest_microcred_gestao_fundos.xml',
        'views/gest_microcred_servico.xml',
        'views/gest_microcred_uni_medida.xml',
        'views/gest_microf_proficoes.xml',

        'views/despachant_sedonia_tarifa_alfandiga.xml',
        'views/despachant_sedonia_hora_remuneracoes.xml',
        'views/despachant_sedonia_ajuda_custo.xml',
        'views/despachant_sedonia_rigime_alfandega.xml',
        'views/rubrica_despachante.xml',

        'views/gestao_hotel_tipo_movimento.xml',
        'views/gestao_hotel_tipo_consumo.xml',
        'views/gestao_hotel_tipo_pagamento.xml',
        'views/gestao_hotel_utilizadores.xml',
        'views/gestao_hotel_tarifario.xml',
        'views/gestao_hotel_habitacoes.xml',
        'views/gestao_hotel_clientes.xml',

        'views/gestao_restaurante_grupos_artigos.xml',
        'views/gestao_restaurante_impressora.xml',
        'views/gestao_restaurante_garconete.xml',
        'views/remuner_descont_por_prestacao.xml',
        'views/gestao_pais.xml',
        'views/gestao_reparticao_financas.xml',
        'views/reg_docum.xml',
        'views/cta_cte.xml',
        'security/parametros_security.xml',

        'security/ir.model.access.csv',

        'views/Tratamento_dado_OP.xml',
        'views/configuracao.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    # 'post_init_hook': '_auto_install_l10n',
}
