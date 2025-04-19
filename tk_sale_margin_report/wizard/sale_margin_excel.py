# -*- coding: utf-8 -*-
from io import BytesIO
import base64
import xlwt
from odoo import fields, models
from odoo.exceptions import UserError


class SaleMarginWizard(models.TransientModel):
    """
    SaleMarginWizard is a transient model used to generate a sale margin report
    in Excel format.It allows users to specify a date range and other filters
    to create a report showing sales margins for orders within the specified criteria.
    """
    _name = 'sale.margin.wizard'
    _description = 'Sale Margin Wizard'

    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    customer_ids = fields.Many2many('res.partner', string='Customers')
    product_ids = fields.Many2many('product.product', string='Products')
    company_ids = fields.Many2many('res.company', string='Companies',
                                   default=lambda self: self.env.company)
    warehouse_ids = fields.Many2many('stock.warehouse', string='Warehouses')
    sale_team_ids = fields.Many2many('crm.team', string='Sale Teams')
    profit = fields.Boolean(string='Highlight Positive Margin')
    loss = fields.Boolean(string='Highlight Negative Margin')
    date_tooltip = fields.Char(default='Filter Records By Create Date')

    def btn_pdf_action(self):
        """
        Generates the sale margin report in PDF format based on the
        provided date range and filters.
        """
        self.ensure_one()
        if self.start_date > self.end_date:
            raise UserError(self.env._ ("Start Date Cannot be after End date"))
        data = {
            'form_data': self.read()[0],

        }
        return (self.env.ref('tk_sale_margin_report.action_sale_margin_pdf_report').report_action
                (self, data=data))

    def excel_sale_margin_report(self):
        """
        Generates the sale margin report in Excel format based on the
        provided date range and filters.
        """
        domain = [('create_date', '>=', self.start_date), ('create_date', '<=', self.end_date),
                  ('state', 'not in', ['draft', 'cancel'])]

        if self.customer_ids:
            domain.append(('partner_id', 'in', self.customer_ids.ids))
        if self.product_ids:
            domain.append(('order_line.product_id', 'in', self.product_ids.ids))
        if self.company_ids:
            domain.append(('company_id', 'in', self.company_ids.ids))
        if self.warehouse_ids:
            domain.append(('warehouse_id', 'in', self.warehouse_ids.ids))
        if self.sale_team_ids:
            domain.append(('team_id', 'in', self.sale_team_ids.ids))

        sale_order = self.env['sale.order'].search(domain, order='date_order ASC')

        workbook = xlwt.Workbook(encoding="UTF-8")
        sheet1 = workbook.add_sheet('Stock-Report-Card', cell_overwrite_ok=True)

        main_head = xlwt.easyxf('align: horiz center;borders: left thin, right thin, bottom thin;')
        font = xlwt.Font()
        font.bold = True
        font.height = 310
        main_head.font = font

        date_head = xlwt.easyxf(
            'align: horiz center; borders: top_color black, bottom_color black, right_color black,'
            ' left_color black, top thin, bottom thin,right thin, left thin;')

        heading_text = xlwt.easyxf(
            'font:bold True;pattern: pattern solid, fore_colour gray25;'
            'align: horiz center, vert center; borders: top_color black, bottom_color black, '
            'right_color black, left_color black, top thin, bottom thin,right thin, left thin;')

        data_text = xlwt.easyxf('align: horiz center;')

        profit_style = xlwt.easyxf(
            'font: color green; align: horiz center;')
        loss_style = xlwt.easyxf(
            'font: color red; align: horiz center;')

        for i in range(11):
            sheet1.col(i).width = 5000

        sheet1.write_merge(0, 1, 4, 6, 'Sale Margin Report', main_head)
        sheet1.write_merge(2, 2, 4, 6, f"{self.start_date} To {self.end_date}", date_head)

        headers = ['Sale Order', 'Product', 'Order Date', 'Customer', 'Warehouse',
                   'Sale Team', 'Cost', 'Price', 'Discount', 'Margin', 'Margin (%)']
        for col, header in enumerate(headers):
            row = 4
            sheet1.write_merge(row, row + 1, col, col, header, heading_text)

        row = 6
        for order in sale_order:
            order_line = order.order_line

            if self.product_ids:
                order_line = (order.order_line.filtered
                              (lambda line: line.product_id.id in self.product_ids.ids))

            for line in order_line:
                margin = line.price_unit - line.product_id.standard_price
                margin_price = round((margin / line.price_unit) * 100, 2)\
                    if line.price_unit else 0

                def write_row(sheet, row, order, line, margin, margin_price, row_style):
                    sheet.write(row, 0, order.name, row_style)
                    sheet.write(row, 1, line.product_id.name, row_style)
                    sheet.write(row, 2, order.date_order.strftime('%d-%m-%Y'), row_style)
                    sheet.write(row, 3, order.partner_id.name, row_style)
                    sheet.write(row, 4, order.warehouse_id.name, row_style)
                    sheet.write(row, 5, order.team_id.name, row_style)
                    sheet.write(row, 6, line.product_id.standard_price, row_style)
                    sheet.write(row, 7, line.price_unit, row_style)
                    sheet.write(row, 8, line.discount, row_style)
                    sheet.write(row, 9, margin, row_style)
                    sheet.write(row, 10, margin_price, row_style)

                if self.profit and margin > 0:
                    write_row(sheet1, row, order, line, margin, margin_price, profit_style)
                    row += 1
                elif self.loss and margin < 0:
                    write_row(sheet1, row, order, line, margin, margin_price, loss_style)
                    row += 1
                else:
                    write_row(sheet1, row, order, line, margin, margin_price, data_text)
                    row += 1

        stream = BytesIO()
        workbook.save(stream)
        filename = "Sale_Margin_Report" + ".xls"
        output = base64.encodebytes(stream.getvalue())
        attachment = self.env['ir.attachment'].sudo()

        attachment_id = attachment.create({
            'name': filename,
            'type': "binary",
            'public': False,
            'datas': output
        })
        if attachment_id:
            report = {
                'type': 'ir.actions.act_url',
                'url': f'/web/content/{attachment_id.id}?download=true',
                'target': 'self'
            }
            return report
