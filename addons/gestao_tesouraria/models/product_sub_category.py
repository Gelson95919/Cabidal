# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
class productSubCategory(models.Model):
     _name = 'product.sub.category'
     _description = "product sub category"
     # campo de seleção para categoria pai.
     parent_category = fields.Selection([('is_living_room', 'Living Room'),
                                         ('is_kitchen_stuff', 'Kitchen &amp; Dining'),
                                         ('is_bed', 'Bedroom'),
                                         ('is_home_office', 'Home Office'),
                                         ('is_other', 'Other')], string='Category')
     benificiario = fields.Many2one('terceiro.terceiro', string='Beneficiário')  # para remover
     name = fields.Char('Name')
     idade = fields.Integer(string="Idade")
     apelido = fields.Char(string="Apelito")
     morada = fields.Char(string="Morada")
     product_template_meu_ids = fields.Many2one('product.template.meu')
     displlay_type = fields.Selection([('line_section', 'section'), ('line_note', 'nota')], string='displlay')


class productTemplate(models.Model):
     _name = "product.template.meu"
     _description = "product template meu"

     is_living_room = fields.Boolean(string='Living Room')
     is_kitchen_stuff = fields.Boolean(string='Kitchen & Dining')
     is_bed = fields.Boolean(string='Bedroom')
     is_home_office = fields.Boolean(string='Home Office')
     is_other = fields.Boolean(string='Other')

     # => campos booleanos para caixas de seleção.
     sub_categ_ids_m2o = fields.Many2one('product.sub.category', string='Select Sub category')
     # =>não se esqueça de criar o objeto para many2one relation neste caso 'product.sub.category'.
     product_sub_category_ids = fields.One2many('product.sub.category', 'product_template_meu_ids')

     # use api.onchange. A função precisa ser acionada quando os campos booleanos são alterados.
     @api.onchange('is_living_room', 'is_bed', 'is_kitchen_stuff', 'is_home_office', 'is_other')
     def onchange_categ(self):
          # crie a lista que conterá a categoria selecionada para definir o campo many2one.
          selected_categ = []
          res = {}

          # aqui o condicional para acrescentar ou remover a cadeia de categoria pai na lista para uso para definir o many2one.

          if self.is_living_room:
               selected_categ.append('is_living_room')

          if self.is_living_room is False:
               if 'is_living_room' in selected_categ:
                    selected_categ.remove('is_living_room')

          if self.is_bed:
               selected_categ.append('is_bed')
          if self.is_bed is False:
               if 'is_bed' in selected_categ:
                    selected_categ.remove('is_bed')
          if self.is_kitchen_stuff:
               selected_categ.append('is_kitchen_stuff')
          if self.is_kitchen_stuff is False:
               if 'is_kitchen_stuff' in selected_categ:
                    selected_categ.remove('is_kitchen_stuff')
          if self.is_home_office:
               selected_categ.append('is_home_office')
          if self.is_home_office is False:
               if 'is_home_office' in selected_categ:
                    selected_categ.remove('is_home_office')
          if self.is_other:
               selected_categ.append('is_other')
          if self.is_other is False:
               if 'is_other' in selected_categ:
                    selected_categ.remove('is_other')

          # Agora, definimos o domínio de campo many2one com a lista de IDs selecionados.
          res.update({'domain': {'sub_categ_ids_m2o': [('parent_category', '=', list(set(selected_categ)))], }})

          return res

