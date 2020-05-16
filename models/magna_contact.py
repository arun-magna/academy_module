
from odoo import models, fields

class MagnaContact(models.Model):
    _inherit = "res.partner"

    twitter_handle = fields.Char(string='Twitter Handle')
    subtitle = fields.Char(string='Sub Title')