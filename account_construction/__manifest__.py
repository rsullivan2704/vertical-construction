# -*- coding: utf-8 -*-
{
    'name': "Account Construction Module",
    'version': '10.0.0.0.0',
    'author': "Robert J Sullivan",
    'website': "http://www.keystonetileandstone.com",
    'license': 'AGPL-3',
    'category': 'Invoicing & Payments',
    'summary': """
This module modifies accounting views and models to
better serve the needs of a construction contracting company.
    """,
    'description': """
Construction contractors have specific needs with respect to information
related to the accounting of services and materials needed for projects.
    """,
    'version': '10.0.0.0.0',
    'application': False,

    # any module necessary for this one to work correctly
    'depends': ['account', 'document'],

    # any external dependencies for this one to work correctly
    'external_dependencies': {
        # 'python': ['pip']
    },

    # always loaded
    'data': [
        # 'data/purchase_construction_data.xml',
        # 'views/purchase_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
