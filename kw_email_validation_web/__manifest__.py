{
    'name': 'Email Validation - Web Interface',
    'summary': '''
        Bulk Email Validation Web | Web Email Validator |
        Bulk Email Verification Form | Web Bulk Email Check |
        Public Email Validator Form | Online Email Validation |
        CSV Email Validation | List Email Verification |
        Multiple Email Validation | Mass Email Address Check |
        Web-based Email Verifier | Browser Email Validator |
        Public Bulk Validation Endpoint | One-click Email Validation |
        Email Validator | Email Verifier | Email Checker |
        Public web interface and HTTP endpoint for single-address and
        bulk email validation. Submit a list of addresses, get a validation
        result per record using any validator configured in the suite.
        Includes a manual entry form and a CSV-style bulk-paste field.
    ''',

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Hidden/Tools',
    'license': 'LGPL-3',
    'version': '19.0.1.0.0',

    'depends': [
        'web',
        'kw_email_validation',
    ],

    'external_dependencies': {'python': [], },

    'data': [
        'security/ir.model.access.csv',
        'views/templates/email_validation_templates.xml',
        'views/menu_views.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': False,

    'images': [
        'static/description/cover.png',
        'static/description/icon.png',
    ],
}
