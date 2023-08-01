from odoo import models, fields, api


class configurations(models.Model):
    _name = 'configurations.configurations'
    _description = 'configurations.configurations'

    n125 = fields.Char()
