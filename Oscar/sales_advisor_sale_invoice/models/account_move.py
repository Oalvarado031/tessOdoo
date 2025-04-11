# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, date
import logging

_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'account.move'

    sales_advisor_id = fields.Many2one('res.partner', string='Asesor de Ventas')