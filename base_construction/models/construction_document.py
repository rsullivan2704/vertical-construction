from odoo import fields, models, _


class ConstructionDocument(models.Model):
    _inherit = ['ir.attachment']
    _name = 'base_construction.construction.document'

    content_type = fields.Selection(
        string=u'Content Type',
        selection=[
            ('drawing', 'Drawing'),
            ('spec', 'Spec'),
            ('other', 'Other')],
        oldname="document_type"
    )
