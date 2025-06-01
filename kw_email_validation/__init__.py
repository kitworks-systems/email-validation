from . import models


def post_init_hook(cr, registry, model_name, email_field):
    from odoo import api, SUPERUSER_ID

    env = api.Environment(cr, SUPERUSER_ID, {})
    records = env[model_name].search([(email_field, 'not in', [False, ''])])

    for record in records:
        email = getattr(record, email_field, False)
        if not email:
            continue
        validation = env['kw.email.validation'].get_validation(email)
        if validation:
            record.kw_email_validation_id = validation.id
