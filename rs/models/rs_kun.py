from odoo import models, fields


class RsKun(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'rs_kun'
    _description = 'Kunjungan'

    res_partner_id = fields.Many2many("res.partner",
        string="pilih pasien",
        help="Input pasien name here")

    tanggal_kunjungan = fields.Date(string="Tanggal Kunjungan")
    rs_jenis_bayar_id = fields.Many2one("rs_jenis_bayar", string="Pilih Jenis Pembayaran")
    rs_unit_id = fields.Many2one("rs_unit", string="Unit Layanan")
    rs_asal_rujukan_id = fields.Many2one("rs_asal_rujukan", string="Asal Rujukan")
    rs_cara_masuk_id = fields.Many2one("rs_cara_masuk", string="Cara Masuk")
    rs_cara_datang = fields.Many2one("rs_cara_datang", string="Cara Datang")

    dokter_hr_employee_id = fields.Many2many("hr.employee", string="Dokter Penanggung Jawab")


    pj_nama = fields.Char(string="Nama Penanggung Jawab")
    pj_rs_hub_pasien_id = fields.Char(string="Hubungan dengan pasien")
    pj_no_telepon = fields.Char(string="No Telp Penanggung Jawab")
    pj_bahasa = fields.Char(string="Bahasa Penanggung Jawab")
    pj_jenis_kelamin_id = fields.Char(string="Penanggung Jawab Jenis Kelamin")
    pj_umur = fields.Char(string="Umur Penanggung Jawab")
    pj_pekerjaan = fields.Char(string="PIC Pekerjaan Penunggu")
    pj_alamat = fields.Char(string="Alamat Penanggung Jawab")
    pj_keterangan = fields.Char(string="Keterangan")

    #_sql_constraints = [
        #('name_check', 'unique(name)', 'Kamar Name must unique!')
    #]
    
    #_order = 'name ASC'