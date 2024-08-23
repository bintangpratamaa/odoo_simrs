from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = ["product.template"]

    flag_obat = fields.Boolean(string="flag obat")
    cacah_yang_dicover_bpjs_per_kunjungan = fields.Char(string="cacah yang dicover bpjs per kunjungan")
    default_aturan = fields.Char(string="default aturan")
    kfa_code = fields.Char(string="kfa code")
