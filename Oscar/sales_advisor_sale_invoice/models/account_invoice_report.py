# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class AccountInvoiceReport(models.Model):
    _inherit = 'account.invoice.report'

    sales_advisor_id = fields.Many2one('res.partner', string='Asesor de Ventas', index=True)

    _depends = {'account.move': ['sales_advisor_id'],}

    def _select(self):
        return super()._select() + ", move.sales_advisor_id as sales_advisor_id"