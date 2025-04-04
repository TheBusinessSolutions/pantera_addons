# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Sales Commission to Internal Users and External Partners',
    'version' : '13.8.18',
    'price' : 99.0,
    'currency': 'EUR',
    'category': 'Sales/Sales',
    'license': 'Other proprietary',
    'description': """
Sales Commission by Sales/Invoice/Payment
Sales Commission to Internal Users and External Partners
sales Commission
sale_commission
sales_Commission
sale Commission
sales Commissions
helpdesk
sales order Commission
order Commission
sales person Commission
sales team Commission
sale team Commission
sale person Commission
team Commission
Commission
sales order on Commission
invoice on Commission
payment on Commission
Commission invoice
Commission vendor invoice
sales Commision
Commission sales user invoice
incentive
sales incentive
sales bonus
bonus
Sales Commission (form)
Sales Commission (form)
Sales Commission List (tree)
Sales Commission List (tree)
Sales Commission Search (search)
Sales Commission Search (search)
sales_commission_id (qweb)
sales_commission_worksheet_id (qweb)
This module provide feature to manage Sales Commission by Sales/Invoice/Payment to Internal Users and External Partners.
Sales Commission by Sales/Invoice/Payment

This module provide feature to manage sales commision by Sales/Invoice/Payments


This module allow company to manage sales commision with different options. You can configure after installing module what option/policy your company is following to give commissions to your sales users.
We are allowing you to select When to Pay and Calculation based on . Here you can define policy which will be used to give commission to your sales team.


For every Calcalulation based on we are allowing you to select:
1. Sales Manager Commission %
2. Sales Person Commission %

If you keep Sales Manager Commission 0% then system will not create sales commision lines and sales commision worksheet. System will work only with single option at time ie for example you can select When to Pay = Invoice confirm and calculation based on = Product category so system will run on that and create commission.

Please note that When to Pay = Customer payment is only supported with Calculation based on Sales Team. - Other options are supported in matrix. 
Workflow will be:
Option1 : Sales Confirmation -> Create Sales commission worksheet (if not created for current month) -> Add Sales commission lines on worksheet -> For every sales of current month, system will append sales commission lines on worksheet. -> End of month Accouant may review worksheet and create commision invoice to pay/release commision to sales person.
Option2 : Invoice Validate -> Create Sales commission worksheet (if not created for current month) -> Add Sales commission lines on worksheet -> For every invoice validation of current month, system will append sales commission lines on worksheet. -> End of month Accouant may review worksheet and create commision invoice to pay/release commision to sales person.
Option3 : Customer Payment -> Create Sales commission worksheet (if not created for current month) -> Add Sales commission lines on worksheet -> For every payment from customer of current month, system will append sales commission lines on worksheet. -> End of month Accouant may review worksheet and create commision invoice to pay/release commision to sales person.
Commission to sales person always will be in company currency. Multi currency is supported for this module so sales order/ invoice / payment can be in different currency but system will take care for it and create commission lines in company currency.
Sales Commission product is created using data and you still can change commission product on commission worksheet to create commission invoice.

Menus
---- Invoicing/Commissions
---- ---- Invoicing/Commissions/Commission Worksheets
---- ---- Invoicing/Commissions/Sales Commissions Lines
---- Sales/Commissions
---- ---- Sales/Commissions/Commission Worksheets
---- ---- Sales/Commissions/Sales Commissions Lines

Configuration for Sales Commission

Commission to sales person always will be in company currency. Multi currency is supported for this module so sales order/ invoice / payment can be in different currency but system will take care for it and create commission lines in company currency.
Sales Commission product is created using data and you still can change commission product on commission worksheet to create commission invoice.
Commission amount will be based on Net Revenue Model where it consider amounts without taxes. (This module does not support Gross Margin Model)

            """,
    'summary' : 'This module provide feature to manage Sales Commission by Sales/Invoice/Payment to Internal Users and External Partners.',
    'author' : 'Probuse Consulting Service Pvt. Ltd.',
    'website' : 'wwww.probuse.com',
    'depends' : ['account','sale_management'],
    'support': 'contact@probuse.com',
    'live_test_url':  'https://probuseappdemo.com/probuse_apps/sales_commission_external_user/119',#'https://youtu.be/Gm-n5QBWSEw', #'https://youtu.be/M5dK7tUWd6c',
    'images': ['static/description/image.jpg'],
    'data' : [
            'security/ir.model.access.csv',
              'security/sales_commission_security.xml',
              'data/commission_sequence.xml',
              'data/product_data.xml',
              'data/sales_commission_level.xml',    
              'view/sale_config_settings_views.xml',
              'view/crm_team_view.xml',
              'view/product_template_view.xml',
#               'view/product_view.xml',
              'view/product_category_view.xml',
              'view/sales_commission_view.xml',
              'view/account_invoice_view.xml',
              'view/report_sales_commission.xml',
              'view/report_sales_commission_worksheet.xml',
              'view/account_payment.xml',
              'view/sale_view.xml',
              'view/sale_commission_level.xml',
              'view/partner_view.xml',
              'wizard/account_payment_register_view.xml',
              ],
    'installable' : True,
    'application' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
