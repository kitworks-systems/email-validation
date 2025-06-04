# Email Validation - Web Interface

Web interface module for email address validation in Odoo 16.0.

## Description

The `kw_email_validation_web` module adds a convenient web interface for bulk email address validation. It allows users to upload lists of email addresses for validation, view validation results, and export them in various formats.

## Key Features

- Web interface for bulk email validation
- Upload email address lists from CSV/Excel files
- Manual entry of address lists for verification
- Visualization of validation results
- Export results in various formats (CSV, Excel, PDF)
- Filtering and sorting results by validation status

## Dependencies

- `kw_email_validation` - base email validation module
- `web` - Odoo base web module

## Installation

1. Install the base module `kw_email_validation`
2. Install the `kw_email_validation_web` module

## Usage

### Accessing the Web Interface

After installing the module, the email validation web interface is accessible via:

1. Menu **Email Validation > Web Interface**
2. Or directly via URL: `/email_validation/web`

### Bulk Email Validation

1. Open the validation web interface
2. Choose one of the methods for entering email addresses:
   - Upload a CSV/Excel file
   - Manual entry of address list
   - Copy list from clipboard
3. Click the "Validate" button
4. Wait for the validation process to complete
5. View the results and export them if needed

### Exporting Results

Validation results can be exported in the following formats:
- CSV
- Excel
- PDF

## Technical Details

The module uses Odoo controllers for processing HTTP requests and QWeb templates for displaying the web interface. It interacts with the base `kw_email_validation` module to perform email address validation.

## Benefits

- Convenient interface for bulk email validation
- Quick verification of large contact lists
- Ability to export results for further use
- Integration with other modules of the email validation system

## License

LGPL-3

## Author

Kitworks Systems: https://kitworks.systems/
