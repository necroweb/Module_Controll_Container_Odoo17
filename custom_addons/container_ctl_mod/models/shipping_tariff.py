from odoo import fields, models

# =====================================================
# MODELO 2: TARIFAS DE NAVIERAS
# =====================================================

class ShippingTariff(models.Model):
    _name = 'shipping.tariff'
    _description = 'Tarifa de Naviera'
    _order = 'date_from desc'

    # Nombre descriptivo de la tarifa
    name = fields.Char(
        string='Referencia tariff',
        store=True
    )

    # Relacion con la naviera
    shipping_id = fields.Many2one(
        comodel_name='shipping.company',
        string='Naviera',
        required=True,
        ondelete='restrict'
    )

    # Tipo de contenedor
    container_type = fields.Selection(
        selection=[
            ('20DV', '20DV'),
            ('40DV', '40DV'),
            ('40HC', '40HC'),
            ('40RF', '40RF'),
        ],
        string='Tipo de contenedor',
        required=True
    )

    # Fecha inicial de vigencia
    date_from = fields.Date(
        string='Fecha desde',
        required=True
    )

    # Fecha final de vigencia
    date_to = fields.Date(
        string='Fecha hasta',
        required=False
    )

    # Días libres acordados en la tarifa, independiente de su vigencia
    free_days = fields.Integer(
        string='Dias libres',
        required=True,
        default=0,
    )

    # Relacion: una tarifa puede tener muchos tramos
    tariff_range_ids = fields.One2many(
        comodel_name='shipping.tariff.range',
        inverse_name='tariff_id',
        string='Tramos de tarifa'
    )

