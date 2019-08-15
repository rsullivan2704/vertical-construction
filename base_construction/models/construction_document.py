from odoo import fields, models, _


class ConstructionDocument(models.Model):
    _inherit = ['ir.attachment']
    _name = 'base.construction.document'

    document_type = fields.Selection(
        string=u'Document type',
        selection=[
            ('drawing', 'Drawing'),
            ('spec', 'Spec'),
            ('other', 'Other')]
    )
