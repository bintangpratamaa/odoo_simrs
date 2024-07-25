from odoo import models, fields


class RsCaradatang(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'rs_cara_datang'
    _description = 'Cara Datang'

    name = fields.Char(
        string="Cara datang",
        help="Input cara datang pasien")

    # _sql_constraints = [
    #    ('name_check', 'unique(name)', 'Poli Name must unique!')
    # ]

    # _order = 'name ASC'