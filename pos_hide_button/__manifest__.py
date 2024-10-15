# -*- coding: utf-8 -*-
{
    'name': "POS Hide Button",

    'summary': """can hide button in pos from setup users""",

    'description': """
        ide button in pos from setup users
    """,

    'author': "Achmad Rayhan Alief",
    'website': "",

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

    'demo': [],
}
