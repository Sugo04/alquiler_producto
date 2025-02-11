{
    "name": "Alquiler de Productos",
    "version": "1.0",
    "summary": "Módulo para gestionar el alquiler de productos de la empresa",
    "category": "Custom",
    "author": "Héctor Martín",
    "license": "LGPL-3",
    "depends": ["base", "mail"],
    "icon": "/alquiler_producto/static/description/icon.png",
    "data": [
        "views/alquiler_producto_views.xml",
        "security/ir.model.access.csv"
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
    "description": """
                    Módulo de Odoo con el que gestionaremos el alquiler de los productos en una Empresa. 
                    """,
}