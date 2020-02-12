# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _

class documento(models.Model):
     _name = 'documento.documento'
     #_inherit = "ir.sequence"
     _description = 'Tipo Documento'
     abrevia = fields.Char('Abreviatura')
     date_release = fields.Date('Data de lançamento')
     _rec_name = 'name'
     name = fields.Char('Descrição')
     codigo = fields.Char(string="Código", copy=False, readonly=True, index=True, default=lambda self: _('New'))
     num_acao = fields.Char(string="Num Act", copy=False, readonly=True, index=True, default=lambda self: _('New'))
     visualizar_no_menu = fields.Boolean('Visualizar no Menu')
     mudar_numeracao_anual = fields.Boolean('Mudar numeração ')
     #pago =fields.Boolean(string='Pago')
     tipo_movimento = fields.Selection(
          [('entrada', 'Entrada'),
           ('saida', 'Saida'),
           ('neutro', 'Neutro')],
          'Tipo Movimento', Widget="radio")
     imagem = fields.Binary('Imagem')
     permite_desconto = fields.Boolean('Permite Desconto')
     nao_aredondar = fields.Boolean('Não Aredondar')
     fat_para= fields.Selection(
          [('armazemStock', 'Armazém / Stock'),
           ('comprasDespesas', 'Compras / Despesas'),
           ('vendasFaturacao', 'Vendas / Faturação'),
           ('tesouraria', 'Tesouraria')],
          'Utilizar em:', Widget="radio")
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

     visualizar_no_tesorer = fields.Boolean('Visualizar no Tesorer')
     liq_cta_cte = fields.Boolean('Liq.Cta.Cte')
     permitir_um_unico_recebimento = fields.Boolean('Permitir um Único Recebimento/Pagam')
     considera_na_cta_cte = fields.Boolean(string='Considera na Cta.Cte')
     fluxo_caixa = fields.Many2one('planteso.planteso', string='Fluxo Caixa')

     criar_registro_para_contabilidade = fields.Boolean('Criar Registro para Contabilidade')
     contabilizar_Pelo_detalhe_do_documento = fields.Boolean('Contabilizar Pelo Detalhe Documento')
     diario = fields.Many2one('diario.diario', string='Diario')
     conta = fields.Many2one('planconta.planconta', string='Conta')
     centro = fields.Many2one('planconta.planconta', string='Centro Custo')
     _sql_constraints = [('name_unique', 'unique(name)', 'Documento ja existe!')]

     descricao = fields.Html('Descrição', sanitize=True, strip_style=False, )

     outros = fields.One2many('documento.documento', 'id', string='Outros', oldname='outros_line')

     artigo = fields.Many2one('artigo.artigo', string='Artigo/Serviço')

     descrica = fields.Text(string='Descrição')

     valor = fields.Integer(string='Valor')
     # Cazo Ver no menu é Tru

     modelo = fields.Char(string='Modelo', default='fatuclient.fatuclient', store=True)
     typeform = fields.Selection([('tree', 'Tree'),
                                  ('form', 'Form'),
                                  ('graph', 'Graph'),
                                  ('pivot', 'Pivot'),
                                  ('calendar', 'Calendar'),
                                  ('diagram', 'Diagram'),
                                  ('gantt', 'Gantt'),
                                  ('kanban', 'Kanban'),
                                  ('search', 'Search'),
                                  ('qweb', 'QWeb')], string='View Type')
     typetree = fields.Selection([('tree', 'Tree'),
                                  ('form', 'Form'),
                                  ('graph', 'Graph'),
                                  ('pivot', 'Pivot'),
                                  ('calendar', 'Calendar'),
                                  ('diagram', 'Diagram'),
                                  ('gantt', 'Gantt'),
                                  ('kanban', 'Kanban'),
                                  ('search', 'Search'),
                                  ('qweb', 'QWeb')], string='View Type')
     arch_fs = fields.Char(string='Arch Filename', default='gestao_vendas/views/documento_factura.xml', store=True)
     #arch_db = fields.Text(string='Arch Blob', default='<?xml version="1.0"?><t t-name="gestao_vendas.listing"><ul> <li t-foreach="objects" t-as="object"><a t-attf-href="#{ root }/objects/#{ object.id }"> <t t-esc="object.display_name"/></a></li></ul></t>', store=True)
     typeact = fields.Char(string='Action Type', default='ir.actions.act_window', store=True)
     help = fields.Html(string='Action Description', translate=True,
                        default='<p class="o_view_nocontent_smiling_face"> Registrar uma nova fatura </p>')
     domain = fields.Char(string='Domain Value', default=lambda self: self.add_dominio()) #inda não funciona
     context = fields.Char(string='Context Value',
                           default="{'default_type_fat': 'fatur_cliente', 'type_fat': 'fatur_cliente'}", required=True)
     view_mode = fields.Char(required=True, default='tree,form,activity')
     view_typeform = fields.Selection([('tree', 'Tree'), ('form', 'Form')], default="form", string='View Type',
                                      required=True)
     num = fields.Char(string="Numero Acta", default='')
     """action = fields.Reference(selection=[('ir.actions.report', 'ir.actions.report'),
                                          ('ir.actions.act_window', 'ir.actions.act_window'),
                                          ('ir.actions.act_url', 'ir.actions.act_url'),
                                          ('ir.actions.server', 'ir.actions.server'),
                                          ('ir.actions.client', 'ir.actions.client')])"""
     #inda não funciona
     @api.model
     def add_dominio(self):
         result = []
         for record in self:
             name = ' ' + record.name
             result.append((name))
         return result


     @api.model
     def create(self, vals):
          vals['codigo'] = self.env['ir.sequence'].next_by_code('tipo.docum.codigo') or _('New')
          vals['num_acao'] = self.env['ir.sequence'].next_by_code('num.acao') or _('New')
          #if self.visualizar_no_menu == True:
          res = super(documento, self).create(vals)
          #if self.visualizar_no_menu == True:
          res.create_form()
          res.create_tree()
          res.create_action()
          res.creat_act_window()
          res.create_menu()
          return res
     @api.one
     def create_form(self):
          if self.visualizar_no_menu == True:
              ir_ui_view = self.env['ir.ui.view']
              arch_db_doc = self.env['ir.ui.view'].search([('name','=','Fatura Cliente Form')])#('id', '=', 436)
              # form
              faturform = ir_ui_view.create({'name': self.name, 'model': self.modelo, 'type': 'form', 'arch_fs': self.arch_fs, 'arch_db': arch_db_doc.arch_db})  # , 'arch_db': self.arch_db
              return faturform

     @api.one
     def create_tree(self):
         if self.visualizar_no_menu == True:
             ir_ui_view = self.env['ir.ui.view']
             arch_db_doc = self.env['ir.ui.view'].search([('name','=','Fatuclient.tree.view')])#('id', '=', 437),
             # Tree
             faturtree = ir_ui_view.create(
                 {'name': self.name, 'model': self.modelo, 'type': 'tree', 'arch_db': arch_db_doc.arch_db, 'arch_fs': self.arch_fs})
             return faturtree

     @api.one
     def create_action(self):
         if self.visualizar_no_menu == True:
             # Action Window View
             # Tabela ir_actions
             ir_actions_actions = self.env['ir.actions.actions']
             faturact_wind = ir_actions_actions.create({'name': self.name, 'model': self.modelo, 'type': self.typeact, 'help': self.help})
             return faturact_wind

     @api.one
     def creat_act_window(self):
         if self.visualizar_no_menu == True:
             # Tabela ir_act_window
             ir_actions_actions = self.env['ir.actions.act_window']
             faturact_wind_filho = ir_actions_actions.create(
                 {'name': self.name, 'model': self.modelo, 'type': self.typeact,
                  'domain': self.domain, 'view_type': self.view_typeform, 'view_mode': self.view_mode,
                  'context': self.context, 'res_model': self.modelo})
             return faturact_wind_filho

     @api.one
     def create_menu(self):
         if self.visualizar_no_menu == True:
             # Menu
             m_actions = self.env['ir.actions.act_window'].search([('name', '=', self.name)])
             menu_pai = self.env['ir.ui.menu'].search([('name', '=', 'Faturas')])
             menu = self.env['ir.ui.menu']
             action = 'ir.actions.act_window,' + str(m_actions.id)
             add_menu = menu.create({'name': self.name, 'parent_id': menu_pai.id, 'help': self.help, 'action': action})
             return add_menu
