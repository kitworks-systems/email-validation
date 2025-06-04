import logging

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class EmailValidationController(http.Controller):
    """Controller for the email validation web interface."""

    @http.route('/email_validation/validate', type='http', auth='user',
                website=True)
    def validate_email_form(self, **kw):
        """Display the form for email validation."""
        validators = request.env['kw.email.validator'].sudo().search([])
        return request.render(
            'kw_email_validation_web.validate_email_form_template', {
                'validators': validators,
            })

    @http.route('/email_validation/validate_batch', type='http',
                auth='user', methods=['POST'], website=True, csrf=True)
    def validate_email_batch(self, **post):
        """Process a request to validate multiple email addresses."""
        emails_text = post.get('emails', '')
        validator_id = post.get('validator_id')

        # Split the input text into separate email addresses
        emails = [e.strip() for e in emails_text.split('\n') if e.strip()]

        results = []
        validation_model = request.env['kw.email.validation'].sudo()

        # If a specific validator is specified
        if validator_id and validator_id.isdigit():
            validator = request.env['kw.email.validator'].sudo().browse(
                int(validator_id))

            for email in emails:
                validation = validation_model.get_validation(email)
                if validation:
                    # Validate email using the specified validator
                    validator.validate_email(validation)
                    results.append({
                        'email': email,
                        'state': validation.state,
                        'message': validation.message or '',
                    })
        else:
            # Automatic validator selection according to rules
            for email in emails:
                validation = validation_model.get_validation(email)
                if validation:
                    validation.validate_email()
                    results.append({
                        'email': email,
                        'state': validation.state,
                        'message': validation.message or '',
                    })

        return request.render(
            'kw_email_validation_web.validate_email_results_template', {
                'results': results,
            })

    @http.route('/email_validation/validate_ajax', type='json',
                auth='user', website=True, csrf=True)
    def validate_email_ajax(self, **post):
        """AJAX endpoint for validating a single email."""
        email = post.get('email', '').strip()
        validator_id = post.get('validator_id')

        if not email:
            return {'error': 'Email not specified'}

        validation_model = request.env['kw.email.validation'].sudo()
        validation = validation_model.get_validation(email)

        if not validation:
            return {'error': 'Failed to create validation record'}

        # If a specific validator is specified
        if validator_id and validator_id.isdigit():
            validator = request.env['kw.email.validator'].sudo().browse(
                int(validator_id))
            validator.validate_email(validation)
        else:
            # Automatic validator selection according to rules
            validation.validate_email()

        return {
            'email': email,
            'state': validation.state,
            'message': validation.message or '',
        }
