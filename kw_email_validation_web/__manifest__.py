{
    'name': 'Email Validation - Web Interface',
    'summary': """
        Web interface for bulk email validation
        Provides a convenient interface for checking multiple email
        addresses at once.
    """,

    'author': 'Kitworks Systems',
    'website': 'https://github.com/kitworks-systems/email-validation',

    'category': 'Customizations',
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
