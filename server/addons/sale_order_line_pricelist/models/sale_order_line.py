# -*- coding: utf-8 -*-
import logging
from openerp.osv import fields, osv
from openerp import tools
from openerp import models, api, exceptions 



class sale_order_line(osv.osv):
    _inherit='sale.order.line'
    _columns= {
#        'x_accion': fields.related('order_id', 'pricelist_id', 'name', type='char', string='Product Category', store=True, readonly=True),
#	'x_tarifas': fields.related(
#	    'order_id',
#   	    'pricelist_id',
 #   	    type="many2one",
  #  	    relation="sale.order",
   # 	    string="Complemento",
    #	    store=True),
#	'x_prueba' : fields.Text('Texto'),
#        'x_accion': fields.Many2one('product.pricelist', 'Complemento', required=False, readonly=False, help="Pricelist for current sales order."), 
    }

#    def _get_line_price(self):
#        res = self.env.get('sale.order').search(cr, uid, [('id','=',pricelist_id.id)], context=context)
#        return return res and res[0] or False


 #   _defaults= {
 #       'x_accion':  _get_line_price,
 #   }           

#    def _get_line_price(self):
#        res = self.env.get('sale.order').search(cr, uid, [('id','=',pricelist_id.id)], context=context)
#        return return res and res[0] or False

sale_order_line()
