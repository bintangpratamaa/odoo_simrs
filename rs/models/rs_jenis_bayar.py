from odoo import models, fields


class RsJenisBayar(models.Model):
    _name = 'rs_jenis_bayar'
    _description = 'Jenis Pembayaran Pasien'

    name = fields.Char(string='Jenis Pembayaran', required=True)
    description = fields.Text(string='Deskripsi')
