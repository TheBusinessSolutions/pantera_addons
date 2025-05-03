# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductVariety(models.Model):
    _name = 'pantera.product.variety'

    name = fields.Char()


class ProductClass(models.Model):
    _name = 'pantera.product.class'

    name = fields.Char()


class ProductSize(models.Model):
    _name = 'pantera.product.size'

    name = fields.Char()


class ProductBox(models.Model):
    _name = 'pantera.product.box'

    name = fields.Char()


class ProductBrand(models.Model):
    _name = 'pantera.product.brand'

    name = fields.Char()


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    pantera_product_variety_id = fields.Many2one('pantera.product.variety',string='Variety')
    pantera_product_class_id = fields.Many2one('pantera.product.class',string='CL')
    pantera_product_size_id = fields.Many2one('pantera.product.size',string='Size')
    pantera_product_box_id = fields.Many2one('pantera.product.box',string='Box')
    pantera_product_brand_id = fields.Many2one('pantera.product.brand',string='Brand')



class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    pantera_product_variety_id = fields.Many2one('pantera.product.variety', string='Variety',related='product_id.pantera_product_variety_id',readonly=False)
    pantera_product_class_id = fields.Many2one('pantera.product.class', string='CL',related='product_id.pantera_product_class_id',readonly=False)
    pantera_product_size_id = fields.Many2one('pantera.product.size', string='Size',related='product_id.pantera_product_size_id',readonly=False)
    pantera_product_box_id = fields.Many2one('pantera.product.box', string='Box',related='product_id.pantera_product_box_id',readonly=False)
    pantera_product_brand_id = fields.Many2one('pantera.product.brand', string='Brand',related='product_id.pantera_product_brand_id',readonly=False)
    product_brand_id = fields.Many2one('product.brand', string='Brand',related='product_id.product_brand_id',readonly=False)




class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    pantera_product_variety_id = fields.Many2one('pantera.product.variety', string='Variety',related='product_id.pantera_product_variety_id',readonly=False)
    pantera_product_class_id = fields.Many2one('pantera.product.class', string='CL',related='product_id.pantera_product_class_id',readonly=False)
    pantera_product_size_id = fields.Many2one('pantera.product.size', string='Size',related='product_id.pantera_product_size_id',readonly=False)
    pantera_product_box_id = fields.Many2one('pantera.product.box', string='Box',related='product_id.pantera_product_box_id',readonly=False)
    pantera_product_brand_id = fields.Many2one('pantera.product.brand', string='Brand',related='product_id.pantera_product_brand_id',readonly=False)
    product_brand_id = fields.Many2one('product.brand', string='Brand',related='product_id.product_brand_id',readonly=False)


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    pantera_product_variety_id = fields.Many2one('pantera.product.variety', string='Variety',related='product_id.pantera_product_variety_id',readonly=False)
    pantera_product_class_id = fields.Many2one('pantera.product.class', string='CL',related='product_id.pantera_product_class_id',readonly=False)
    pantera_product_size_id = fields.Many2one('pantera.product.size', string='Size',related='product_id.pantera_product_size_id',readonly=False)
    pantera_product_box_id = fields.Many2one('pantera.product.box', string='Box',related='product_id.pantera_product_box_id',readonly=False)
    pantera_product_brand_id = fields.Many2one('pantera.product.brand', string='Brand',related='product_id.pantera_product_brand_id',readonly=False)
    product_brand_id = fields.Many2one('product.brand', string='Brand',related='product_id.product_brand_id',readonly=False)
    container_no = fields.Char(string='Container #')

class StockMove(models.Model):
    _inherit = 'stock.move'

    pantera_product_variety_id = fields.Many2one('pantera.product.variety', string='Variety',related='product_id.pantera_product_variety_id',readonly=False)
    pantera_product_class_id = fields.Many2one('pantera.product.class', string='CL',related='product_id.pantera_product_class_id',readonly=False)
    pantera_product_size_id = fields.Many2one('pantera.product.size', string='Size',related='product_id.pantera_product_size_id',readonly=False)
    pantera_product_box_id = fields.Many2one('pantera.product.box', string='Box',related='product_id.pantera_product_box_id',readonly=False)
    pantera_product_brand_id = fields.Many2one('pantera.product.brand', string='Brand',related='product_id.pantera_product_brand_id',readonly=False)
    product_brand_id = fields.Many2one('product.brand', string='Brand',related='product_id.product_brand_id',readonly=False)



class AccountMove(models.Model):
    _inherit = 'account.move'

    vessel = fields.Char(string='Vessel')
    pol = fields.Char(string='POL')
    pod = fields.Char(string='POD')
    date_log_no = fields.Char(string='Data Log No.')
    bl_number = fields.Char(string='BL Number')


    temp_on_loading = fields.Float(string='Temp on Loading')
    temp_on_arrival = fields.Float(string='Temp on Arrival')

    etd_date = fields.Date(string='ETD')
    eta_date = fields.Date(string='ETA')

    exporter_id = fields.Many2one('res.partner')
    seller_id = fields.Many2one('res.partner')

    def print_pantera_inv(self):
        return self.env.ref('pantera_invoice.action_report_inv_pantera').report_action(self)

