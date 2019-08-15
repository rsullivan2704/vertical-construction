# -*- coding: utf-8 -*-
{
    'name': "Base Construction Module",
    'version': '10.0.0.0.0',
    'author': "Robert J Sullivan",
    'website': "http://www.keystonetileandstone.com",
    'license': 'AGPL-3',
    'category': 'Technical Settings',
    'summary': """
This module modifies base models to better serve the
needs of a construction contracting company.
    """,
    'description': """

    """,
    'version': '10.0.0.0.0',
    'application': False,

    # any module necessary for this one to work correctly
    'depends': ['base', 'document'],

    # any external dependencies for this one to work correctly
    'external_dependencies': {
        # 'python': ['pip']
    },

    # always loaded
    'data': [
        # 'data/crm_construction_data.xml',
        'views/construction_document_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
