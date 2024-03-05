{
    'name' : "stock transport",
    'version': '1.0',
    'depends':['base','fleet','stock_picking_batch'],
    'data':[
          'security/ir.model.access.csv',
          'views/fleet_vehicle_model_category_views.xml',
          'views/stock_picking_batch_views.xml',
          'views/stock_picking_views.xml'
        ],
    'author': "Meep",
    'application':True,
    'installable':True,
    # data files always loaded at installation
    # data files containing optionally loaded demonstration data
}
