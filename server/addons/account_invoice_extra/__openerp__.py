# -*- encoding: utf-8 -*-
 
{
    "name": "Mejoras factura para gruas",
    "version": "1.0",
    "description": """
        Permite agregar campos vinculados a las gruas en el formulario de presupuestos
    """,
    "author": "Álvaro Pereira Camiña",
    "website": "",
    "category": "Tools",
    "depends": [
            "account",
            "base",#Este modulo para instalarse debe tener el modulo base y product instalado
                ],
    "data":[
            "account_invoice_extra_view.xml", #todos los archivos xml que posea nuestro modulo se debe de agregarse aqui
          
                ],
    "demo_xml": [
                        ],
    "update_xml": [
                        ],
    "active": False,
    "installable": True,
    "certificate" : "",
}


