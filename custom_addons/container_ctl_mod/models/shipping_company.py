class ShippingCompany(models.Model):
    _name = 'shipping.company'
    _description = 'Shipping Company'

    name = fields.Char(required=True)