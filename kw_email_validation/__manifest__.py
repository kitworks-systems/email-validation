{
    'name': 'Base Email Validation',
    'summary': """
        Email Validator | Email Verifier | Email Checker | Email Validation |
        Email Verification | Email Check | Validate Email | Verify Email |
        Email Cleaner | Address Validator | Address Verifier | Email Tester |
        Validation Framework | Validator Engine | Rule Engine |
        Validation Pipeline | Extensible Validators | Custom Validators |
        Pluggable Validators | Email Validation Status | Validation Tracking |
        Syntax Email Check | Regex Email Check | Domain Email Check |
        Third Party Email Validation | External Validator API |
        Core framework for email address validation with status tracking,
        a pluggable rule engine and hooks for syntax, domain and external
        third-party validators. Foundation module of the Email Validation
        Suite, required by all CRM, HR, Contacts, Events, Mailing and SMTP
        and DNS validators.
    """,

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Hidden/Tools',
    'license': 'LGPL-3',
    'version': '18.0.1.0.0',

    'depends': [
        'web',
    ],

    'external_dependencies': {'python': [], },

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'data/email_validator.xml',
        'data/ir_cron.xml',

        'views/menu_views.xml',
        'views/email_validation_views.xml',
        'views/email_validator_views.xml',
        'views/email_validation_rule_views.xml',
    ],
    'demo': [
        'demo/email_validation.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': False,

    'images': [
        'static/description/cover.png',
        'static/description/icon.png',
    ],
}
