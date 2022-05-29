# -*- coding: utf-8 -*-
{
    'name': "Advanced Pdf Layout",

    'version': '15.0.1.0.0',
    'summary': "Invoice format",
    'description': "Customised invoice,quotation,purchase order formats",
    'category': 'Invoicing',
    'author': 'Advanced Solutions',
    'website': 'http://www.advanced.qa',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'sale', 'sale_management'],

    # always loaded
    'data': [
        'views/res_company.xml',
        'report/invoice_layout.xml',
        'report/invoice_second_layout.xml',
        'report/quotation.xml',
        'report/report.xml',
    ],

}
