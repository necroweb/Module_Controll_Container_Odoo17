from odoo import fields, models

# =====================================================
# MODELO 1: NAVIERA
# =====================================================

class ShippingCompany(models.Model):
    _name = 'shipping.company'
    _description = 'shipping line'
    _order = 'name'
  
    # Nombre de la naviera
    name = fields.Char(
        string='name shipping company',
        required=True
    )

    # Estado de la naviera
    active = fields.Boolean(
        string='Activo',
        default=True
    )

    # Relacion: una naviera puede tener muchas tarifas
    tariff_ids = fields.One2many(
        comodel_name='shipping.tariff',
        inverse_name='shipping_id',
        string='Tarifas'
    )

    _sql_constraints = [
        (
            'shipping_company_name_unique',
            'UNIQUE(name)',
            'El nombre de la naviera ya existe.'
        )
    ]