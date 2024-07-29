from odoo import models, fields


class RsKamar(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'rs_kamar'
    _description = 'Kamar'

    name = fields.Char(
        string="Kamar",
        help="Input kamar name here")

    _sql_constraints = [
        ('name_check', 'unique(name)', 'Kamar Name must unique!')
    ]
    
    #_order = 'name ASC'