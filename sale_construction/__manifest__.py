# -*- coding: utf-8 -*-
{
    'name': "Sale Construction Module",
    'version': '10.0.0.0.0',
    'author': "Robert J Sullivan",
    'website': "http://www.keystonetileandstone.com",
    'license': 'AGPL-3',
    'category': 'Sales',
    'summary':"""
This module modifies sales views and models to better serve the needs of a construction contracting company.
    """,
    'description':"""
Construction contractors have specific needs with respect to information related to the sale of services and materials needed for projects.
    """,
    'version': '10.0.0.0.0',
    'application': False,

    # any module necessary for this one to work correctly
    # 'depends': ['report_wkhtmltopdf_param', 'website', 'web_notify'],
    'depends': ['sale'],

    # any external dependencies for this one to work correctly
    'external_dependencies': {
        # 'python': ['pip']
    },

    # always loaded
    'data': [
        'data/sale_construction_data.xml',
        'views/sale_views.xml',
        # 'data/mailpiece_rule_category_data.xml',
        # 'data/mailpiece_rule_data.xml',
        # 'data/paper_data.xml',
        # 'data/mailpiece_rule_category_data.xml',
        # 'data/mailpiece_rule_data.xml',
        # 'views/main_menu.xml',
        # 'views/paper_views.xml',
        # 'views/mailpiece_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
