# Copyright 2025 Kitworks Systems
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

from . import models


def post_init_hook(cr, registry, model_name, email_field):
    """Post init hook for adding existing emails to validation queue.
    
    Args:
        cr: Database cursor
        registry: Odoo registry
        model_name: Model name to process (e.g. 'res.partner')
        email_field: Field name containing email (e.g. 'email')
    """
    from odoo import api, SUPERUSER_ID
    
    env = api.Environment(cr, SUPERUSER_ID, {})
    model = env[model_name]
    validation_model = env['kw.email.validation']
    
    # Get all records with non-empty email field
    domain = [(email_field, '!=', False), (email_field, '!=', '')]
    records = model.search(domain)
    
    # Process emails in batches to avoid memory issues
    batch_size = 1000
    total_records = len(records)
    
    for i in range(0, total_records, batch_size):
        batch = records[i:i+batch_size]
        for record in batch:
            email = getattr(record, email_field, False)
            if email:
                # Add email to validation queue
                validation = validation_model.get_validation(email)
                if validation:
                    record.kw_email_validation_id = validation.id
        
        # Commit transaction after each batch
        cr.commit()
