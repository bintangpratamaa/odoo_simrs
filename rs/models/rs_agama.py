from odoo import models, fields


class RsAgama(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'rs_agama'
    _description = 'Agama'

    name = fields.Char(
        string="Agama",
        help="Input agama name here")

    _sql_constraints = [
        ('name_check', 'unique(name)', 'Poli Name must unique!')
    ]
    
    #_order = 'name ASC'