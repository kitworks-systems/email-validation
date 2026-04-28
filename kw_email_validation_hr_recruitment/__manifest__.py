{
    'name': 'Email Validation - HR Recruitment',
    'summary': """
        Candidate Email Validation | Candidate Email Verification |
        Applicant Email Validation | Applicant Email Verifier |
        Recruitment Email Validator | Recruitment Email Verification |
        hr.applicant Email Validation | hr.applicant Email Check |
        Job Applicant Email Check | Hiring Email Quality |
        Recruitment Pipeline Quality | Candidate Quality |
        Candidate Data Cleansing | ATS Email Validation |
        Applicant Tracking Email Check | Talent Acquisition Email Quality |
        Email Validator | Email Verifier | Email Checker |
        Validates the email_from field on hr.applicant records with a
        status badge in candidate kanban and list views. Helps recruiters
        focus on real applicants, reduces wasted outreach on invalid
        addresses and improves overall recruitment pipeline quality.
    """,

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Hidden/Tools',
    'license': 'LGPL-3',
    'version': '18.0.1.0.0',

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
    'post_init_hook': 'post_init_hook',

    'images': [
        'static/description/cover.png',
        'static/description/icon.png',
    ],

}
