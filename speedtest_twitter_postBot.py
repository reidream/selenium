from CustomWebDriver import CustomWebdriver
from twitter_post import My_Twitter
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SpeedTestTwitterBot:
    def __init__(self, config_name, **kwargs):
        self.custom_driver = CustomWebdriver(config_name, **kwargs)
        self.driver = self.custom_driver.create_driver()

    def close_cookie_popup(self):
        try:
            self.custom_driver.wait_and_click(By.ID, "onetrust-accept-btn-handler")
        except Exception as e:
            print(f"Cookie consent button not found or click failed: {e}")

    def get_speedtest_result(self):
        self.driver.get("https://www.speedtest.net/")
        self.close_cookie_popup()
        try:
            self.custom_driver.wait_and_click(By.XPATH, '//span[text()="Go"]')
            download = self.custom_driver.find_element_safely(
                By.XPATH, '//span[@class="result-data-large number result-data-value download-speed"]', 100)
            upload = self.custom_driver.find_element_safely(
                By.XPATH, '//span[@class="result-data-large number result-data-value upload-speed"]', 100)
            return self.custom_driver.wait_for_element_text(download, upload)
        except Exception as e:
            print(f"Failed to get speed test results: {e}")
            return None

    def post_to_twitter(self, post_text):
        try:
            twitter = My_Twitter()
            if twitter.login_twitter():
                print("Twitter login succeeded")
                twitter.twitter_post(post_text)
                if twitter.verify_post_success():
                    print("Tweet posted successfully")
                else:
                    print("Failed to verify tweet post")
            else:
                print("Twitter login failed")
        except Exception as e:
            print(f"Error during Twitter posting: {e}")
        finally:
            if hasattr(twitter, 'custom_driver'):
                twitter.custom_driver.quit()

    def run(self):
        try:
            results = self.get_speedtest_result()
            if results and len(results) == 2:
                post_text = f"DOWNLOAD: {results[0]}\nUPLOAD: {results[1]}"
                print(post_text)
                self.post_to_twitter(post_text)
            else:
                print("Failed to get valid speed test results")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.custom_driver.quit()

if __name__ == "__main__":
    bot = SpeedTestTwitterBot("config_2", headless=False)
    bot.run()