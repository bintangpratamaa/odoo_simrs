from odoo import models, fields


class RsStatkawin(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'rs_stat_kawin'
    _description = 'stat kawin'

    name = fields.Char(
        string="status kawin",
        help="Input status kawin anda disini")
    
    _order = 'name ASC'