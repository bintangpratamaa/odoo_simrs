from odoo import models, fields


class RsInstalation(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'rs_installation'
    _description = 'department'

    rs_installation_id = fields.Many2one("hr.department",
        string="pilih department",
        help="Input department here")