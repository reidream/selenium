import os
from dotenv import load_dotenv
from CustomWebDriver import CustomWebdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchWindowException

load_dotenv("facebook.env")
# EMAIL = os.getenv("email")
# PASSWORD = os.getenv("key")
EMAIL ="Hello Test"
PASSWORD = "123456789"

config={
    "bot_prevention": "config_1",
    "high_speed": "config_2",
    "privacy_focused": "config_3"
}

kwargs={
    "headless": False
}
custom_driver = CustomWebdriver(config["high_speed"], **kwargs)
driver=custom_driver.create_driver()

# def make_driver():   
#     custom_driver = CustomWebdriver(config["high_speed"], **kwargs)
#     custom_driver.create_driver()
#     return custom_driver

def login_to_tinder():#dont forget 
        custom_driver.driver.get("https://tinder.com/app/explore")
        custom_driver.wait_and_click(By.XPATH, "//div[text()='ログイン']")
        custom_driver.wait_and_click(By.XPATH, "//div[text()='Facebookでログイン']")
        if custom_driver.switch_to_popup():
            email_field = custom_driver.find_element_safely(By.ID, "email")
            password_field = custom_driver.find_element_safely(By.ID, "pass")
            login_button = custom_driver.find_element_safely(By.CSS_SELECTOR, "input[name=login]")
            if email_field and password_field and login_button :
                email_field.send_keys(EMAIL)
                password_field.send_keys(PASSWORD) 
                # login_button.click() 
                
                
                input("Close the browser by pressing 'ENTER KEY'")
                return True
            else:
                return False

    
def main():
    # custom_driver_1 = make_driver()
    if login_to_tinder():  # Corrected from "longin" to "login"
        print("Login complete")
    else:
        print("Login failed")

main()



    
