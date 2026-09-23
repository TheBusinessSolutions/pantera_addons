# -*- coding: utf-8 -*-
from odoo import models, fields

class ResCompany(models.Model):
    _inherit = 'res.company'
    
    pantera_stamp_image = fields.Binary(
        string="Invoice Stamp", 
        attachment=True,
        help="Upload the stamp image to be printed on the Pantera Invoice with Stamp."
    )