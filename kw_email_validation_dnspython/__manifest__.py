{
    'name': 'Email Validation - DNS',
    'summary': '''
        DNS Email Validator | DNS Email Verification |
        DNS Email Check | DNS Based Email Validation |
        MX Record Validation | MX Record Email Check |
        MX Lookup Email Validator | A Record Email Check |
        Domain Validation | Domain Email Verification |
        Domain MX Check | Email Domain Resolver |
        dnspython Email Check | dnspython Email Validator |
        Mail Exchanger Lookup | Email Domain Existence Check |
        Email Validator | Email Verifier | Email Checker |
        DNS-based email validator that resolves MX and A records via the
        dnspython library to confirm the recipient domain is configured to
        accept mail. Plugs into the Email Validation Suite as an additional
        rule for the validation pipeline.
    ''',

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Hidden/Tools',
    'license': 'LGPL-3',
    'version': '17.0.1.0.0',

    'depends': [
        'crm',
        'kw_email_validation',
    ],

    'external_dependencies': {
        'python': ['dnspython'],
    },

    'data': [
        'data/email_validator.xml',
    ],
    'demo': [
    ],

    'installable': True,
    'auto_install': False,
    'application': False,

    'images': [
        'static/description/cover.png',
        'static/description/icon.png',
    ],

}
