# -*- coding: utf-8 -*-
{
    'name': "Laffan Report",

    'summary': """
     Report Customization""",

    'description': """
        Customisation in quotation report
    """,

    'author': "Advanced Solutions",
    'website': "http://www.advanced.qa",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.9',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'project'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/res_company.xml',
        'report/report_quotation.xml',
        'report/invoice_layout.xml',
        'report/report.xml',
    ],
}
