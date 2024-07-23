from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ResPartnerPasien(models.Model):
    _inherit = 'res.partner'

    no_rm = fields.Char(string='Nomor Rekam Medis')
    date_of_birth = fields.Date(string='Date of Birth')
    flag_pasien = fields.Boolean()
    datetime_pendaftaran = fields.Datetime(string='Tanggal dan Jam Pendaftaran',
                                           default=lambda self: fields.Datetime.now())
    rs_agama_id = fields.Many2one("rs_agama")
    rs_goldar_id = fields.Many2one("rs_goldar")
    rs_stat_kawin_id = fields.Many2one("rs_stat_kawin")

    @api.model
    def create(self, vals):
        if self.env.context.get('force_flag_pasien_true', False):
            vals['flag_pasien'] = True
        else:
            vals['flag_pasien'] = False
        return super(ResPartnerPasien, self).create(vals)

    _sql_constraints = [
        ('no_rm_unique', 'unique(no_rm)', 'Nomor Rekam Medis sudah ada!'),
    ]

    @api.constrains('flag_pasien', 'is_company')
    def _check_flag_pasien(self):
        for record in self:
            if record.flag_pasien and record.is_company:
                raise ValidationError("Flag Pasien hanya bisa dicentang jika bukan perusahaan.")
