{
    'name': "Container_ctl_mod",

    'summary': """
        Starting module for "Discover the JS framework, chapter 2: Build a dashboard"
    """,
    'website': "https://www.odoo.com/",


    'description': """
            This module for controlling containers.
            """,
    'author': '@ja developer',
    'category': 'Services',
    'version': '0.1',
    'application': True,
    'installable': True,
    'depends': ['base', 'web'],

    'data': [
        'security/ir.model.access.csv',
        'views/shipping_views.xml',
        'views/menu_views.xml',
    ],
    'license': 'LGPL-3'
}