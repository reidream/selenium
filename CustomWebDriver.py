import importlib.util
import os
import importlib
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException, NoSuchWindowException
from selenium.webdriver.common.by import By

class CustomWebdriver:
    def __init__(self, config_name='config_1', config_dir="config", **kwargs):
        self.options = uc.ChromeOptions()
        try:
            config_path = os.path.join(config_dir,f"{config_name}.py")
            spec = importlib.util.spec_from_file_location(config_name, config_path)
            config_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(config_module)
            
            self.config = getattr(config_module, f'WEBDRIVER_CONFIG_{config_name.split("_")[-1]}').copy()
            self.apply_config = config_module.apply_config
        except (ImportError, AttributeError) as e:
            print(f"Error loading configuration: {str(e)}")
            raise
        self.config.update(kwargs)
        self.options = self.apply_config(self.options, self.config)
        self.driver = None

    def create_driver(self):
        try:
            self.driver = uc.Chrome(options=self.options)
            print(f"Chrome driver (undetected) created successfully using {self.config}")
            return self.driver
        except WebDriverException as e:
            print(f"Error in creating driver: {str(e)}")
            return None

    def find_element_safely(self, by, value, timeout=10):
        self._check_driver()
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            print(f"Element not found: {by}={value}")
            return None

    def switch_to_popup(self, timeout=10):
        self._check_driver()
        original_window = self.driver.current_window_handle
        try:
            WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) > 1)
            for window_handle in self.driver.window_handles:
                if window_handle != original_window:
                    self.driver.switch_to.window(window_handle)
                    return True
            return False  
        except TimeoutException:
            print("No new window appeared within the timeout period.")
            return False

    def switch_to_main_window(self):
        self._check_driver()
        try:
            main_window = self.driver.window_handles[0]
            self.driver.switch_to.window(main_window)
        except IndexError:
            print("No windows available.")

    def close_current_window(self):
        self._check_driver()
        try:
            self.driver.close()
            if len(self.driver.window_handles) > 0:
                self.switch_to_main_window()
            else:
                self.driver = None
        except NoSuchWindowException:
            print("Current window is already closed.")

    def wait_and_click(self, by, value, timeout=10):
        self._check_driver()
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            element.click()
            return True
        except TimeoutException:
            print(f"Element not clickable: {by}={value}")
            return False
        
    def close_extra_popups(self):
        main_window = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)
                self.driver.close()
        self.driver.switch_to.window(main_window)  
    
    def wait_for_element_text(self, *element, timeout=120):
        element_list=[]
        try:
            for i in element:
                WebDriverWait(self.driver, timeout).until(
                    lambda d: i.text != '—' and i.text != ''
                )
                element_list.append(i.text)   
            return element_list  
        except Exception as e:
            print(f"error: {e}")

    def quit(self):
        if self.driver:
            self.driver.quit()
            self.driver = None

    def _check_driver(self):
        if not self.driver:
            raise Exception("Driver not created. Call create_driver() first.")