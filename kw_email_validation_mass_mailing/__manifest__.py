{
    'name': 'Email Validation - Mass Mailing',
    'summary': '''
        Mass Mailing Email Validation | Mass Mailing Email Verification |
        Mailing List Validator | Mailing List Email Check |
        Mailing List Cleaner | Mailing List Hygiene |
        mailing.contact Email Validation | mailing.contact Email Verification |
        Bulk Email Cleaning | Bulk Email Validation | Bulk Email Verification |
        Marketing List Quality | Marketing Email Validator |
        Newsletter List Cleaning | Subscriber Email Validation |
        Bounce Prevention | Bounce Rate Reduction |
        Sender Reputation Protection | Email Deliverability |
        Email Validator | Email Verifier | Email Checker |
        Validates the email field on mailing.contact records and flags
        invalid addresses before a campaign is sent. Cuts hard bounces,
        protects sender reputation, and keeps marketing lists clean for
        higher deliverability and engagement.
    ''',

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Hidden/Tools',
    'license': 'LGPL-3',
    'version': '17.0.1.0.0',

    'depends': [
        'mass_mailing',
        'kw_email_validation',
    ],

    'external_dependencies': {'python': [], },

    'data': [
        'views/mailing_contact_views.xml',
    ],
    'demo': [
    ],

    'installable': True,
    'auto_install': False,
    'application': False,
    'post_init_hook': 'post_init_hook',

    'images': [
        'static/description/cover.png',
        'static/description/icon.png',
    ],

}
