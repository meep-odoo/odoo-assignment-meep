from odoo import api, fields, models


class StockPickingBatch(models.Model):
    _inherit = 'stock.picking.batch'

    vehicle_id = fields.Many2one('fleet.vehicle.model')
    vehicle_category_id = fields.Many2one('fleet.vehicle.model.category')
    weight = fields.Float(compute='compute_weight',string="Weight",readonly= True,store=True)
    volume = fields.Float(compute='compute_volume',string="Volume",readonly= True,store = True)
    transfer = fields.Float(compute="compute_transfer",string="Transfer",store=True)
    lines = fields.Float(compute='compute_lines',string="Lines",store=True)
    dock = fields.Many2one('dock')
    date_start = fields.Date(default=fields.Date.today)
    date_end = fields.Date()

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

    @api.depends('picking_ids')
    def compute_transfer(self):
          for record in self:
               curr = len(record.picking_ids)
               record.transfer = curr

    @api.depends('move_line_ids')
    def compute_lines(self):
          for record in self:
               curr = len(record.move_line_ids)
               record.lines = curr

    @api.depends('weight','volume')
    def _compute_display_name(self):
         super()._compute_display_name()
         for record in self:
             record.display_name = record.name + f'({record.weight} kg, {record.volume} m³)'
