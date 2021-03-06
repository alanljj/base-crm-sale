# -*- coding: utf-8 -*-
# Author: Andrius Laukavičius. Copyright: JSC Boolit.
# See LICENSE file for full copyright and licensing details.

{
    'name': "SMTP Per User",
    'version': '1.3.0',
    'summary': 'Send letters from Odoo using your own mail',
    'category': 'Mail',
    'description': """Can configure different mail servers per user""",
    'author': 'Boolit',
    'license': 'LGPL-3',
    'website': "www.boolit.eu",
    "depends" : ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/smtp_per_user_view.xml',
    ],
    "installable": True
}
