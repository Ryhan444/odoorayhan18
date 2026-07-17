import logging
from os import utime
from os.path import getmtime
from time import time

from odoo import models, fields, api, http, _
from odoo.http import SessionExpiredException

_logger = logging.getLogger(__name__)


class ResUsers(models.Model):
    _inherit = "res.users"
    
    pos_hide_refund = fields.Boolean(
        string="Hide Refund Button",
        default=False,
        help="Hide Refund Button in POS"
    )
    pos_hide_general_note = fields.Boolean(
        string="Hide General Note",
        default=False,
        help="Hide General Note in POS"
    )
    pos_hide_customer_note = fields.Boolean(
        string="Hide Customer Note",
        default=False,
        help="Hide Custom Note in POS"
    )
    pos_hide_pricelist = fields.Boolean(
        string="Hide Pricelist Button",
        default=False,
        help="Hide Pricelist Button in POS"
    )
    pos_hide_cancel_order = fields.Boolean(
        string="Hide Cancel Order Button",
        default=False,
        help="Hide Cancel Order Button in POS"
    )
    pos_hide_quotations_order = fields.Boolean(
        string="Hide Quotations Order Button",
        default=False,
        help="Hide Quotations Order Button in POS"
    )
    pos_hide_actions = fields.Boolean(
        string="Hide Actions Button",
        default=False,
        help="Hide Actions Button in POS"
    )
    pos_hide_info = fields.Boolean(
        string="Hide Info Button",
        default=False,
        help="Hide Info Button in POS"
    )
    pos_hide_enter_code = fields.Boolean(
        string="Hide Enter Code Button",
        default=False,
        help="Hide Enter Code Button in POS"
    )
    pos_hide_reward = fields.Boolean(
        string="Hide Reward Button",
        default=False,
        help="Hide Reward Button in POS"
    )
    pos_hide_reset_program = fields.Boolean(
        string="Hide Reset Program Button",
        default=False,
        help="Hide Reset Program Button in POS"
    )

