from odoo import models, fields, api
from odoo.exceptions import UserError

class AlquilerProducto(models.Model):

    # Desarrollamos los requirimientos de nuestra clase del modelo
    _name="alquiler.producto"
    _description = "Gestion del Alquiler de Productos"
    _rec_name = "alquilerProd_id"

# Estos son los campos que vamos a utilizar:

    # alquilerProd_id: id del alquiler del producto
    alquilerProd_id = fields.Many2one('alquiler.producto', string='Préstamo', required=True)

    # Campos relacionados: Cliente y Producto
    customer_id = fields.Many2one('res.partner', string='Cliente', related='garantia_id.customer_id', store=True)
    product_id = fields.Many2one('product.product', string='Producto', related='garantia_id.product_id', store=True)

    # Fecha de inicio del préstamo, por defecto será la del día de "hoy" (es decir, la fecha en la que se crea)
    fecha_inicial = fields.Date(string='Fecha de Solicitud', default=fields.Date.context_today, required=True)
    
    # Fecha final del préstamo que depende de la fecha inicial.
    fecha_final = fields.Date(string='Fecha de Solicitud', default=fields.Date.context_today, store=True)

    estado = fields.Selection([
            ('en_alquiler', 'En Alquiler'),
            ('entregado', 'Entregado'),
            ('no_entregado', 'No Entregado')
            ], string='Estado', default='en_alquiler', required=True)