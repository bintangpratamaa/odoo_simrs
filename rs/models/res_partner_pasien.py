from odoo import models, fields, api


class ResPartnerPasien(models.Model):
    _inherit = 'res.partner'

    no_rm = fields.Char(string='Nomor Rekam Medis')
    date_of_birth = fields.Date(string='Date of Birth')
    flag_pasien = fields.Boolean()

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
