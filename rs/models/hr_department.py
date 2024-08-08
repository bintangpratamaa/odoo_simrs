from odoo import models, fields


class RsDepartment(models.Model):
    # tambahkan chatter
    _inherit = ["hr.department"]

    #flag_department = fields.Boolean(string="flag department")
    name = fields.Char(string="name")

    #@api.model
    #def create(self, vals):
        #if self.env.context.get('force_flag_department_true', False):
            #vals['flag_department'] = True
        #else:
            #vals['flag_department'] = False
        #return super(RsDepartment, self).create(vals)

    #@api.constrains('flag_department', 'is_company')
    #def _check_flag_pasien(self):
        #for record in self:
            #if record.flag_department and record.is_company:
                #raise ValidationError("Flag Department hanya bisa dicentang jika bukan perusahaan.")
