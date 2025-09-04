# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from datetime import date



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
    no_of_box_carton = fields.Integer(string="No. of Boxs/Cartons")

    def _prepare_stock_moves(self, picking):
        res = super(PurchaseOrderLine, self)._prepare_stock_moves(picking)
        res[0]['no_of_box_carton'] = self.no_of_box_carton
        return res

    def _prepare_account_move_line(self, move=False):
        res = super()._prepare_account_move_line(move=move)
        res['no_of_box_carton'] = self.no_of_box_carton
        return res



class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    pantera_product_variety_id = fields.Many2one('pantera.product.variety', string='Variety',related='product_id.pantera_product_variety_id',readonly=False)
    pantera_product_class_id = fields.Many2one('pantera.product.class', string='CL',related='product_id.pantera_product_class_id',readonly=False)
    pantera_product_size_id = fields.Many2one('pantera.product.size', string='Size',related='product_id.pantera_product_size_id',readonly=False)
    pantera_product_box_id = fields.Many2one('pantera.product.box', string='Box',related='product_id.pantera_product_box_id',readonly=False)
    pantera_product_brand_id = fields.Many2one('pantera.product.brand', string='Brand',related='product_id.pantera_product_brand_id',readonly=False)
    product_brand_id = fields.Many2one('product.brand', string='Brand',related='product_id.product_brand_id',readonly=False)
    no_of_box_carton = fields.Integer(string="No. of Boxs/Cartons")


    def _prepare_procurement_values(self, group_id=False):
        res = super()._prepare_procurement_values(group_id)
        res['no_of_box_carton'] = self.no_of_box_carton
        return res

    def _prepare_invoice_line(self, **optional_values):
        res = super()._prepare_invoice_line(**optional_values)

        res['no_of_box_carton'] = self.no_of_box_carton
        return res

class StockRuleInherit(models.Model):
    _inherit = 'stock.rule'

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, company_id,
                               values):
        move_values = super()._get_stock_move_values(product_id, product_qty, product_uom, location_id, name, origin,
                                                     company_id, values)
        if values.get('no_of_box_carton') and values.get('group_id'):
            move_values['no_of_box_carton'] = values['no_of_box_carton']

        return move_values

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    pantera_product_variety_id = fields.Many2one('pantera.product.variety', string='Variety',related='product_id.pantera_product_variety_id',readonly=False)
    pantera_product_class_id = fields.Many2one('pantera.product.class', string='CL',related='product_id.pantera_product_class_id',readonly=False)
    pantera_product_size_id = fields.Many2one('pantera.product.size', string='Size',related='product_id.pantera_product_size_id',readonly=False)
    pantera_product_box_id = fields.Many2one('pantera.product.box', string='Box',related='product_id.pantera_product_box_id',readonly=False)
    pantera_product_brand_id = fields.Many2one('pantera.product.brand', string='Brand',related='product_id.pantera_product_brand_id',readonly=False)
    product_brand_id = fields.Many2one('product.brand', string='Brand',related='product_id.product_brand_id',readonly=False)
    container_no = fields.Char(string='Container #')
    no_of_box_carton = fields.Integer(string="No. of Boxs/Cartons")

    @api.depends('product_id', 'move_id.payment_reference','pantera_product_variety_id','pantera_product_class_id','pantera_product_size_id','pantera_product_box_id','no_of_box_carton')
    def _compute_name(self):
        def get_name(line):
            product = line.product_id.with_context(
                lang=line.partner_id.lang) if line.partner_id.lang else line.product_id
            if not product:
                return False

            no_boxes = str(line.no_of_box_carton or '')
            product_name = product.name or ''
            class_name = line.pantera_product_class_id.name if line.pantera_product_class_id else ''
            variety_name = line.pantera_product_variety_id.name if line.pantera_product_variety_id else ''
            size_name = line.pantera_product_size_id.name if line.pantera_product_size_id else ''
            box_name = line.pantera_product_box_id.name if line.pantera_product_box_id else ''

            name_parts = [no_boxes, "BOX", product_name, class_name, variety_name, size_name, box_name]
            name = ' '.join(filter(None, name_parts))  # حذف القيم الفارغة
            print(name)

            return name or False

        term_by_move = (self.move_id.line_ids | self).filtered(lambda l: l.display_type == 'payment_term').sorted(
            lambda l: l.date_maturity or date.max).grouped('move_id')

        for line in self.filtered(lambda l: l.move_id.inalterable_hash is False):
            if line.display_type == 'payment_term':
                term_lines = term_by_move.get(line.move_id, self.env['account.move.line'])
                n_terms = len(line.move_id.invoice_payment_term_id.line_ids)
                name = line.move_id.payment_reference or False
                if n_terms > 1:
                    index = term_lines._ids.index(line.id) if line in term_lines else len(term_lines)
                    name = _('%s installment #%s', name if name else '', index + 1).lstrip()
                if n_terms > 1 or not line.name or line._origin.name == line._origin.move_id.payment_reference:
                    line.name = name

            if not line.product_id or line.display_type in ('line_section', 'line_note'):
                continue

            if not line.name or line._origin.name == get_name(line._origin):
                line.name = get_name(line)
            line.name = get_name(line)

class StockMove(models.Model):
    _inherit = 'stock.move'

    pantera_product_variety_id = fields.Many2one('pantera.product.variety', string='Variety',related='product_id.pantera_product_variety_id',readonly=False)
    pantera_product_class_id = fields.Many2one('pantera.product.class', string='CL',related='product_id.pantera_product_class_id',readonly=False)
    pantera_product_size_id = fields.Many2one('pantera.product.size', string='Size',related='product_id.pantera_product_size_id',readonly=False)
    pantera_product_box_id = fields.Many2one('pantera.product.box', string='Box',related='product_id.pantera_product_box_id',readonly=False)
    pantera_product_brand_id = fields.Many2one('pantera.product.brand', string='Brand',related='product_id.pantera_product_brand_id',readonly=False)
    product_brand_id = fields.Many2one('product.brand', string='Brand',related='product_id.product_brand_id',readonly=False)
    no_of_box_carton = fields.Integer(string="No. of Boxs/Cartons")


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

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super().action_confirm()

        return res
