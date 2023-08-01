from odoo import models, fields, api


class admissionregister(models.Model):
    _name = 'admissionregister.admissionregister'
    _description = 'admissionregister.admissionregister'

 # personalinformation
    na1 = fields.Char(required=True)
    na2 = fields.Char(required=True)
    na3 = fields.Char(required=True)
  # schoolinformation
    na4 = fields.Char(string="School", required=True)
    na5 = fields.Date(string="AccademicYear")
    na6 = fields.Char(string="Address")
    na7 = fields.Char("")
    na8 = fields.Char(string="", required=True)
       # gp2
    na9 = fields.Char(string="", required=True)
    na10 = fields.Char(string="", required=True)
    na11 = fields.Char(string="", required=True)
 # classinformation
    na12 = fields.Char(string="Medium")
    na13 = fields.Char(string="Class")
    na14 = fields.Integer(string="Phone")
    na141 = fields.Integer(string="Phone")
    na15 = fields.Char(string="Email")
    na16 = fields.Char(string="Weblink")
 # generalinformation
    na17 = fields.Char(string="Gender", required=True)
    na18 = fields.Date(string="Birthdate", required=True)
    na19 = fields.Integer(string="Age")
    na1117 = fields.Integer(string="Mother tongue")
    na1118 = fields.Integer(string="Admssiondate")
    na1119 = fields.Integer(string="select marital status")


 # emergencycontactdeatails
    na20 = fields.Integer(string="phonenumber")
    na21 = fields.Integer(string="Mobilenumber")












#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
