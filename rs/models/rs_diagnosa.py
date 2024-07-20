from odoo import models, fields


class RsDiagnosa(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'rs_diagnosa'
    _description = 'Diagnosa ICD10'

    name = fields.Char(
        string="Diagnosa",
        required=True,
        tracking=True,
        help="Input diagnose name here")
    diagnosa_kode = fields.Char(
        string="Kode Diagnosa"
    )
    flag_menular = fields.Boolean(
        string="Menular"
    )
    flag_non_spesialis = fields.Boolean(
        string="Non Spesialis"
    )

    _sql_constraints = [
        # ('name_check', 'unique(name)', 'Name must unique!'),
        ('diagnosa_kode_check','unique(diagnosa_kode)', 'Diagnosa kode must be unique!'),
    ]

    _order = 'diagnosa_kode ASC'