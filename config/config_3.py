import undetected_chromedriver as uc

WEBDRIVER_CONFIG_3 = {
    "name": "Privacy and Security Focused",
    "headless": False,
    "start_maximized": False,
    "window_size": "1366,768",
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "disable_extensions": True,
    "incognito": True,
    "disable_cookies": True,
    "disable_cache": True,
    "disable_geolocation": True,
    "disable_notifications": True,
    "disable_webgl": True,
    "disable_automated_test_detection": True,
    # "proxy": "socks5://127.0.0.1:9150", # Torプロキシを一時的に無効化
    "disable_plugins": True,
    "disable_popup_blocking": False,
    "disable_password_saving": True,
    "disable_autofill": True,
    "disable_client_side_phishing_detection": True,
    "disable_default_apps": True,
    "disable_webrtc": True,
    "disable_infobars": True,
    "no_sandbox": True,
    "ignore_certificate_errors": False,
}

def apply_config(options: uc.ChromeOptions, config: dict):
    if config.get("headless"):
        options.add_argument("--headless")
    if config.get("start_maximized"):
        options.add_argument("--start-maximized")
    if config.get("window_size"):
        options.add_argument(f"--window-size={config['window_size']}")
    if config.get("user_agent"):
        options.add_argument(f"user-agent={config['user_agent']}")
    if config.get("disable_extensions"):
        options.add_argument("--disable-extensions")
    if config.get("incognito"):
        options.add_argument("--incognito")
    if config.get("disable_cookies"):
        options.add_argument("--disable-cookies")
    if config.get("disable_cache"):
        options.add_argument("--disable-cache")
    if config.get("disable_geolocation"):
        options.add_argument("--disable-geolocation")
    if config.get("disable_notifications"):
        options.add_argument("--disable-notifications")
    if config.get("disable_webgl"):
        options.add_argument("--disable-webgl")
    if config.get("disable_automated_test_detection"):
        options.add_argument("--disable-blink-features=AutomationControlled")
    if config.get("disable_plugins"):
        options.add_argument("--disable-plugins")
    if not config.get("disable_popup_blocking"):
        options.add_argument("--disable-popup-blocking")
    if config.get("disable_password_saving"):
        options.add_argument("--password-store=basic")
    if config.get("disable_autofill"):
        options.add_argument("--disable-autofill")
    if config.get("disable_client_side_phishing_detection"):
        options.add_argument("--disable-client-side-phishing-detection")
    if config.get("disable_default_apps"):
        options.add_argument("--disable-default-apps")
    if config.get("disable_webrtc"):
        options.add_argument("--disable-webrtc")
    if config.get("disable_infobars"):
        options.add_argument("--disable-infobars")
    if config.get("no_sandbox"):
        options.add_argument("--no-sandbox")
    if not config.get("ignore_certificate_errors"):
        options.add_argument("--enable-strict-mixed-content-checking")
    if config.get("proxy"):
        options.add_argument(f"--proxy-server={config['proxy']}")
    return options