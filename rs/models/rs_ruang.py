from odoo import models, fields


class RsRuang(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'rs_ruang'
    _description = 'Ruangan'

    name = fields.Char(
        string="Ruangan",
        help="Input nama ruangan")

    _sql_constraints = [
        ('name_check', 'unique(name)', 'Ruangan Name must unique!')
    ]
    
    #_order = 'name ASC'