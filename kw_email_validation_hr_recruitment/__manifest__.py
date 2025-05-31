{
    'name': 'Email Validation - HR Recruitment',
    'summary': """
        This module integrates email validation with the HR Recruitment module,
        allowing validation of job applicant email addresses.
    """,

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Customizations',
    'license': 'LGPL-3',
    'version': '16.0.1.0.0',

    'depends': [
        'hr_recruitment',
        'kw_email_validation',
    ],

    'external_dependencies': {'python': [], },

    'data': [
        'views/hr_applicant_views.xml',
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
