from odoo.addons.kw_email_validation import post_init_hook as validation_hook

from . import models


def post_init_hook(cr, registry):
    """Add existing partner emails to validation queue."""
    validation_hook(cr, registry, 'res.partner', 'email')
