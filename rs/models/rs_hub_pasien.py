from odoo import models, fields


class RsHubPasien(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'rs_hub_pasien'
    _description = 'hubungan dengan pasien'

    name = fields.Char(

       string="Hubungan dengan pasien",
       help="Input Hubungan dengan pasien")

    #_order = 'name ASC'