from odoo import models, fields


class RsAgama(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'rs.agama'
    _description = 'agama'

    name = fields.Char(
        string="agama",
        help="Input agama name here")

    _sql_constraints = [
        ('name_check', 'unique(name)', 'Poli Name must unique!')
    ]
    
    #_order = 'name ASC'