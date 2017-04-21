# -*- encoding: utf-8 -*-
 
#importa la clase osv del modulo osv y fields
from openerp.osv import fields, osv
 
#Crea una clase llamada datos_presupuesto que hereda de la clase datos_presupuesto padre que esta en /opt/openerp/server/openerp/addons/product
#En openobject hay varios tipos de herencia averiguar mas del tema
#Aqui las clases tienen un atributo _name que es el nombre de la tabla que existe o se creara cuando instala el modulo en postgresql
 
class datos_factura(osv.osv):
    _name = 'account.invoice' # Aqui va el mismo nombre de la clase que se hereda
    _inherit = 'account.invoice' # Permite la herencia propiamente dicho del modulo product 
 
    #Agrega varios campos al formulario de sale_order o a la tabla datos_presupuesto
    _columns = {
                'x_recogido': fields.char('Nombre asistido',size=40),
		'x_vehiculo': fields.char('Vehiculo',size=40),
		'x_matricula': fields.char('Matricula',size=10),
		'x_comentarios': fields.text('Comentarios'),
		'x_telefono': fields.char('Teléfono',size=15, required=False),
#		'only_allowed_products' : fields.Boolean(string="Use only allowed products", help="If checked, you will only be able to select products that have " "this customer added to their customer list."),
#   		'allowed_products' : fields.Many2many(comodel_name='product.product', string='Allowed products'),
   		'x_categ_id' : fields.many2one ('product.category', 'Acción'),
#   		'x_remolque' : fields.selection (('Turismo','Accesorios'),('Componentes','Componentes'),'Extra')
		}
 #   @api.multi
 #   def onchange_partner_id(self, partner_id):
 #       result = super(datos_factura, self).onchange_partner_id(partner_id)
 #       partner = self.env['res.partner'].browse(partner_id)
 #       result['value']['only_allowed_products'] = (
 #           partner.commercial_partner_id.sale_only_allowed)
 #       return result

#    @api.one
#    @api.onchange('pricelist_id')
#    def onchange_only_allowed_products(self):
#        product_obj = self.env['product.product']
#        self.x_allowed_product = product_obj.search([('sale_ok', '=', True)])
#        if self.partner_id:
#            supplierinfos = self.env['product.supplierinfo'].search(
#                [('type', '=', 'customer'),
#                 ('name', 'in', (self.partner_id.commercial_partner_id.id,
#                                 self.partner_id.id))])
#            self.x_allowed_product = product_obj.search(
#                [('product_tmpl_id', 'in',
#                  [x.product_tmpl_id.id for x in supplierinfos])])		
	
        
datos_factura()

