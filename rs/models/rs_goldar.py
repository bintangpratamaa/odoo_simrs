from odoo import models, fields


class RsGoldar(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'rs_goldar'
    _description = 'goldar'

    name = fields.Char(
        string="Gologan Darah",
        help="Input golongaan darah name here")
    
    _order = 'name ASC'