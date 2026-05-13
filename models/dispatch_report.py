# -*- coding: utf-8 -*-
# Part of ITDELHI.IN. See LICENSE file for full copyright and licensing details.
# Copyright (C) 2026 Faizal Emam (<https://itdelhi.in>)
from odoo import models, fields, tools

class WarehouseDispatchReport(models.Model):
    _name = 'warehouse.dispatch.report'
    _description = 'Warehouse Dispatch Detailed Report'
    _auto = False
    _order = 'date_done desc'

    product_name = fields.Char(string='Product Name', readonly=True)
    qty = fields.Float(string='Qty', readonly=True)
    cost = fields.Float(string='Unit Cost', readonly=True)
    total_cost = fields.Float(string='Total Cost', readonly=True)
    unit = fields.Char(string='Unit', readonly=True)
    branch_name = fields.Char(string='Branch Name', readonly=True)
    date_done = fields.Datetime(string='Shipping Date & Time', readonly=True)
    sro_number = fields.Char(string='SRO Number', readonly=True)

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW warehouse_dispatch_report AS (
                SELECT
                    sm.id AS id,
                    CASE
                        WHEN pp.default_code IS NOT NULL AND pp.default_code != ''
                            THEN '[' || pp.default_code || '] ' ||
                                 COALESCE(pt.name->>'en_US', pt.name->>'en', '')
                        ELSE COALESCE(pt.name->>'en_US', pt.name->>'en', '')
                    END AS product_name,
                    sm.quantity_done AS qty,
                    COALESCE(ip_cost.value_float, 0.0) AS cost,
                    (sm.quantity_done * COALESCE(ip_cost.value_float, 0.0)) AS total_cost,
                    COALESCE(uu.name->>'en_US', uu.name->>'en', 'Units') AS unit,
                    COALESCE(sw.name, 'Main Warehouse') AS branch_name,
                    sp.date_done AS date_done,
                    sp.origin AS sro_number
                FROM stock_move sm
                JOIN stock_picking sp ON sm.picking_id = sp.id
                JOIN product_product pp ON sm.product_id = pp.id
                JOIN product_template pt ON pp.product_tmpl_id = pt.id
                LEFT JOIN uom_uom uu ON sm.product_uom = uu.id
                JOIN stock_picking_type spt ON sp.picking_type_id = spt.id
                LEFT JOIN stock_warehouse sw ON spt.warehouse_id = sw.id
                LEFT JOIN LATERAL (
                    SELECT ip.value_float FROM ir_property ip
                    WHERE ip.name = 'standard_price'
                      AND ip.res_id = 'product.product,' || pp.id::varchar
                    ORDER BY ip.id DESC
                    LIMIT 1
                ) ip_cost ON TRUE
                WHERE sp.state = 'done'
                  AND sm.quantity_done > 0
                  AND spt.code = 'internal'
                  AND sp.origin LIKE 'SRO/%'
                  AND sp.date_done >= date_trunc('month', CURRENT_DATE)
            )
        """)
