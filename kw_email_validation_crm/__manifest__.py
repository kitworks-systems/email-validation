{
    'name': 'Email Validation - CRM',
    'summary': """
        Lead Email Validation | Lead Email Verification |
        Opportunity Email Validation | Opportunity Email Check |
        CRM Email Validator | CRM Email Verifier | CRM Email Checker |
        crm.lead Email Validation | crm.lead Email Verification |
        Sales Lead Email Check | Sales Pipeline Quality |
        Lead Quality | Lead Qualification | Lead Scoring |
        Bad Lead Detection | Junk Lead Filter | Fake Lead Detection |
        Spam Lead Filter | Lead Data Cleansing | Lead Deduplication Helper |
        Email Validator | Email Verifier | Email Checker |
        Validates the email_from field on crm.lead records and shows a
        status badge in lead and opportunity list, kanban and form views.
        Helps sales teams qualify pipeline faster, prevent wasted outreach
        on invalid addresses and improve overall CRM data quality.
    """,

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Hidden/Tools',
    'license': 'LGPL-3',
    'version': '18.0.1.0.0',

    'depends': [
        'crm',
        'kw_email_validation',
    ],

    'external_dependencies': {'python': [], },

    'data': [
        'views/crm_lead_views.xml',
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
