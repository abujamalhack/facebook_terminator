import random
import time
import numpy as np

class BehavioralMimic:
    def __init__(self):
        self.behavior_patterns = self.load_behavior_patterns()
    
    def load_behavior_patterns(self):
        """تحميل أنماط السلوك البشري"""
        return {
            'scroll_speed': [200, 300, 400, 500],
            'wait_times': [1.5, 2.0, 2.5, 3.0, 4.0],
            'tap_positions': [
                (100, 200), (150, 300), (200, 400),
                (250, 350), (300, 250)
            ]
        }
    
    def random_scroll(self, driver):
        """تمرير عشوائي للشاشة"""
        scroll_amount = random.choice(self.behavior_patterns['scroll_speed'])
        direction = random.choice([-1, 1])
        
        script = f"window.scrollBy(0, {scroll_amount * direction})"
        driver.execute_script(script)
    
    def random_wait(self):
        """انتظار عشوائي"""
        wait_time = random.choice(self.behavior_patterns['wait_times'])
        time.sleep(wait_time)
    
    def random_tap(self, driver, element=None):
        """نقر عشوائي"""
        if element:
            try:
                action = ActionChains(driver)
                action.move_to_element(element)
                action.click()
                action.perform()
            except:
                pass
    
    def human_like_session(self, driver, duration=60):
        """جلسة تشبه السلوك البشري"""
        start_time = time.time()
        
        while time.time() - start_time < duration:
            # مزيج عشوائي من الإجراءات
            actions = [
                lambda: self.random_scroll(driver),
                lambda: self.random_wait(),
                lambda: self.random_tap(driver)
            ]
            
            for _ in range(random.randint(2, 5)):
                random.choice(actions)()
            
            self.random_wait()
