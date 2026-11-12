from odoo import models, fields, api
from odoo.exceptions import ValidationError

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
        required=True
    )

    # Vigencia de la tarifa
    vigencia = fields.Char(
    string='Vigencia',
    compute='_compute_vigencia',
    store=True,
    
    )
    # Dias libres
    free_days = fields.Integer(
        string='Dias libres',
        compute="_compute_free_days",
        store=True 
    )

    # Relacion: una tarifa puede tener muchos tramos
    tariff_range_ids = fields.One2many(
        comodel_name='shipping.tariff.range',
        inverse_name='tariff_id',
        string='Tramos de tarifa'
    )

    # Funcion para concatenar date_from + date_to
    @api.depends('date_from', 'date_to')
    def _compute_vigencia(self):
        for rec in self:
            if rec.date_from and rec.date_to:
                desde = rec.date_from.strftime('%d/%m/%Y')
                hasta = rec.date_to.strftime('%d/%m/%Y')
                rec.vigencia = f'Desde {desde} hasta {hasta}'
            else:
                rec.vigencia = ''

    # funcion para calcular los dias libres de la tarifa
    @api.depends('date_from', 'date_to')
    def _compute_free_days(self):
        
        for rec in self:

            if rec.date_from and rec.date_to:

                delta = (
                    rec.date_to -
                    rec.date_from
                )

                rec.free_days = delta.days

            else:

                rec.free_days = 0