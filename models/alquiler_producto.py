from datetime import timedelta, date
from odoo import models, fields, api

class AlquilerProducto(models.Model):
    _name = "alquiler.producto"
    _description = "Gestión del Alquiler de Productos"
    _rec_name = "alquilerProd_id"

    alquilerProd_id = fields.Char(string="ID Préstamo", required=True)

    customer_id = fields.Many2one('res.partner', string='Cliente', required=True)
    product_id = fields.Many2one('product.product', string='Producto', required=True)

    fecha_inicial = fields.Date(string='Fecha Inicio del Préstamo', default=fields.Date.context_today, required=True)

    fecha_final = fields.Date(string='Fecha de Devolución', compute="_compute_fecha_final", store=True)

    estado = fields.Selection([
        ('en_alquiler', 'En Alquiler'),
        ('entregado', 'Entregado'),
        ('no_entregado', 'No Entregado')
    ], string='Estado', default='en_alquiler', required=True)

    observaciones = fields.Text(string="Observaciones")

    @api.depends("fecha_inicial")
    def _compute_fecha_final(self):
        for record in self:
            if record.fecha_inicial:
                record.fecha_final = record.fecha_inicial + timedelta(days=30)

    @api.onchange('product_id')
    def _check_product_availability(self):
        if self.product_id and self.product_id.qty_available <= 0:
            return {
                'warning': {
                    'title': "Producto no disponible",
                    'message': "El producto seleccionado no tiene stock.",
                }
            }

    def marcar_prestamos_vencidos(self):
        fecha_hoy = date.today()
        prestamos_vencidos = self.search([
            ('estado', '=', 'en_alquiler'),
            ('fecha_final', '<', fecha_hoy)
        ])
        if prestamos_vencidos:
            prestamos_vencidos.write({'estado': 'no_entregado'})
