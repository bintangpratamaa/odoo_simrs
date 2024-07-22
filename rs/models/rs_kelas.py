from odoo import models, fields


class RsKelas(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'rs_kelas'
    _description = 'kelas'

    name = fields.Char(
        string="kelas",
        help="Input kelas kamar here")

    _order = 'name ASC'