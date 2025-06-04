#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Скрипт для додавання скріншотів до README файлів модулів валідації email.
"""

import os
import re
import argparse

# Словник відповідності модулів та скріншотів
MODULE_SCREENSHOTS = {
    'kw_email_validation': {
        'validators_list': '../docs/images/base_module/validators_list.png',
        'validator_form': '../docs/images/base_module/validator_form.png',
        'test_connection': '../docs/images/base_module/test_connection.png',
    },
    'kw_email_validation_contacts': {
        'contacts_list': '../docs/images/contacts_module/contacts_list.png',
        'contact_form': '../docs/images/contacts_module/contact_form.png',
        'manual_validation': '../docs/images/contacts_module/manual_validation.png',
    },
    'kw_email_validation_crm': {
        'leads_list': '../docs/images/crm_module/leads_list.png',
        'lead_form': '../docs/images/crm_module/lead_form.png',
    },
    'kw_email_validation_hr': {
        'employees_list': '../docs/images/hr_module/employees_list.png',
        'employee_form': '../docs/images/hr_module/employee_form.png',
    },
    'kw_email_validation_event': {
        'registrations_list': '../docs/images/event_module/registrations_list.png',
        'registration_form': '../docs/images/event_module/registration_form.png',
    },
    'kw_email_validation_hr_recruitment': {
        'applicants_list': '../docs/images/recruitment_module/applicants_list.png',
        'applicant_form': '../docs/images/recruitment_module/applicant_form.png',
    },
    'kw_email_validation_mass_mailing': {
        'mailing_contacts_list': '../docs/images/mass_mailing_module/mailing_contacts_list.png',
        'mailing_contact_form': '../docs/images/mass_mailing_module/mailing_contact_form.png',
    },
    'kw_email_validation_web': {
        'web_upload': '../docs/images/web_interface/web_upload.png',
        'web_results': '../docs/images/web_interface/web_results.png',
        'web_export': '../docs/images/web_interface/web_export.png',
    },
}

# Секції README, після яких потрібно додати скріншоти
SECTIONS = {
    'kw_email_validation': '## Key Features',
    'kw_email_validation_contacts': '## Key Features',
    'kw_email_validation_crm': '## Key Features',
    'kw_email_validation_hr': '## Key Features',
    'kw_email_validation_event': '## Key Features',
    'kw_email_validation_hr_recruitment': '## Key Features',
    'kw_email_validation_mass_mailing': '## Key Features',
    'kw_email_validation_web': '## Key Features',
}

def update_readme(module_path, module_name):
    """Оновлення README файлу модуля."""
    readme_path = os.path.join(module_path, 'README.md')
    
    # Перевірка наявності README файлу
    if not os.path.exists(readme_path):
        print(f"README файл не знайдено: {readme_path}")
        return False
    
    # Перевірка наявності скріншотів для модуля
    if module_name not in MODULE_SCREENSHOTS:
        print(f"Скріншоти для модуля {module_name} не знайдено")
        return False
    
    # Зчитування вмісту README файлу
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Перевірка наявності секції для додавання скріншотів
    section = SECTIONS.get(module_name)
    if not section or section not in content:
        print(f"Секцію {section} не знайдено в README файлі {readme_path}")
        return False
    
    # Перевірка наявності секції скріншотів
    screenshots_section = '## Screenshots'
    if screenshots_section in content:
        print(f"Секція скріншотів вже існує в README файлі {readme_path}")
        return False
    
    # Додавання секції скріншотів після вказаної секції
    screenshots_content = '\n\n## Screenshots\n\n'
    
    # Додавання скріншотів
    for name, path in MODULE_SCREENSHOTS[module_name].items():
        # Перевірка наявності файлу скріншоту
        if not os.path.exists(os.path.join(module_path, path.replace('../', ''))):
            print(f"Файл скріншоту не знайдено: {path}")
            continue
        
        # Додавання скріншоту
        screenshots_content += f'### {name.replace("_", " ").title()}\n\n'
        screenshots_content += f'![{name}]({path})\n\n'
    
    # Вставка секції скріншотів після вказаної секції
    pattern = f'({re.escape(section)}.*?)(\n\n##|$)'
    replacement = f'\\1\n{screenshots_content}\\2'
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Збереження оновленого вмісту README файлу
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"README файл оновлено: {readme_path}")
    return True

def main():
    """Головна функція скрипту."""
    parser = argparse.ArgumentParser(description='Оновлення README файлів модулів валідації email')
    parser.add_argument('--base-dir', default='/home/vovik/odoo_dev/addons16/repositories/kitworks-systems/email-validation',
                        help='Базова директорія проекту')
    
    args = parser.parse_args()
    
    # Перебір всіх модулів
    for module_name in MODULE_SCREENSHOTS.keys():
        module_path = os.path.join(args.base_dir, module_name)
        
        # Перевірка наявності директорії модуля
        if not os.path.exists(module_path):
            print(f"Директорію модуля не знайдено: {module_path}")
            continue
        
        # Оновлення README файлу модуля
        update_readme(module_path, module_name)

if __name__ == '__main__':
    main()
