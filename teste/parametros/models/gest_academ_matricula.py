# -*- coding: utf-8 -*-


from odoo import api, fields, models, exceptions


class matricula(models.Model):
    _name = 'matricula.matricula'
    _rec_name = 'ano_lectivo'
    _description = 'Matricula'

    numero_matricula = fields.Integer()
    data =fields.Date(default=fields.Date.today, string="DataE")
    aluno = fields.Many2one('aluno.aluno')
    ano_lectivo = fields.Many2one('ano.lectivo')
    curso = fields.Many2one('curso.curso')
    ano = fields.Selection([('primeiro_ano', 'Primeiro Ano'),
                            ('segundo_ano', 'Segundo Ano'),
                            ('terceiro_ano', 'Terceiro Ano'),
                            ('quarto_ano', 'Quarto Ano'),
                            ('quinto_ano', 'Quinto Ano')], default='primeiro_ano')
    tipo_matricula = fields.Selection([('mtriculaNormal', 'Matricula Normal'),
                                       ('desciplinaAtrasso', 'Desciplina(s) em Atrasso')], default='mtriculaNormal')
    bolsario = fields.Boolean()
    primeira_ves = fields.Boolean()
    desciplina_atrazo = fields.Boolean()

    matricula = fields.Float(string="Valor")
    curso_val = fields.Float()
    semestre1 = fields.Float()
    semestre2 = fields.Float()
    prest1 = fields.Float()
    prest2 = fields.Float()
    obs = fields.Text()
    ger_cont_corent = fields.Boolean()

    #CAmpos apresentado na grid Imprimir documento
    documento_factura_id = fields.Many2one('imprimir.documento.fatura')
    ok = fields.Boolean(string="OK")
    codigo_id_aluno = fields.Integer(string="Codigo", related="aluno.id", store=True)
    numero = fields.Integer(string="Numero", related="aluno.id", store=True)
    nome = fields.Char(string="Nome", related="aluno.name", store=True)
    utilizador_id = fields.Many2one('res.users', string="Utilizador", default=lambda self: self.env.user)
