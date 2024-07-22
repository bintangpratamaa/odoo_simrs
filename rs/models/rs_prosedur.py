from odoo import models, fields


class RsProsedur(models.Model):
    # tambahkan chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _name = 'rs_prosedur'
    _description = 'prosedur'

    name = fields.Char(
        string="nama prosedur",
        help="Input nama prosedur disini")
    prosedur_code = fields.Char(
        string="prosedur kode",
        help="Input prosedur kode disini")
    
    _order = 'prosedur_code ASC'