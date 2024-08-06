from odoo import models, fields


class RsDepartment(models.Model):
    # tambahkan chatter
    _inherit = ["hr.department"]
