import undetected_chromedriver as uc

# 高速処理用の設定
WEBDRIVER_CONFIG_2 = {
    "headless": True,
    "start_maximized": False,
    "disable_dev_shm_usage": True,
    "disable_automation": False,
    "window_size": "1920,1080",
    "no_sandbox": True,
    "disable_gpu": True,
    "disable_images": True,
    "disable_javascript": False,
    "ignore_certificate_errors": True,
    "disable_extensions": True,
    "disable_logging": True
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
    if config.get("no_sandbox"):
        options.add_argument("--no-sandbox")
    if config.get("disable_gpu"):
        options.add_argument("--disable-gpu")
    if config.get("disable_images"):
        options.add_argument("--blink-settings=imagesEnabled=false")
    if config.get("disable_javascript"):
        options.add_argument("--disable-javascript")
    if config.get("ignore_certificate_errors"):
        options.add_argument("--ignore-certificate-errors")
    if config.get("disable_extensions"):
        options.add_argument("--disable-extensions")
    if config.get("disable_logging"):
        options.add_argument("--disable-logging")
    
    # パフォーマンス関連の設定
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    
    return options


