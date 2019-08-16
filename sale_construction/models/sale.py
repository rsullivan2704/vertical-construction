from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = ['sale.order']
    _description = 'Proposal'

# region fields

    state = fields.Selection([
            ('draft', 'Proposal'),
            ('sent', 'Proposal Sent'),
            ('sale', 'Awarded'),
            ('done', 'Locked'),
            ('cancel', 'Cancelled'),
        ],
        string='Status',
        readonly=True,
        copy=False,
        index=True,
        track_visibility='onchange',
        default='draft')

    documents = fields.Many2many(
        string=u'Documents',
        comodel_name='base_construction.construction.document'
    )

    document_count = fields.Integer(
        compute="compute_document_count"
    )

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

    # @api.multi
    # def compute_attachments(self):
    #     attachment_model = self.env['ir.attachment']
    #     self.attachments = attachment_model.search(
    #         [
    #             ('res_model', '=', 'sale.order'),
    #             ('res_id', '=', self.id),
    #             ('type', 'in', ('binary', 'url'))
    #         ])

    @api.multi
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        """
        Update the following fields when the partner is changed:
        - property_owner
        """
        super(SaleOrder, self).onchange_partner_id()
        if not self.partner_id:
            self.update({
                'property_owner': False,
            })
            return
        values = {
            'property_owner': self.partner_id
        }
        self.update(values)

    @api.multi
    @api.onchange('property_owner')
    def onchange_property_owner(self):
        '''
        Update the following fields when the property owner is changed:
        - partner_shipping_id
        '''
        if not self.property_owner:
            self.update({
                'partner_shipping_id': False
            })
            return
        values = {
            'partner_shipping_id': self.property_owner
        }
        self.update(values)

    @api.multi
    def action_view_documents(self):
        docs = self.mapped('documents')
        view = self.env['ir.ui.view'].search([(
            'name', '=', 'base_construction.construction_document_view_tree')])
        domain = [('id', 'in', docs.ids)]
        return {
            'type': 'ir.actions.act_window',
            'name': 'Documents',
            'res_model': 'base_construction.construction.document',
            'src_model': 'sale.order',
            'domain': domain,
            'target': 'current',
            'view_type': 'form',
            'view_mode': 'tree, form',
            'view_id': view.id
        }

    @api.multi
    @api.onchange('documents')
    def compute_document_count(self):
        for order in self:
            order.document_count = len(order.documents)

# endregion
