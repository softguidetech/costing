# -*- coding: utf-8 -*-


{
    'name': 'Manufacturing Process Costing SGT',
    'version': '16.0.1.0.0',
    'category': 'Manufacturing',
    'summary': 'This plugin helps to show process costing on Manufacturing Order based on BOM',
    'description': """
                   """,
    'price': 85.00,
    'currency': "EUR",
    'author': 'SGT',
    'category': 'Manufacturing',
    'website': "http://www.softguidetech.com",
    'depends': ['sale_management', 'mrp'],
    'data': [
        'security/ir.model.access.csv',
        'views/custom_bom_view.xml',
        'views/config.xml',
        'views/menu_inheritance.xml',
        'report/mrp_costing_report.xml',
        'report/mrp_bom_report_view.xml',
        'report/mrp_production_report_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    "images": ['static/description/icon.png'],
}
