# -*- coding: utf-8 -*-
import datetime
from odoo.tests.common import TransactionCase, tagged


@tagged('custom_tags')
class TestWizard(TransactionCase):
    """
    Test case for validating sale margin report wizard functionality.
    It tests the creation and functionality of a sale margin wizard,
    including generating PDF and Excel reports.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment, including the creation of required records
        like partners, products, sale orders, and the sale margin wizard.
        """
        super().setUpClass()

        cls.partner_one = cls.env['res.partner'].create({
            'name': 'Customer 2'
        })
        cls.product_one = cls.env['product.product'].create({
            'name': 'product 2',
            'list_price': 300,
            'standard_price': 200,
            'default_code': 'P-COM[2]'
        })
        cls.company_one = cls.env['res.company'].create({
            'name': 'Company 2'
        })
        cls.warehouse_location = cls.env['stock.location'].create({
            'name': 'Warehouse 2',
            'company_id': cls.company_one.id,
        })
        cls.warehouse_one = cls.env['stock.warehouse'].create({
            'name': 'Warehouse 2',
            'code': 'WH2',
            'company_id': cls.company_one.id,
            'view_location_id': cls.warehouse_location.id,
        })
        cls.sale_team_one = cls.env['crm.team'].create({
            'name': 'Team 2',
            'company_id': cls.company_one.id
        })
        cls.sale_order = cls.env['sale.order'].create({
            'partner_id': cls.partner_one.id,
            'company_id': cls.company_one.id,
            'warehouse_id': cls.warehouse_one.id,
            'team_id': cls.sale_team_one.id,
            'date_order': datetime.datetime.today(),
            'order_line': [(0, 0, {
                'product_id': cls.product_one.id,
                'product_uom_qty': 5,
                'price_unit': 300
            })]
        })
        cls.sale_wizard = cls.env['sale.margin.wizard'].create({
            'start_date': datetime.datetime.today(),
            'end_date': datetime.datetime.strptime('2025-03-26', "%Y-%m-%d").date(),
            'customer_ids': [(6, 0, [cls.partner_one.id])],
            'product_ids': [(6, 0, [cls.product_one.id])],
            'company_ids': [(6, 0, [cls.company_one.id])],
            'warehouse_ids': [(6, 0, [cls.warehouse_one.id])],
            'sale_team_ids': [(6, 0, [cls.sale_team_one.id])],
            'profit': True,
            'loss': False
        })

    def test_sale_margin_wizard(self):
        """
        Test the sale margin wizard functionality by validating the form data
        for the PDF action.
        """
        self.assertTrue(self.sale_wizard)
        action = self.sale_wizard.btn_pdf_action()
        self.assertIsInstance(action, dict)
        form_data = action.get('data', {}).get('form_data', {})
        self.assertEqual(form_data['start_date'], self.sale_wizard.start_date)
        self.assertEqual(form_data['end_date'], self.sale_wizard.end_date)
        self.assertEqual(form_data['customer_ids'], [self.partner_one.id])
        self.assertEqual(form_data['product_ids'], [self.product_one.id])
        self.assertEqual(form_data['company_ids'], [self.company_one.id])
        self.assertEqual(form_data['warehouse_ids'], [self.warehouse_one.id])
        self.assertEqual(form_data['sale_team_ids'], [self.sale_team_one.id])
        self.assertTrue(form_data['profit'])
        self.assertFalse(form_data['loss'])

    def test_excel_sale_margin_report(self):
        """
        Test generating the Excel report for the sale margin wizard.
        """
        method_excel = self.sale_wizard.excel_sale_margin_report()
        self.assertEqual(method_excel.get('type'), 'ir.actions.act_url')
        extract_url = method_excel.get('url')
        self.assertTrue(extract_url.startswith('/web/content'))

    def test_pdf_sale_margin_report(self):
        """
        Test generating the PDF report for the sale margin wizard.
        """
        form_data = {
            'start_date': self.sale_wizard.start_date,
            'end_date': self.sale_wizard.end_date,
            'customer_ids': [self.partner_one.id],
            'product_ids': [self.product_one.id],
            'company_ids': [self.company_one.id],
            'warehouse_ids': [self.warehouse_one.id],
            'sale_team_ids': [self.sale_team_one.id],
            'profit': True,
            'loss': False
        }
        action = self.sale_wizard.btn_pdf_action()
        self.assertIsInstance(action, dict)
        report_data = action.get('data', {}).get('form_data', {})
        keys_to_remove = ['create_date', 'create_uid', 'write_date',
                          'write_uid', 'display_name', 'date_tooltip', 'id']
        for key in keys_to_remove:
            report_data.pop(key, None)
        self.assertEqual(report_data, form_data)
