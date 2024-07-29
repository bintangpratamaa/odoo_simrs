from odoo import models, fields


class RsPoli(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'rs_unit'
    _description = 'Unit Layanan'

    name = fields.Char(
        string="Unit Layanan",
        required=True,
        tracking=True)
    description = fields.Text()

    _sql_constraints = [
        ('name_check', 'unique(name)', 'Unit Name must unique!')
    ]