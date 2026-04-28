{
    'name': 'Email Validation - SMTP',
    'summary': '''
        SMTP Email Validator | SMTP Email Verification |
        SMTP Email Check | SMTP Based Email Validation |
        Mailbox Existence Check | Mailbox Verification |
        SMTP Handshake Validation | SMTP RCPT Check |
        Server-level Email Verification | Server-side Email Check |
        Recipient Server Probe | Recipient Mailbox Probe |
        Real-time Email Validation | Live Mailbox Check |
        Email Validator | Email Verifier | Email Checker |
        SMTP-based email validator that opens a connection to the recipient
        mail server and queries mailbox existence without sending mail.
        Plugs into the Email Validation Suite as an additional rule for the
        validation pipeline. No API key required.
    ''',

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Hidden/Tools',
    'license': 'LGPL-3',
    'version': '16.0.1.0.0',

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
