from odoo import api, fields, models


class HrAttendance(models.Model):
    _name = 'hr.attendance'
    _inherit = 'hr.attendance'

    lat_check_in = fields.Float(string="Latitude Check In")
    long_check_in = fields.Float(string="Longitude Check In")
    lat_check_out = fields.Float(string="Latitude Check Out")
    long_check_out = fields.Float(string="Longitude Check Out")
    image_check_in = fields.Binary(string="Image Check In")
    image_check_out = fields.Binary(string="Image Check Out")