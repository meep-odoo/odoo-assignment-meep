from odoo import fields, models,api


class FleetVehicleModelCategory(models.Model):
    _inherit = 'fleet.vehicle.model.category'
    


    max_weight = fields.Float()
    max_volume = fields.Float()
    
    @api.depends('max_weight','max_volume')
    def _compute_display_name(self):
        for record in self:
            name = f"{record.name}" +"(" +str(record.max_weight)+"kg,"+ str(record.max_volume) +"m3)"
            record.display_name = name
