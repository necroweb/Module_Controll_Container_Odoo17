from odoo import fields, models

# =====================================================
# MODELO 4: CUSTOMER
# =====================================================

class Customer(models.Model):
    _name = 'shipping.customer'
    _description = 'Cliente'
    _order = 'name'

    name = fields.Char(
        string='Cliente',
        required=True,
    )

    extra_days = fields.Integer(
        string='Días extra',
        required=True,
    )

    percentage = fields.Selection(
        selection=[
            ('5', '5%'),
            ('10', '10%'),
        ],
        string='Porcentaje',
        required=True,
    )

    condition_ids = fields.One2many(
        comodel_name='shipping.customer.condition',
        inverse_name='customer_id',
        string='Condiciones por naviera',
    )