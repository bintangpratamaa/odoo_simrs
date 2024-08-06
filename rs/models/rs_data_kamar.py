from odoo import models, fields


class RsDataKamar(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'rs_data_kamar'
    _description = 'data kamar'

    rs_ruang_id = fields.Many2one("rs_ruang",string="id ruang")
    name = fields.Char(string="jenis kamar")
    #_order = 'prosedur_code ASC'