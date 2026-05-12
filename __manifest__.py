{
    'name': 'Warehouse Daily Dispatch Report',
    'version': '16.0.1.0.0', 
    'category': 'Inventory/Reporting',
    'summary': 'Validated SRO product delivery report with Branch and Date for Blue Sky Coffee',
    'description': """
Warehouse Daily Dispatch Report
===============================
This module provides a comprehensive reporting tool for warehouse dispatches.
- Track SRO (Stock Return/Order) deliveries.
- Branch-wise reporting.
- Product cost and total valuation for Finance.
- Pivot and Tree views for daily analysis.
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
    'license': 'LGPL-3',
}