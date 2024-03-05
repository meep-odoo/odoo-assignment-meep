from odoo import api, fields, models


class Dock(models.Model):
    _name = "dock"
    _description = "Dock Model"


    name = fields.Char(string="Dock")
