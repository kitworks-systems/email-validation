{
    'name': 'Email Validation - HR',
    'summary': '''
        Employee Email Validation | Employee Email Verification |
        HR Email Validator | HR Email Verifier | HR Email Checker |
        work_email Validation | work_email Verification |
        hr.employee Email Validation | hr.employee Email Check |
        Staff Email Validation | Workforce Email Quality |
        Employee Directory Quality | HR Master Data Quality |
        Internal Communication Quality | Onboarding Email Check |
        Email Validator | Email Verifier | Email Checker |
        Validates the work_email field on hr.employee records and displays
        a status badge in employee list, kanban and form views. Keeps the
        employee directory clean, ensures payroll, internal newsletters and
        HR notifications reach the right inbox.
    ''',

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Hidden/Tools',
    'license': 'LGPL-3',
    'version': '16.0.1.0.0',

    'depends': [
        'hr',
        'kw_email_validation',
    ],

    'external_dependencies': {'python': [], },

    'data': [
        'views/hr_employee_views.xml',
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
