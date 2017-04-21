from openerp.osv import fields, osv
from openerp import netsvc

class sale_order(osv.osv):

    _inherit = 'sale.order'

    def create(self, cr, uid, vals, context=None):
        if vals.get('name','/')=='/':
            vals['name'] = self.pool.get('ir.sequence').get(cr, uid, 'sale.order') or '/'
        result = super(sale_order, self).create(cr, uid, vals, context=context)
        wf_service = netsvc.LocalService('workflow')
        wf_service.trg_validate(uid, 'sale.order', result, 'order_confirm', cr)
        return result
