import os
import time
from dotenv import load_dotenv
from CustomWebDriver import CustomWebdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


load_dotenv("twitter.env")
EMAIL = os.getenv("email")
PASSWORD = os.getenv("key")
NAME = os.getenv("name")
# EMAIL ="Hello Test"
# PASSWORD = "123456789"

config={
    "bot_prevention": "config_1",
    "high_speed": "config_2",
    "privacy_focused": "config_3"
}

kwargs={
    "headless": False
}
class My_Twitter:
    def __init__(self) -> None:       
        self.custom_driver = CustomWebdriver(config["bot_prevention"])
        self.driver = self.custom_driver.create_driver()
    def login_twitter(self):
        try:
            self.custom_driver.driver.get("https://twitter.com/i/flow/signup")
            self.custom_driver.wait_and_click(By.XPATH, '//span[text()="ログイン"]')

            # Enter email
            self.custom_driver.find_element_safely(By.NAME, "text").send_keys(EMAIL)
            self.custom_driver.wait_and_click(By.XPATH, '//span[text()="次へ"]')

            # Enter name
            self.custom_driver.find_element_safely(By.NAME, "text").send_keys(NAME)
            self.custom_driver.wait_and_click(By.XPATH, '//span[text()="次へ"]')

            # Enter password and login
            self.custom_driver.find_element_safely(By.XPATH, '//input[@name="password"]').send_keys(PASSWORD)
            self.custom_driver.wait_and_click(By.XPATH, '//button[@data-testid="LoginForm_Login_Button"]')           

            return True
        except Exception as e:
            print(f"Login failed: {e}")
            return False  
        

    def verify_post_success(self, timeout=30):
        try:
            # タイムラインの最新ツイートの時間要素を待つ
            time_element = self.custom_driver.find_element_safely(By.XPATH, '//div[@data-testid="User-Name"]//time')
            # 時間テキストを取得
            time_text = time_element.get_attribute('datetime')
            
            # 現在時刻との差を計算
            from datetime import datetime, timezone
            tweet_time = datetime.fromisoformat(time_text.replace('Z', '+00:00'))
            current_time = datetime.now(timezone.utc)
            time_difference = (current_time - tweet_time).total_seconds()
            
            # 60秒以内であれば成功とみなす
            if time_difference <= 60:
                print(f"Post verified: posted {time_difference:.0f} seconds ago")
                return True
            else:
                print(f"Post verification failed: last post was {time_difference:.0f} seconds ago")
                return False
        
        except Exception as e:
            print(f"Error verifying post: {e}")
            return False    
        
    def twitter_post(self, post_text):  
        # Click on Post button
        try:
            self.custom_driver.wait_and_click(By.XPATH, '//a[@aria-label="Post"]')  
            self.custom_driver.switch_to_popup()
            twitter_text = self.custom_driver.find_element_safely(By.XPATH, '//div[@data-testid="tweetTextarea_0"]')
            twitter_text.send_keys(post_text)
            self.custom_driver.wait_and_click (By.CSS_SELECTOR, 'button[data-testid="tweetButton"]')
            self.custom_driver.close_extra_popups()
            time.sleep(5)
            if not self.verify_post_success():
                raise Exception("Post verification failed")

            return True
        except Exception as e :
            print(f"error: {e}")
            return False    
          
       

if __name__ == "__main__":
    driver = My_Twitter()
    try:
        if driver.login_twitter():
            print("Login succesded")
    except:
        print("login failed")  
    try:
        if driver.twitter_post("hello test"):
            print("Post succesded") 
    except:
        print("Post faild")           

    input()
    driver.custom_driver.quit()    






