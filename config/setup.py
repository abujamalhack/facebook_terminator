# config.py
import os

class Config:
    # إعدادات النظام
    MAX_BOTS = 20
    ATTACK_DELAY = 2.0
    PROXY_ENABLED = True
    
    # مسارات الملفات
    PROXY_LIST_FILE = "config/proxies.txt"
    TARGETS_FILE = "config/targets.json"
    LOG_FILE = "logs/attack.log"
    
    # إعدادات API
    OPENAI_API_KEY = "your-api-key-here"
    
    @staticmethod
    def create_directories():
        """إنشاء المجلدات المطلوبة"""
        directories = [
            'mobile_botnet',
            'ai_content', 
            'session_hijacker',
            'behavioral_mimic',
            'command_control',
            'deployment',
            'config',
            'logs'
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
    
    @staticmethod
    def create_config_files():
        """إنشاء ملفات الإعداد"""
        # ملف البروكسيات
        with open(Config.PROXY_LIST_FILE, 'w') as f:
            f.write("# Add your proxies here\n")
            f.write("192.168.1.1:8080\n")
            f.write("192.168.1.2:8080\n")
        
        # ملف الأهداف
        with open(Config.TARGETS_FILE, 'w') as f:
            json.dump([], f, indent=2)

# تنفيذ الإعداد
if __name__ == '__main__':
    Config.create_directories()
    Config.create_config_files()
    print("[+] System configuration completed!")
