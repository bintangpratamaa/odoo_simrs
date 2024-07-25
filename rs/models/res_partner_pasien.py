from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ResPartnerPasien(models.Model):
    _inherit = 'res.partner'

    no_rm = fields.Char(string='Nomor Rekam Medis')
    date_of_birth = fields.Date(string='Date of Birth')
    flag_pasien = fields.Boolean(string='Pasien')
    datetime_pendaftaran = fields.Datetime(string='Tanggal dan Jam Pendaftaran',
                                           default=lambda self: fields.Datetime.now())
    rs_agama_id = fields.Many2one("rs_agama",string='Agama')
    rs_goldar_id = fields.Many2one("rs_goldar",string='Golongan Darah')
    rs_stat_kawin_id = fields.Many2one("rs_stat_kawin",string='Status Perkawinan')
    rs_gender_id = fields.Many2one("rs_gender",string='Jenis Kelamin')
    address = fields.Char(string="Alamat")
    no_kk = fields.Char(string="Nomor Kartu Keluarga", help="masukan nomor kartu keluarga")
    no_nik = fields.Char(string="NIK", help="masukan nomor induk kependudukan")
    no_kis = fields.Char(string="Nomor KIS/BPJS", help="masukan nomor Kartu Indonesia Sehat")
    no_hp = fields.Char(string="Nomor HP", help="masukan no hp",default='08')
    tempat_lahir = fields.Char(string="Tempat Lahir")
    pendidikan = fields.Selection([("sd/mi","SD/MI"),("smp/mts","SMP/MTS"),("sma/k/ma","SMA/K/MA")], string="Pendidikan",help="Pendidikan Terakhir")
    pekerjaan = fields.Char(string="Pekerjaan")
    suku = fields.Char(string="Nama Suku",help="contoh suku jawa")
    zip_code = fields.Integer(string="Kode Pos")
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
