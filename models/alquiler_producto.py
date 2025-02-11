from datetime import timedelta
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
    fecha_inicial = fields.Date(string='Fecha Inicio del Pŕestamo', default=fields.Date.context_today, required=True)
    
    # Fecha final del préstamo que depende de la fecha inicial.
    fecha_final = fields.Date(string='Fecha de Devolución', default=fields.Date.context_today, store=True)

    # Estado del préstamo
    estado = fields.Selection([
            ('en_alquiler', 'En Alquiler'),
            ('entregado', 'Entregado'),
            ('no_entregado', 'No Entregado')
            ], string='Estado', default='en_alquiler', required=True)

    # Campo de Observaciones
    observaciones= fields.Text(string="Observaciones");
    
    # Darle la fecha a fecha_final la cual depende de la fecha_inicial
    @api.depends("fecha_inicial")
    def _compute_fecha_final(self):
        for record in self:
            if record.fecha_inicial:
                record.fecha_final= record.fecha_inicial + timedelta(days=30)
            else:
                record.fecha_final=False
    
    @api.onchange('product_id')
    def _check_product_availability(self):
        if self.product_id and self.product_id.qty_available <= 0:
            return {
                'warning': {
                    'title': "Producto no disponible",
                    'message': "El producto seleccionado no está disponible en stock.",
                }
            }

    # Para el cron job: actualizamos el estado seguún la fecha final
    #def _compute_status():
