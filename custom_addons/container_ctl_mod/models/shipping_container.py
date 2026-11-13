from odoo import fields, models


class ShippingContainer(models.Model):
    _name = 'shipping.container'
    _description = 'Contenedor'
    _order = 'book_lading_id, sequence, container_ref'

    sequence = fields.Integer(
        string='N.º',
        default=0,
    )

    container_ref = fields.Char(
        string='Número de contenedor',
        required=True,
    )

    container_type = fields.Selection(
        selection=[
            ('20DV', '20DV'),
            ('40DV', '40DV'),
            ('40HC', '40HC'),
            ('40RF', '40RF'),
        ],
        string='Tipo',
        required=True,
    )

    book_lading_id = fields.Many2one(
        comodel_name='shipping.book.lading',
        string='BL',
        required=True,
        ondelete='cascade',
    )

    shipping_id = fields.Many2one(
        comodel_name='shipping.company',
        string='Naviera',
        related='book_lading_id.shipping_id',
        store=True,
        readonly=True,
    )

    customer_id = fields.Many2one(
        comodel_name='shipping.customer',
        string='Cliente',
        related='book_lading_id.customer_id',
        store=True,
        readonly=True,
    )

    date_discharge = fields.Date(
        string='Fecha de descarga',
        required=True,
    )

    date_return = fields.Date(
        string='Fecha de devolución',
    )

    observations = fields.Text(
        string='Observaciones',
    )
