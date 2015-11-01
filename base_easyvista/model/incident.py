# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Nicolas Bessi
#    Copyright 2015 Etat de Vaud
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
import random
from datetime import datetime, timedelta
from openerp import models, fields, api


class Incident(models.Model):
    """Incident base class"""
    _rec_name = 'number'
    _name = 'easy_incident'

    _inherit = ['mail.thread', 'ir.needaction_mixin']

    @api.multi
    def _track_subtype(self,  init_values):
        if 'stage_id' in init_values:
            return 'base_easyvista.easy_incident_changes'
        return super(Incident, self)._track_subtype(init_values)

    @api.model
    def create(self, vals):
        if not vals.get('execution_date'):
            now = datetime.now()
            execution = now + timedelta(days=random.randint(1, 90))
            end = execution + timedelta(days=random.randint(1, 90))
            vals.update(
                {
                    'execution_date': fields.Datetime.to_string(execution),
                    'end_date': fields.Datetime.to_string(end),
                }
            )
        return super(Incident, self).create(vals)

    @api.model
    def _get_default_execution_days(self):
        return random.randint(1, 50)

    @api.model
    def _get_default_number(self):
        return self.env['ir.sequence'].next_by_code('incident')

    @api.model
    def _get_default_stage_id(self):
        """ Gives default stage_id """
        return self.env.ref('base_easyvista.st1').id

    name = fields.Char(
        required=True,
        help="Title of incident"
    )
    number = fields.Integer(
        default=_get_default_number,
    )

    beneficiary_id = fields.Many2one(
        string='Beneficiary',
        comodel_name='res.users',
        required=True,
        help="People who will beneficiate of prestation"
    )

    execution_date = fields.Datetime(
        string="Execution date",
        help='Date of work start'
    )

    end_date = fields.Datetime(
        string="End date",
        help='Effective end date',
    )

    resource_id = fields.Many2one(
        string='Executant',
        comodel_name='res.users',
        required=False,
        help='People how does the job'
    )

    entity = fields.Char(
        string="Entity",
        related='beneficiary_id.entity_id.name',
        readonly=True,
    )

    description = fields.Html(
        string='Commentaire',
        help='Please enter as many details as possible'
    )

    material_ids = fields.Many2many(
        string='Materials',
        comodel_name='easy_material',
    )

    ci_id = fields.Many2one(
        string='CI',
        comodel_name='easy_ci',
    )

    stage_id = fields.Many2one(
        string='state',
        comodel_name='easy_stage',
        default=_get_default_stage_id,
        track_visibility='onchange',
    )

    execution_days = fields.Integer(
        default=_get_default_execution_days,
        String="Execution days",
    )

    @api.one
    def populate_incident(self):
        cis = self.env['easy_ci'].search([])
        users = self.env['res.users'].search([])
        stages = self.env['easy_stage'].search([])
        description = """
Lorem ipsum dolor sit amet, elit vitae, ornare enim mauris
vulputate sagittis ultricies ridiculus, lectus vestibulum,
enim bibendum. Eget nec. Curabitur nullam platea, tellus egestas ut nec ipsum.
 Pede tempus integer sit varius non, pellentesque nisl eget sed porta sed,
 at fringilla auctor duis vivamus ullamcorper. Ut duis mauris
sollicitudin quam, montes neque, mattis adipiscing feugiat ante.
 Sed nibh et a id, turpis mi odio, integer orci vivamus.
In quisque in, elit sollicitudin.
Eu ac urna lectus amet, sodales elementum nunc ut.
        """
        for len in xrange(1000):
            self.create(
                {
                    'name': "Generated {}".format(len),
                    'beneficiary_id': random.choice(users).id,
                    'resource_id': random.choice(users).id,
                    'ci_id': random.choice(cis).id,
                    'description': description,
                    'stage_id': random.choice(stages).id
                }
            )


class EasyStage(models.Model):
    _name = 'easy_stage'

    name = fields.Char()
