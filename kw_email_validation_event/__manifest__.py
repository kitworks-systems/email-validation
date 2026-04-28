{
    'name': 'Email Validation - Events',
    'summary': '''
        Attendee Email Validation | Attendee Email Verification |
        Event Email Validator | Event Email Verifier | Event Email Checker |
        Registration Email Validation | Registration Email Verification |
        event.registration Email Check | Event Attendee Email Validator |
        Event Attendee Quality | Event Registration Quality |
        Conference Registration Validation | Webinar Email Verification |
        Event Invitation Deliverability | Event Bounce Prevention |
        Email Validator | Email Verifier | Email Checker |
        Validates the email field on event.registration records and shows a
        status badge in attendee list and kanban views. Ensures event
        invitations, reminders and post-event communications reach real
        attendees and reduces bounce rates on event campaigns.
    ''',

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Hidden/Tools',
    'license': 'LGPL-3',
    'version': '17.0.1.0.0',

    'depends': [
        'event',
        'kw_email_validation',
    ],

    'external_dependencies': {'python': [], },

    'data': [
        'views/event_registration_views.xml',
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
