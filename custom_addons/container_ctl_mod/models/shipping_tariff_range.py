from odoo import models, fields
from odoo.exceptions import ValidationError

# =====================================================
# MODELO 3: TRAMOS DE TARIFAS
# =====================================================

class ShippingTariffRange(models.Model):
    _name = 'shipping.tariff.range'
    _description = 'Tramos de Tarifas'
    _order = 'sequence, day_start, id'

    # Relacion con la tarifa
    tariff_id = fields.Many2one(
        comodel_name='shipping.tariff',
        string='Tarifa',
    )

    sequence = fields.Integer(default=10)
   
    day_start = fields.Integer(
        string="Desde Día"
    )

    day_end = fields.Integer(
        string="Hasta Día"
    )

    price_usd = fields.Float(
        string="Precio USD"
    )

