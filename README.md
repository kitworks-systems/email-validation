# Email Validation for Odoo

Comprehensive solution for email address validation in Odoo 16.0, developed by Kitworks Systems.

## Overview

The Email Validation system provides the ability to verify the correctness of email addresses in various Odoo modules. It includes a base module and a set of integration modules for different parts of Odoo.

Key features:
- Email address syntax verification
- Domain and MX record verification
- Integration with external APIs for advanced validation
- Automatic validation when creating/updating records
- Visual display of validation status
- Manual verification through the action menu
- Automatic validation of existing records when installing modules

## Project Structure

### Base Module

- **kw_email_validation** - core module with basic validation functionality

### Integration Modules

- **kw_email_validation_contacts** - email validation for contacts (res.partner)
- **kw_email_validation_crm** - email validation for CRM leads (crm.lead)
- **kw_email_validation_hr** - email validation for employees (hr.employee)
- **kw_email_validation_event** - email validation for event registrations (event.registration)
- **kw_email_validation_mass_mailing** - email validation for mailing contacts (mailing.contact)
- **kw_email_validation_hr_recruitment** - email validation for applicants (hr.applicant)
- **kw_email_validation_smtp** - email validation when sending emails via SMTP
- **kw_email_validation_dnspython** - enhanced validation using DNSPython
- **kw_email_validation_web** - web interface for email validation
- **kw_email_validation_bundle** - metapackage for installing all modules together

## Supported Validation Services

The system supports integration with the following external validation services:

1. **NeverBounce** - high accuracy, speed, detailed information about results
2. **QuickEmailVerification** - high accuracy, speed, detailed information
3. **MillionVerifier** - medium accuracy, high speed, low price
4. **SendPulse** - integration with other SendPulse services
5. **ZeroBounce** - high accuracy, AI scoring, spam trap detection
6. **Clearout** - high accuracy, spam trap detection
7. **MailerCheck** - high accuracy, spam trap detection
8. **Mailgun** - high accuracy, integration with other Mailgun services

Detailed information about validation services can be found in [validation_service.md](validation_service.md).

## Installation

1. Clone the repository into your Odoo addons directory:
   ```bash
   git clone https://github.com/kitworks-systems/email-validation.git
   ```

2. Update the module list in Odoo

3. Install the base module and required integration modules:
   - For basic functionality: `kw_email_validation`
   - For integration with contacts: `kw_email_validation_contacts`
   - For integration with CRM: `kw_email_validation_crm`
   - And so on...

4. To install all modules together, use the metapackage: `kw_email_validation_bundle`

## Configuration

1. Go to menu **Settings > Technical > Email Validation > Validators**
2. Configure parameters for each validator (API keys, URLs, etc.)
3. Set validator priorities through validation rules

## Usage

### Automatic Validation

After installation, the system automatically checks email addresses when creating or updating records.

### Manual Validation

1. Open a record with an email address
2. Use the action menu to launch manual verification

### Bulk Validation

1. Select multiple records in the list
2. Use the action menu to launch bulk verification

## License

LGPL-3

## Author

Kitworks Systems: https://kitworks.systems/
