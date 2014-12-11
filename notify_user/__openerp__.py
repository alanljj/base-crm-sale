# -*- encoding: utf-8 -*-
##############################################################################
#    
#    Odoo, Open Source Management Solution
#
#    Author: Andrius Laukavičius. Copyright: JSC NOD Baltic
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

{
    'name': 'CRM Salesman Notify',
    'version': '1.0',
    'depends': ['crm_helpdesk', 'project'],
    'author': 'OERP',
    'description': """
Modifies notification when user is set responsible in a way that only
that user will be notified excluding other followers.

    """,
    'website': 'http://www.oerp.eu',
    'category': 'notify',
    'demo': [],
    'test': [],
    'data': [
      'data/mail_message_subtype_data.xml'
    ],
    'auto_install': False,
    'installable': True,
}
