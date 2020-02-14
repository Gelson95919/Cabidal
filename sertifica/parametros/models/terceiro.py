# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class terceiro(models.Model):
     _name = 'terceiro.terceiro'
     _description = 'Terceiro'
     name = fields.Char(string='Nome/Razão')
     _order = 'id,name'
     #_rec_name = 'name'
     #date_release = fields.Date('Data lançamento', style="width:180px")
     codigo = fields.Char(string="Código", copy=False, index=True,  default=lambda self: _('New'))#readonly=True, index=True,  default=lambda self: _('New')
     controlo = fields.Boolean(string='Controla Reg padrao', store=True)#controla aquele registro padrão pa não aparecer no list

     street = fields.Char()
     street2 = fields.Char()
     city = fields.Char()
     state_id = fields.Many2one()
     zip = fields.Char()
     country_id = fields.Many2one('nacionalidade.nacionalidade')
     image = fields.Binary('Logo', store=True)
     type = fields.Integer()
     Slogan = fields.Char()
     website = fields.Char()
     email = fields.Char()
     utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)

     phone = fields.Integer('Telefone')#para remover
     fax = fields.Integer('Fax')#para remover
     nif = fields.Integer('NIF')#para remover

     nif_pessoa = fields.Char(string="NIF Terc")#, required=True, size=9
     telefone_pessoa = fields.Char(string="Telefone Terc")#, size=7
     fixo_pessoa = fields.Char(string="Fax Terc")#, required=True, size=7

     nib = fields.Integer('NIB')
     moeda_id = fields.Many2one('moeda.moeda', string='Moeda')
     report_footer = fields.Text('Rodapé')
     state = fields.Selection([('individual', 'Individual'), ('enpresa', 'Empresa')], 'Tipo Sujeito', Widget="radio", default='enpresa')
     clientes = fields.Boolean('Cliente', store=True)
     fornecedores = fields.Boolean('Fornecedores', store=True)
     trabalhadores = fields.Boolean('Trabalhadores', store=True)
     socios = fields.Boolean('Socios', store=True)
     entidades_estatais = fields.Boolean('Entidades Estatais', store=True)
     condicao_pagamento = fields.Many2one('pagamento.pagamento', string='Condição Pagamento')
     fiscal_lins = fields.One2many('fiscal', 'terceiro_id', string='Fiscal Lines', oldname='fiscais_line',)
     filiais=fields.One2many('filiais.filiais', 'terceiro_id', string='filial_lenes', oldname='filiais_lines')
     controlo_subc = fields.Boolean(string='Activar Controlo Subcidiario')

     tem_solicitacao = fields.Selection([('1', 'Sim'), ('2', 'Não')], string="Tem Documento", store=True)
     tem_pedido = fields.Selection([('1', 'Sim'), ('2', 'Não')], string="Tem Pedido", default='2')
     tem_despesas = fields.Boolean(string="Tem Despesas", store=True)
     tem_fatur = fields.Boolean(string="Tem Fatura", store=True)
     receb_pess = fields.Boolean(string='Receb Pessoa', default=False)
     pessoa = fields.Boolean(string='Receb Pessoa', store=True)
     _sql_constraints = [('nif_unique', 'unique(nif)', 'Nif ja existe!')]
     ata_id = fields.Integer(string="ID Ata")#para facilitar na algumas procedimento de ata
     cliente_fornecdor = fields.Boolean()
     #PESSOA
     tipo = fields.Selection([('terceiro', 'Terceiro'), ('pessoa', 'Pessoa')], eadonly=True, index=True, change_default=True,
          track_visibility='always', default=lambda self: self._context.get('type', 'terceiro'),)
     mud_id = fields.Boolean(string="Mudar ID", default=True)

     #@api.model
     #def _get_next_cod(self):
     #     sequence = self.env['ir.sequence'].search([('code', '=', 'pessoa.codigo')])
     #     next = sequence.get_next_char(sequence.number_next_actual)
     #     return next


     @api.model
     def create(self, vals):
          terc = self.env['terceiro.terceiro'].search([('receb_pess', '=', True)])
          if not terc:
             vals['codigo'] = self.env['ir.sequence'].next_by_code('terceiro.codigo') or _('New')
          res = super(terceiro, self).create(vals)
          return res


     @api.multi
     def name_get(self):
          result = []
          for record in self:
               name = '' + str(record.codigo) + ' ' + ' ' + record.name
               result.append((record.id, name))
          return result


     #Validacao dos campos
     @api.multi
     @api.constrains('nif', 'telefone_fixo', )
     def _check_size(self):
          nif = str(self.nif_pessoa)
          telef = str(self.telefone_pessoa)
          if (nif.isnumeric()) == True:
               if len(str(nif)) < 9:
                    raise ValidationError('O campo NIF recebe 9 dígitos!')
          else:
               raise ValidationError('O campo NIF tem que ser numerico e 9 dígitos!')

          if (telef.isnumeric()) == True:
               if len(str(telef)) < 7:
                    raise ValidationError('O campo Telefone recebe 7 dígitos!')
          else:
               raise ValidationError('O campo Telefone tem que ser numerico e 7 dígitos!')




class fiscal(models.Model):
    _name = 'fiscal'

    _description = 'Fiscal de Terceiro'
    terceiro_id = fields.Many2one('terceiro.terceiro')
    tipo = fields.Selection(
         [('cliente', 'Cliente'), ('fornecedor', 'Fornecedor'),
          ('funcionário/trabalhador', 'Funcionário / Trabalhador'),
          ('socio / acionista', 'Socio / Acionista'), ('setor publico estatal', 'Setor Publico Estatal')],
         'Tipo')
    conta = fields.Many2one('planconta.planconta', string='Conta')
    diario = fields.Many2one('diario.diario', string='Diario', )
