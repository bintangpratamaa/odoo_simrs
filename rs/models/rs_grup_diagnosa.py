from odoo import models, fields


class RsDiagnosa(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'rs_grup_diagnosa'
    _description = 'Grup Diagnosa ICD10'

    name = fields.Char(
        string="Grup Diagnosa",
        required=True,
        tracking=True,
        help="Input group diagnose name here")
    grup_diagnosa_kode = fields.Char(
        string="Kode Grup Diagnosa"
    )

    _sql_constraints = [
        ('name_check', 'unique(name)', 'Name must unique!'),
        ('grup_diagnosa_kode_check', 'unique(grup_diagnosa_kode)', 'Grup Diagnosa Kode must be unique!'),
    ]