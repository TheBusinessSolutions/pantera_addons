# -*- coding: utf-8 -*-
{
    'name': "Pantera Invoice",

    'summary': """ Pantera Invoice
       """,

    'description': """
       Pantera Invoice
    """,
    'author': " TheBusinessSolutions",

    'category': 'Uncategorized',

    # any module necessary for this one to work correctly
    'depends': ['base','account_invoice_refund_link','product','stock','sale','purchase','product_brand'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/product_data.xml',
        'views/company_res.xml',
        'reports/invoice_pantera_report.xml',
        'reports/pantera_packing_list_report.xml',
        'reports/pantera_invoice_with_stamp.xml',
    ],

    'assets': {
        'web.report_assets_common': [
            'pantera_invoice/static/src/css/rtl.css',

        ],
        'web.assets_backend': [
            'pantera_invoice/static/src/xml/*.xml',
        ]
    }
}
