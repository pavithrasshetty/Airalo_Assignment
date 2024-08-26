import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import homepage_xpaths as xpaths


class AiraloTests(unittest.TestCase):
    # Set up Chrome options
    options = webdriver.ChromeOptions()

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=options)

    page_url = "https://www.airalo.com/"
    country = "Japan"

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def click_element(self, xpath):
        element = self.driver.find_element_by_xpath(xpath)
        element.click()

    def click_on_text(self, text):
        self.driver.find_element_by_xpath(f"(//*[contains(text(), '{text}')])[2]").click()
        time.sleep(5)

    def select_google_search_engine(self):
        self.click_element(xpaths.google_search_engine_radio_button)

    def accept_privacy_policy(self):
        is_privacy_policy_popup_displayed = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, xpaths.privacy_accept_button)))
        if is_privacy_policy_popup_displayed:
            self.click_element(xpaths.privacy_accept_button)
            print("Privacy policy has been accepted")
        else:
            print("Privacy policy popup is not displayed")

    def dont_allow_notifications(self):
        is_notification_permission_popup_displayed = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, xpaths.dont_allow_notification_button)))
        if is_notification_permission_popup_displayed:
            self.click_element(xpaths.dont_allow_notification_button)
            print("Notification permission has been rejected")
        else:
            print("Notification permission popup is not displayed")

    def search_for_the_country(self, country_name):
        search_element = self.driver.find_element_by_xpath(xpaths.search_field)
        time.sleep(2)
        if search_element.is_enabled():
            search_element.click()
            search_element.send_keys(country_name)
            time.sleep(5)
        else:
            print("Element is not enabled.")

    def select_the_first_esim_package(self):
        self.click_element(xpaths.first_esim_package)

    def click_on_buy_now_button_of_first_esim_package(self):
        self.click_element(xpaths.first_buy_now_button)

    def assert_element_and_text_displayed_are_correct(self, name, value):
        name_element = self.driver.find_element_by_xpath(f"//*[@class='package-list-detail']//*[contains(text(), '{name}')]")
        assert name_element.is_displayed(), message

        expected_value_xpath = f"//*[@class='package-list-detail']//*[contains(text(), '{name}')]/following-sibling::*[contains(text(), '{value}')]"
        value_element = self.driver.find_element_by_xpath(expected_value_xpath)
        assert value_element.is_displayed(), message
        # OR
        expected_value = value_element.text
        print(f"{name} is expected_value")
        assert expected_value == value, f"{value} is missing in esim details"


    #####    TESTS      #####

    def test_1_launch_airalo_website(self):
        # Launch the website
        self.driver.get(self.page_url)

        # Print the page title
        print(self.driver.title)

        time.sleep(5)
        #self.select_google_search_engine()
        self.accept_privacy_policy()
        self.dont_allow_notifications()

    def test_2_search_for_japan(self):
        time.sleep(10)
        self.search_for_the_country(self.country)
        self.click_on_text(self.country)

    def test_3_buy_first_esim_package(self):
        self.click_on_buy_now_button_of_first_esim_package()

    def test_4_verify_the_esim_package_info_displayed(self):
        time.sleep(2)
        self.assert_element_and_text_displayed_are_correct("COVERAGE","Japan")
        self.assert_element_and_text_displayed_are_correct("DATA", "1 GB")
        self.assert_element_and_text_displayed_are_correct("VALIDITY", "7 Days")
        self.assert_element_and_text_displayed_are_correct("PRICE", "4.50 €")

if __name__ == '__main__':
    unittest.main()