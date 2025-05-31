from . import models


def post_init_hook(cr, registry):
    """Add existing employee emails to validation queue."""
    from odoo.addons.kw_email_validation import post_init_hook as validation_hook
    validation_hook(cr, registry, 'hr.employee', 'work_email')

