from odoo import models, fields


class RsDataSdm(models.Model):
    # tambahkan chatter
    _inherit = ["hr.employee"]

    flag_dokter = fields.Boolean(
        string="Dokter")

    flag_dokter = fields.Boolean(
        string="Perawat")

    _order = 'name ASC'