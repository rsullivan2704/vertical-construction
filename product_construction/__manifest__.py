# -*- coding: utf-8 -*-
{
    'name': "Product Construction Module",
    'version': '10.0.0.0.0',
    'author': "Robert J Sullivan",
    'website': "http://www.keystonetileandstone.com",
    'license': 'AGPL-3',
    'category': 'Sales',
    'summary': """
This module modifies product views and models to better serve the
needs of a construction contracting company.
    """,
    'description': """
Construction contractors have specific needs with respect to
information related to their products and services.
    """,
    'version': '10.0.0.0.0',
    'application': False,

    # any module necessary for this one to work correctly
    'depends': ['product', 'document'],

    # any external dependencies for this one to work correctly
    'external_dependencies': {
        # 'python': ['pip']
    },

    # always loaded
    'data': [
        'data/product_construction_data.xml',
        # 'views/crm_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
