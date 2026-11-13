from odoo import api, fields, models


class ShippingCustomerCondition(models.Model):
    _name = 'shipping.customer.condition'
    _description = 'Condición de cliente por naviera'
    _order = 'customer_id, shipping_id'

    customer_id = fields.Many2one(
        comodel_name='shipping.customer',
        string='Cliente',
        required=True,
        ondelete='cascade',
    )

    shipping_id = fields.Many2one(
        comodel_name='shipping.company',
        string='Naviera',
        required=True,
        ondelete='restrict',
    )

    extra_days = fields.Integer(
        string='Días extra',
        required=True,
        default=0,
    )

    percentage = fields.Selection(
        selection=[
            ('5', '5%'),
            ('10', '10%'),
        ],
        string='Porcentaje acordado',
        required=True,
    )

    _sql_constraints = [
        (
            'customer_shipping_unique',
            'UNIQUE(customer_id, shipping_id)',
            'Ya existe una condición para este cliente y esta naviera.',
        )
    ]

    @api.model
    def default_get(self, fields_list):
        values = super().default_get(fields_list)
        customer_id = (
            values.get('customer_id')
            or self.env.context.get('default_customer_id')
        )
        if customer_id:
            customer = self.env['shipping.customer'].browse(customer_id)
            if 'extra_days' in fields_list and not values.get('extra_days'):
                values['extra_days'] = customer.extra_days
            if 'percentage' in fields_list and not values.get('percentage'):
                values['percentage'] = customer.percentage
        return values
