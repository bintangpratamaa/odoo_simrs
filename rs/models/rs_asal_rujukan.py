from odoo import models, fields


class RsAsalrujukan(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'rs_asal_rujukan'
    _description = 'Asal Rujukan'

    name = fields.Char(
        string="Asal Rujukan",
        help="Input asal rujukan pasien")

    # _sql_constraints = [
    #    ('name_check', 'unique(name)', 'Poli Name must unique!')
    # ]

    # _order = 'name ASC'