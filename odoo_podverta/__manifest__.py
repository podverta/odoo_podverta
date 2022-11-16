# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Odoo_podverta',
    'version': '1.0',
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'report/sale_order_report_inherit.xml',
        'views/podverta_view.xml',
        'views/podverta_type.xml',
        'views/podverta_menu.xml',
    ],
    'author': 'Podverta',
    'depends': ['sale'],
    'application': True,
    'description': "add fields on sale_order model",
}
