import undetected_chromedriver as uc

#bot対策
WEBDRIVER_CONFIG_1 = {
    "headless": False,
    "start_maximized": True,
    "disable_dev_shm_usage": True,
    "disable_automation": True,
    "window_size": None 
}

def apply_config(options: uc.ChromeOptions, config: dict):
    if config.get("headless"):
        options.add_argument("--headless")
    if config.get("start_maximized"):
        options.add_argument("--start-maximized")
    if config.get("disable_dev_shm_usage"):
        options.add_argument("--disable-dev-shm-usage")
    if config.get("disable_automation"):
        options.add_argument("--disable-blink-features=AutomationControlled")
    if config.get("window_size"):
        options.add_argument(f"--window-size={config['window_size']}")  
    
    # undetected_chromedriver 特有の設定
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--ignore-certificate-errors")
    
    return options