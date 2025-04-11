# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class SaleReport(models.Model):
    _inherit = 'sale.report'

    sales_advisor_id = fields.Many2one('res.partner', string='Asesor de Ventas', readonly=True)

    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res['sales_advisor_id'] = "s.sales_advisor_id"
        return res
    
    def _group_by_sale(self):
        res = super()._group_by_sale()
        res += """,
                s.sales_advisor_id"""
        return res
