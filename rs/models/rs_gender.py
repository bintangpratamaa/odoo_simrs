from odoo import models, fields


class RsGender(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'rs_gender'
    _description = 'gender'

    name = fields.Selection([('laki-laki','Laki-Laki'),('perempuan','Perempuan')],
        string="gender",
        help="Input gender here")

    _order = 'name ASC'