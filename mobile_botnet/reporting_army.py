import threading
import random
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests

class MobileBot:
    def __init__(self, bot_id, proxy_config):
        self.bot_id = bot_id
        self.proxy_config = proxy_config
        self.driver = None
        
    def init_driver(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '11.0',
            'deviceName': f'bot_{self.bot_id}',
            'automationName': 'UiAutomator2',
            'browserName': 'Chrome',
            'chromeOptions': {
                'args': [f'--proxy-server={self.proxy_config}']
            }
        }
        
        try:
            self.driver = webdriver.Remote(
                'http://localhost:4723/wd/hub',
                desired_caps
            )
            return True
        except Exception as e:
            print(f"[-] Bot {self.bot_id} failed to initialize: {e}")
            return False
    
    def human_like_behavior(self):
        """محاكاة السلوك البشري"""
        actions = [
            lambda: self.driver.execute_script("window.scrollBy(0, 300)"),
            lambda: self.driver.execute_script("window.scrollBy(0, -150)"),
            lambda: time.sleep(random.uniform(2.0, 5.0))
        ]
        
        for _ in range(random.randint(3, 6)):
            random.choice(actions)()
    
    def report_profile(self, target_url, report_reason):
        """الإبلاغ عن الحساب المستهدف"""
        try:
            self.driver.get(target_url)
            time.sleep(3)
            
            # محاكاة السلوك البشري أولاً
            self.human_like_behavior()
            
            # النقر على القائمة
            menu_button = self.driver.find_element(
                By.XPATH, 
                '//button[@aria-label="More options"]'
            )
            menu_button.click()
            time.sleep(1)
            
            # اختيار الإبلاغ
            report_option = self.driver.find_element(
                By.XPATH,
                '//span[contains(text(), "Report")]'
            )
            report_option.click()
            time.sleep(1)
            
            # اختيار السبب
            reason_option = self.driver.find_element(
                By.XPATH,
                f'//span[contains(text(), "{report_reason}")]'
            )
            reason_option.click()
            time.sleep(1)
            
            # متابعة الإبلاغ
            next_button = self.driver.find_element(
                By.XPATH,
                '//span[text()="Next"]'
            )
            next_button.click()
            time.sleep(1)
            
            # تأكيد الإبلاغ
            submit_button = self.driver.find_element(
                By.XPATH,
                '//span[text()="Submit"]'
            )
            submit_button.click()
            
            print(f"[+] Bot {self.bot_id} successfully reported for {report_reason}")
            return True
            
        except Exception as e:
            print(f"[-] Bot {self.bot_id} reporting failed: {e}")
            return False
    
    def close(self):
        if self.driver:
            self.driver.quit()

class ReportingArmy:
    def __init__(self):
        self.bots = []
        self.report_reasons = [
            "Terrorism",
            "Child exploitation", 
            "Hate speech",
            "Bullying",
            "Impersonation",
            "Scam",
            "False information"
        ]
    
    def initialize_bots(self, num_bots=20):
        """تهيئة مجموعة البوتات"""
        proxies = self.load_proxies()
        
        for i in range(num_bots):
            proxy = random.choice(proxies) if proxies else None
            bot = MobileBot(i, proxy)
            if bot.init_driver():
                self.bots.append(bot)
                print(f"[+] Bot {i} initialized successfully")
            time.sleep(1)
    
    def load_proxies(self):
        """تحميل قائمة البروكسيات"""
        try:
            with open('config/proxies.txt', 'r') as f:
                return [line.strip() for line in f.readlines()]
        except:
            return []
    
    def mass_report_target(self, target_url):
        """هجمة الإبلاغ الجماعي"""
        if not self.bots:
            self.initialize_bots(15)
        
        threads = []
        
        for bot in self.bots:
            reason = random.choice(self.report_reasons)
            thread = threading.Thread(
                target=bot.report_profile,
                args=(target_url, reason)
            )
            threads.append(thread)
            thread.start()
            time.sleep(random.uniform(0.5, 2.0))
        
        # انتظار انتهاء جميع البوتات
        for thread in threads:
            thread.join()
        
        print(f"[+] Mass reporting completed for {target_url}")
    
    def cleanup(self):
        """تنظيف الموارد"""
        for bot in self.bots:
            bot.close()
