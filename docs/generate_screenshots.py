#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Скрипт для автоматичного створення скріншотів для документації
модулів валідації email в Odoo.
"""

import os
import time
import yaml
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ScreenshotGenerator:
    """Клас для генерації скріншотів на основі конфігурації YAML."""
    
    def __init__(self, config_file, base_url, username, password, output_dir=None):
        """Ініціалізація генератора скріншотів."""
        self.config_file = config_file
        self.base_url = base_url
        self.username = username
        self.password = password
        
        # Завантаження конфігурації
        with open(config_file, 'r') as f:
            self.config = yaml.safe_load(f)
        
        # Визначення директорії для збереження скріншотів
        if output_dir:
            self.output_dir = output_dir
        else:
            self.output_dir = self.config.get('output_dir', 'screenshots')
        
        # Створення директорії, якщо вона не існує
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Налаштування Selenium WebDriver
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--headless")  # Запуск у фоновому режимі
        
        # Використання webdriver-manager для автоматичного завантаження ChromeDriver
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
    
    def login(self):
        """Вхід в Odoo."""
        self.driver.get(self.base_url + "/web/login")
        
        # Заповнення форми входу
        self.driver.find_element(By.ID, "login").send_keys(self.username)
        self.driver.find_element(By.ID, "password").send_keys(self.password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        # Очікування завантаження головної сторінки
        try:
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "o_home_menu")))
            print("Успішний вхід в Odoo")
        except TimeoutException:
            print("Помилка входу в Odoo")
            self.driver.quit()
            exit(1)
    
    def take_screenshot(self, name, path, wait_for, click=None, select_rows=None, filename=None):
        """Створення скріншоту для конкретної сторінки."""
        print(f"Створення скріншоту: {name}")
        
        # Перехід на сторінку
        self.driver.get(self.base_url + path)
        
        # Очікування завантаження елемента
        try:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, wait_for)))
            print(f"  Елемент {wait_for} знайдено")
        except TimeoutException:
            print(f"  Помилка: елемент {wait_for} не знайдено")
            return False
        
        # Вибір рядків (для масової валідації)
        if select_rows:
            try:
                for row in select_rows:
                    checkbox = self.driver.find_element(By.XPATH, f"//table[contains(@class, 'o_list_table')]/tbody/tr[{row}]/td[1]/div/input")
                    checkbox.click()
                print(f"  Вибрано {len(select_rows)} рядків")
            except Exception as e:
                print(f"  Помилка вибору рядків: {e}")
        
        # Клік на елемент (якщо потрібно)
        if click:
            try:
                element = self.driver.find_element(By.CSS_SELECTOR, click)
                element.click()
                print(f"  Клік на елемент {click}")
                
                # Очікування після кліку
                time.sleep(1)
            except Exception as e:
                print(f"  Помилка кліку на елемент {click}: {e}")
        
        # Визначення імені файлу
        if not filename:
            filename = f"{name}.png"
        
        # Створення скріншоту
        screenshot_path = os.path.join(self.output_dir, filename)
        self.driver.save_screenshot(screenshot_path)
        print(f"  Скріншот збережено: {screenshot_path}")
        
        return True
    
    def generate_screenshots(self):
        """Генерація всіх скріншотів згідно з конфігурацією."""
        # Вхід в Odoo
        self.login()
        
        # Перебір всіх розділів конфігурації
        for section_name, screenshots in self.config.items():
            # Пропуск службових розділів
            if section_name in ['version', 'project', 'output_dir']:
                continue
            
            print(f"\nРозділ: {section_name}")
            
            # Створення директорії для розділу
            section_dir = os.path.join(self.output_dir, section_name)
            os.makedirs(section_dir, exist_ok=True)
            
            # Перебір всіх скріншотів у розділі
            for screenshot in screenshots:
                name = screenshot.get('name')
                description = screenshot.get('description', '')
                path = screenshot.get('path')
                wait_for = screenshot.get('wait_for')
                click = screenshot.get('click')
                select_rows = screenshot.get('select_rows')
                filename = screenshot.get('filename', f"{name}.png")
                
                # Перевірка обов'язкових параметрів
                if not all([name, path, wait_for]):
                    print(f"  Пропуск скріншоту {name}: відсутні обов'язкові параметри")
                    continue
                
                # Створення скріншоту
                success = self.take_screenshot(
                    name=name,
                    path=path,
                    wait_for=wait_for,
                    click=click,
                    select_rows=select_rows,
                    filename=os.path.join(section_name, filename)
                )
                
                if not success:
                    print(f"  Помилка створення скріншоту {name}")
        
        # Закриття браузера
        self.driver.quit()
        print("\nГенерація скріншотів завершена")

def main():
    """Головна функція скрипту."""
    parser = argparse.ArgumentParser(description='Генерація скріншотів для документації Odoo')
    parser.add_argument('--config', default='screenshots.yaml', help='Шлях до файлу конфігурації')
    parser.add_argument('--url', default='http://127.0.16.1:16001', help='Базовий URL Odoo')
    parser.add_argument('--username', default='admin', help='Ім\'я користувача Odoo')
    parser.add_argument('--password', default='admin', help='Пароль користувача Odoo')
    parser.add_argument('--output', help='Директорія для збереження скріншотів')
    
    args = parser.parse_args()
    
    generator = ScreenshotGenerator(
        config_file=args.config,
        base_url=args.url,
        username=args.username,
        password=args.password,
        output_dir=args.output
    )
    
    generator.generate_screenshots()

if __name__ == '__main__':
    main()
