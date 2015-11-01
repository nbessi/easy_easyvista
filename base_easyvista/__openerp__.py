# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Nicolas Bessi
#    Copyright 2015 Etat De Vaud SA
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
{'name': 'Easy vista',
 'version': '0.1',
 'author': 'Etat De Vaud',
 'maintainer': 'Etat De Vaud',
 'category': 'other',
 'complexity': 'easy',
 'depends': ['base', 'mail'],
 'description': """Sample addons of Open'Up and tech lunch""",
 'website': 'http://vd.ch',
 'data': [
     'view/incident_views.xml',
     'data/data.xml'
 ],
 'demo': ['data/demo.xml'],
 'test': [],
 'installable': True,
 'auto_install': False,
 'license': 'AGPL-3',
 'application': True,
 }
