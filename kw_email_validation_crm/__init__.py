from odoo.addons.kw_email_validation import post_init_hook as validation_hook

from . import models


def post_init_hook(cr, registry):
    """Add existing CRM lead emails to validation queue."""
    validation_hook(cr, registry, 'crm.lead', 'email_from')
