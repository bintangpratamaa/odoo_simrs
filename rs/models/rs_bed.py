from odoo import models, fields


class RsBed(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'rs_bed'
    _description = 'bed'

    flag_aktif = fields.Boolean(
        string="rs bed",
        help="Input nama bed disini")
    rs_kelas_id = fields.Many2one("rs_kelas")
    name = fields.Char(string="nama kamar")
    
    #_order = 'prosedur_code ASC'