from odoo.tests import tagged
from odoo.tests.common import HttpCase


@tagged('post_install', '-at_install')
class TestEmailValidationController(HttpCase):

    def setUp(self):
        super().setUp()
        self.authenticate('admin', 'admin')

    def test_form_page(self):
        response = self.url_open('/email_validation/validate')
        self.assertEqual(response.status_code, 200)
        self.assertIn('name="emails"', response.text)
        self.assertIn('Email Validation', response.text)

    def test_form_page_escapes_validator_name(self):
        self.env['kw.email.validator'].create(
            {'name': '<img src=x onerror=alert(1)>'})
        response = self.url_open('/email_validation/validate')
        self.assertEqual(response.status_code, 200)
        self.assertIn('&lt;img src=x onerror=alert(1)&gt;', response.text)
        self.assertNotIn('<img src=x', response.text)

    def test_batch_page_without_emails(self):
        response = self.url_open(
            '/email_validation/validate_batch',
            data={'emails': '', 'csrf_token': self.csrf_token()})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Return to form', response.text)

    def test_batch_page_without_csrf(self):
        with self.assertLogs('odoo.http', 'WARNING'):
            response = self.url_open(
                '/email_validation/validate_batch',
                data={'emails': 'third@example.com'})
        self.assertEqual(response.status_code, 400)

    def test_ajax_empty_email(self):
        result = self.make_jsonrpc_request(
            '/email_validation/validate_ajax', {'email': ' '})
        self.assertEqual(result, {'error': 'Email not specified'})
