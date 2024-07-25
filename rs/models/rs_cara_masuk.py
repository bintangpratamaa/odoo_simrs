from odoo import models, fields


class RsCaramasuk(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'rs_cara_masuk'
    _description = 'Cara masuk'

    name = fields.Char(
        string="Cara masuk",
        help="Input cara masuk pasien")

    # _sql_constraints = [
    #    ('name_check', 'unique(name)', 'Poli Name must unique!')
    # ]

    # _order = 'name ASC'