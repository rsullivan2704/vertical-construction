from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = ['sale.order']
    _description = 'Proposal'

# region fields

    partner_shipping_id = fields.Many2one(
        'res.partner',
        string='Property Address',
        help="Location of the property where works are to be performed.")

    property_owner = fields.Many2one(
        'res.partner',
        string='Property Owner',
        readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=True,
        track_visibility='onchange')

    architect = fields.Many2one(
        'res.partner',
        string='Architect',
        readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=True,
        index=True,
        track_visibility='always')

    struct_engineer = fields.Many2one(
        'res.partner',
        string='Structural Engineer',
        readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=False,
        track_visibility='onchange')

    geo_engineer = fields.Many2one(
        'res.partner',
        string='Geotechnical Engineer',
        readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=False,
        track_visibility='onchange')

    mep_engineer = fields.Many2one(
        'res.partner',
        string='MEP Engineer',
        readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=False,
        track_visibility='onchange')

    interior_designer = fields.Many2one(
        'res.partner',
        string='Interior Designer',
        readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=False,
        track_visibility='onchange')

# endregion

# region methods

@api.multi
@api.onchange('partner_id')
def onchange_partner_id(self):
    """
    Update the following fields when the partner is changed:
    - Property Owner
    """
    if not self.partner_id:
        self.update({
            'property_owner': False,
        })
        return
    values = {
        'property_owner': self.partner_id
    }
    self.update(values)
    super(SaleOrder, self).onchange_partner_id()

# endregion
