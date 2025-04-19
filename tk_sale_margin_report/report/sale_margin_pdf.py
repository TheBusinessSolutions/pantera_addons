# -*- coding: utf-8 -*-
from odoo import models, api


class SaleMarginReport(models.AbstractModel):
    """
    This class is responsible for generating the sale margin report in PDF format.
    It uses a template to render the report and includes data such as sales margins,
    product details, and other relevant financial information for sales analysis.
    """
    _name = 'report.tk_sale_margin_report.sale_pdf_report_template'
    _description = 'Sale Margin Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        form_data = data.get('form_data')
        start_date = form_data.get('start_date')
        end_date = form_data.get('end_date')

        domain = [('create_date', '>=', start_date), ('create_date', '<=', end_date),
                  ('state', 'not in', ['draft', 'cancel'])]

        if form_data.get('customer_ids'):
            domain.append(('partner_id', 'in', form_data['customer_ids']))
        if form_data.get('product_ids'):
            domain.append(('order_line.product_id', 'in', form_data['product_ids']))
        if form_data.get('company_ids'):
            domain.append(('company_id', 'in', form_data['company_ids']))
        if form_data.get('warehouse_ids'):
            domain.append(('warehouse_id', 'in', form_data['warehouse_ids']))
        if form_data.get('sale_team_ids'):
            domain.append(('team_id', 'in', form_data['sale_team_ids']))

        sale_order = self.env['sale.order'].search(domain, order='date_order ASC')
        report_data = []

        for order in sale_order:
            order_line = order.order_line

            if form_data.get('product_ids'):
                product_ids = form_data.get('product_ids')
                order_line = (order.order_line.filtered
                              (lambda line: line.product_id.id in product_ids))

            for line in order_line:
                margin = line.price_unit - line.product_id.standard_price
                margin_price = round((margin / line.price_unit) * 100, 2)\
                    if line.price_unit else 0
                color = ''

                if form_data.get('loss') and margin < 0:
                    color = 'red'
                elif form_data.get('profit') and margin > 0:
                    color = 'green'

                report_data.append({
                    'order': order.name,
                    'product': line.product_id.name,
                    'order_date': order.date_order.strftime('%d-%m-%Y'),
                    'customer': order.partner_id.name,
                    'warehouse': order.warehouse_id.name,
                    'sale_team': order.team_id.name,
                    'cost': line.product_id.standard_price,
                    'price': line.price_unit,
                    'discount': line.discount,
                    'margin': margin,
                    'margin_percentage': margin_price,
                    'color': color
                })

        return {
            'docs': report_data,
            'from_date': start_date,
            'to_date': end_date,
        }
