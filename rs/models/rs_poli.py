from odoo import models, fields


class RsPoli(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'rs_poli'
    _description = 'Poli'

    name = fields.Char(
        string="Poli",
        required=True,
        tracking=True,
        help="Input poli name here")
    description = fields.Text()

    _sql_constraints = [
        ('name_check', 'unique(name)', 'Poli Name must unique!')
    ]