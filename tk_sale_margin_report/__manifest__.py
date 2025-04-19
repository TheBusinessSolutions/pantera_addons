# -*- coding: utf-8 -*-
{
    'name': 'Sales Margin Report - PDF, XLS',
    'description': """
              Sales Margin Report - PDF, XLS
    """,
    'summary': 'Sale Margin Report',
    'version': '1.0',
    'category': 'Inventory',
    'author': 'TechKhedut Inc.',
    'company': 'TechKhedut Inc.',
    'maintainer': 'TechKhedut Inc.',
    'website': "https://www.techkhedut.com",
    'depends': [
        'stock', 'sale_management',
    ],
    'data': [
        #  security
        'security/ir.model.access.csv',
        # data
        'data/paper_format_view.xml',
        # report
        'report/sale_margin_pdf_view.xml',
        # wizard
        'wizard/sale_margin_excel_view.xml',
        #  views
        'views/menus.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
