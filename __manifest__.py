{
    'name': 'Warehouse Daily Dispatch Report',
    'version': '16.0.1.0.0', 
    'category': 'Inventory/Reporting',
    'summary': 'Secure SRO product delivery report for Blue Sky Coffee',
    'description': """
Warehouse Daily Dispatch Report
===============================
Developed by Faizal Emam (itdelhi.in).
This module is proprietary software. All rights reserved.
- Track SRO (Stock Return/Order) deliveries.
- Branch-wise reporting.
- Advanced costing logic (ir_property + product_template).
- Financial auditing via Pivot and Tree views.
    """,
    'author': 'Faizal Emam',
    'website': 'https://itdelhi.in', 
    'maintainer': 'Faizal Emam',
    'depends': ['stock', 'uom'],
    'data': [
        'security/ir.model.access.csv',
        'views/dispatch_report_views.xml',
    ],
    'images': ['static/description/banner.png'], 
    'installable': True,
    'auto_install': False,
    'application': True, 
    'license': 'OPL-1',  # Proprietary license to prevent unauthorized copying
    'price': 49.00,      # Optional: Currency in EUR agar aap ise Odoo Apps store par bechna chahen
    'currency': 'EUR',
}
