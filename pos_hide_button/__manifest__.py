# -*- coding: utf-8 -*-
{
    'name': "Hide Button Actions or Hide Components Button Actions in Point of Sale(POS)",

    'summary': """can hide button in pos from setup users""",

    'description': """
        hide button in pos from setup users
    """,

    'author': "ARA SOFT",
    'website': "",
    "images": ["static/description/icon.png"],
    'category': 'Point of Sale',
    "version": "18.0.0.0.0",

    'depends': [
        'point_of_sale',
    ],

    'data': [
        'views/res_users_view.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos':[
            'pos_hide_button/static/src/xml/controlbutton.xml',
            'pos_hide_button/static/src/js/models.js'
        ]
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'demo': [],
    'price': 13.50,
    'currency': 'USD',
    'license': 'OPL-1',
}
