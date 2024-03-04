from odoo import api, fields, models


class StockPickingBatch(models.Model):
    _inherit = 'stock.picking.batch'

    vehicle_id = fields.Many2one('fleet.vehicle.model')
    vehicle_category_id = fields.Many2one('fleet.vehicle.model.category')
    weight = fields.Float(compute='compute_weight',readonly= True)
    volume = fields.Float(compute='compute_volume',readonly= True)

    @api.depends("move_line_ids","vehicle_category_id")
    def compute_weight(self):
       w = 0
       for record in self:
           temp = record.move_line_ids
           for product in temp:
               w = w + product.product_id.weight * product.quantity
               
       if self.vehicle_category_id.max_weight>0:
            self.weight = (w/self.vehicle_category_id.max_weight)*100
       else:
            self.weight = w


    @api.depends("move_line_ids","vehicle_category_id")
    def compute_volume(self):
       v = 0
       for record in self:
           temp = record.move_line_ids
           for product in temp:
               v = v + product.product_id.volume * product.quantity
               
       if self.vehicle_category_id.max_volume>0:
            self.volume = (v/self.vehicle_category_id.max_volume)*100
       else:
            self.volume = v
