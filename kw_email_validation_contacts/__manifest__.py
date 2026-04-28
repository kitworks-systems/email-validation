{
    'name': 'Email Validation - Contacts',
    'summary': '''
        Partner Email Validation | Contact Email Validation |
        Partner Email Verification | Contact Email Verification |
        res.partner Email Validator | res.partner Email Check |
        Customer Email Validation | Customer Email Verification |
        Customer Email Checker | Supplier Email Validation |
        Supplier Email Verification | Vendor Email Check |
        Address Book Email Validator | Master Data Email Quality |
        Master Data Quality | Contact Data Cleansing |
        Partner Data Cleansing | CRM Contacts Email Check |
        Email Validator | Email Verifier | Email Checker |
        Validates email addresses on res.partner records (customers,
        suppliers, vendors) with a status badge displayed in contact
        list and form views. Improves master data quality by flagging
        invalid partner emails before they reach quotations, invoices
        or marketing campaigns.
    ''',

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Hidden/Tools',
    'license': 'LGPL-3',
    'version': '17.0.1.0.0',

    'depends': [
        'contacts',
        'kw_email_validation',
    ],

    'external_dependencies': {'python': [], },

    'data': [
        'views/res_partner_views.xml',
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
