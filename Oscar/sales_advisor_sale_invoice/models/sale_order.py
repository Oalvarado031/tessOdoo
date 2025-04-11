# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, date
import logging

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sales_advisor_id = fields.Many2one('res.partner', string='Asesor de Ventas')

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['sales_advisor_id'] = self.sales_advisor_id.id
        return invoice_vals
