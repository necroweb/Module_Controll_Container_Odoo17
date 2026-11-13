from odoo import fields, models

class ShippingBookLading(models.Model):
    _name = 'shipping.book.lading'
    _description = 'Conocimiento de embarque'
    _rec_name = 'number_book_lading'
    _order = 'date_discharge desc, number_book_lading'

    number_book_lading = fields.Char(
        string='Número BL',
        required=True,
    )

    shipping_id = fields.Many2one(
        comodel_name='shipping.company',
        string='Naviera',
        required=True,
        ondelete='restrict',
    )

    customer_id = fields.Many2one(
        comodel_name='shipping.customer',
        string='Cliente',
        required=True,
        ondelete='restrict',
    )

    date_discharge = fields.Date(
        string='Fecha de descarga',
        required=True,
    )

    container_ids = fields.One2many(
        comodel_name='shipping.container',
        inverse_name='book_lading_id',
        string='Contenedores',
    )
   