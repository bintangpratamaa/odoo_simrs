from odoo import models, fields


class RsHubPasien(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'rs_hub_pasien'
    _description = 'hubungan dengan pasien'

    name = fields.Selection([
        ('diri_sendiri', 'Diri Sendiri'),('anak', 'Anak'),('istri', 'Istri'), ('ayah_kandung', 'Ayah Kandung'),('ibu_kandung', 'Ibu Kandung')],

       string="Hubungan dengan pasien",
       help="Input Hubungan dengan pasien")

    _order = 'name ASC'