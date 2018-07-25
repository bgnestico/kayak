"""
Base class for the base of all pages, for all screen resolutions.
"""
import time
from qa_automation.base.base import Base
from qa_automation.qa_settings import WAIT
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException


class Categories(Base):
    """
    Locators:
    """
    body = (By.XPATH, "//table[@class='comp-tabl comp-tabl--ntnl']")
    top_1 = (By.XPATH, "//tbody//span[contains(text(),'#1 MOST POPULAR')]")
    top_2 = (By.XPATH, "//tbody//span[contains(text(),'#2')]")
    top_3 = (By.XPATH, "//tbody//span[contains(text(),'#3')]")
    stars_pos_1 = (By.XPATH, "//tbody/tr[1]//div[@class='sr__cntr']")
    stars_pos_2 = (By.XPATH, "//tbody/tr[2]//div[@class='sr__cntr']")
    stars_pos_3 = (By.XPATH, "//tbody/tr[3]//div[@class='sr__cntr']")
    read_more_btn_pos1 = (By.XPATH, "//table//a[@href='#campaign_1']"
                                    "[contains(text(),'Read More')]")
    read_more_btn_pos2 = (By.XPATH, "//table//a[@href='#campaign_2']"
                                    "[contains(text(),'Read More')]")
    read_more_btn_pos3 = (By.XPATH, "//table//a[@href='#campaign_3']"
                                    "[contains(text(),'Read More')]")
    ppc_banner = (By.XPATH, "//div/strong[@class='lead-cta__pos h2']")
    ppc_banner_stars = (By.XPATH, "//div[2]/div[@class='sr sr--sm']")

    """
    Methods:
    """
    def get_category_title(self, cat_name):
        return WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located(
                (By.XPATH, "//h1[contains(text(),'" + cat_name + "')]")))

    # Top 1 position ------------------------------------------------------
    def get_top_one_position(self, brand):
        WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located((tuple(self.top_1))))
        return self.driver.find_element(
            By.XPATH, "//tbody/tr[1]//div[contains(text(),'" + brand + "')]")

    def get_top_one_image(self, name):
        return WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located(
                (By.XPATH, "//tr[1]/td[1]/img[@src][contains(@alt,'"
                           + name + "')]")))

    def get_top_one_stars(self):
        return WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located((tuple(self.stars_pos_1))))

    def get_top_one_phone_btn(self, name):
        try:
            return WebDriverWait(self.driver, WAIT).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//tbody/tr[1]//a[contains(@data-campaign,'"
                               + name + "')][contains(@href,'tel')]")))
        except WebDriverException:
            return None

    def click_top_one_phone_btn(self, name):
        phone_btn = self.get_top_one_phone_btn(name)
        self.scroll_into_element(phone_btn)
        phone_btn.click()

    def get_top_one_visit_website_btn(self, name):
        try:
            return WebDriverWait(self.driver, WAIT).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//tbody/tr[1]//a[contains(@data-campaign,'"
                               + name + "')][contains(text(),'VISIT')] | "
                               "//tbody/tr[1]//a[contains(@data-campaign,'"
                               + name + "')][contains(text(),'LEARN MORE')]")))
        except WebDriverException:
            return None

    def click_top_one_visit_website_btn(self, name):
        visit_btn = self.get_top_one_visit_website_btn(name)
        self.scroll_into_element(visit_btn)
        visit_btn.click()

    def get_read_more_btn_pos1(self):
        return WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located((tuple(self.read_more_btn_pos1))))

    def click_read_more_btn_pos1(self):
        read_more_btn = self.get_read_more_btn_pos1()
        self.scroll_into_element(read_more_btn)
        read_more_btn.click()

    def get_brand_info_pos_1(self, name):
        try:
            return WebDriverWait(self.driver, WAIT).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[contains(@data-campaign,'" + name +
                               "')][contains(text(),'VIEW ALL PLANS')]|"
                               "//tr[2]/td[2]/a[contains(@data-campaign,'"
                               + name + "')][contains(text(),'VISIT')]|"
                               "//a[contains(@data-campaign,'" + name +
                               "')][contains(text(),'SCHEDULE')]")))
        except WebDriverException:
            return None

    # Top 2 position ------------------------------------------------------
    def get_top_two_position(self, brand):
        WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located((tuple(self.top_2))))
        return self.driver.find_element(
            By.XPATH, "//tbody/tr[2]//div[contains(text(),'" + brand + "')]")

    def get_top_two_image(self, name):
        return WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located(
                (By.XPATH, "//tr[2]/td[1]/img[@src][contains(@alt,'"
                           + name + "')]")))

    def get_top_two_stars(self):
        return WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located((tuple(self.stars_pos_2))))

    def get_top_two_phone_btn(self, name):
        try:
            return WebDriverWait(self.driver, WAIT).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//tbody/tr[2]//a[contains(@data-campaign,'"
                               + name + "')][contains(@href,'tel')]")))
        except WebDriverException:
            return None

    def click_top_two_phone_btn(self, name):
        phone_btn = self.get_top_two_phone_btn(name)
        self.scroll_into_element(phone_btn)
        phone_btn.click()

    def get_top_two_visit_website_btn(self, name):
        try:
            return WebDriverWait(self.driver, WAIT).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//tbody/tr[2]//a[contains(@data-campaign,'"
                               + name + "')][contains(text(),'VISIT')] | "
                               "//tbody/tr[2]//a[contains(@data-campaign,'"
                               + name + "')][contains(text(),'LEARN MORE')]")))
        except WebDriverException:
            return None

    def click_top_two_visit_website_btn(self, name):
        visit_btn = self.get_top_two_visit_website_btn(name)
        self.scroll_into_element(visit_btn)
        time.sleep(1)
        visit_btn.click()

    def get_read_more_btn_pos2(self):
        return WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located((tuple(self.read_more_btn_pos2))))

    def click_read_more_btn_pos2(self):
        read_more_btn = self.get_read_more_btn_pos2()
        self.scroll_into_element(read_more_btn)
        read_more_btn.click()

    def get_brand_info_pos_2(self, name):
        try:
            return WebDriverWait(self.driver, WAIT).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[contains(@data-campaign,'" + name +
                               "')][contains(text(),'VIEW ALL PLANS')]|"
                               "//tr[4]/td[2]/a[contains(@data-campaign,'"
                               + name + "')][contains(text(),'VISIT')]|"
                               "//a[contains(@data-campaign,'" + name +
                               "')][contains(text(),'SCHEDULE')]")))
        except WebDriverException:
            return None

    # Top 3 position ------------------------------------------------------
    def get_top_three_position(self, brand):
        WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located((tuple(self.top_2))))
        return self.driver.find_element(
            By.XPATH, "//tbody/tr[3]//div[contains(text(),'" + brand + "')]")

    def get_top_three_image(self, name):
        return WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located(
                (By.XPATH, "//tr[3]/td[1]/img[@src][contains(@alt,'"
                           + name + "')]")))

    def get_top_three_stars(self):
        return WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located((tuple(self.stars_pos_3))))

    def get_top_three_phone_btn(self, name):
        try:
            return WebDriverWait(self.driver, WAIT).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//tbody/tr[3]//a[contains(@data-campaign,'"
                               + name + "')][contains(@href,'tel')]")))
        except WebDriverException:
            return None

    def click_top_three_phone_btn(self, name):
        phone_btn = self.get_top_three_phone_btn(name)
        self.scroll_into_element(phone_btn)
        time.sleep(2)
        phone_btn.click()

    def get_top_three_visit_website_btn(self, name):
        try:
            return WebDriverWait(self.driver, WAIT).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//tbody/tr[3]//a[contains(@data-campaign,'"
                               + name + "')][contains(text(),'VISIT')] | "
                               "//tbody/tr[3]//a[contains(@data-campaign,'"
                               + name + "')][contains(text(),'LEARN MORE')]")))
        except WebDriverException:
            return None

    def click_top_three_visit_website_btn(self, name):
        visit_btn = self.get_top_three_visit_website_btn(name)
        self.scroll_into_element(visit_btn)
        visit_btn.click()

    def get_read_more_btn_pos3(self):
        return WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located((tuple(self.read_more_btn_pos3))))

    def click_read_more_btn_pos3(self):
        read_more_btn = self.get_read_more_btn_pos3()
        self.scroll_into_element(read_more_btn)
        read_more_btn.click()

    def get_brand_info_pos_3(self, name):
        try:
            return WebDriverWait(self.driver, WAIT).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[contains(@data-campaign,'" + name +
                               "')][contains(text(),'VIEW ALL PLANS')]|"
                               "//tr[6]/td[2]/a[contains(@data-campaign,'"
                               + name + "')][contains(text(),'VISIT')]|"
                               "//a[contains(@data-campaign,'" + name +
                               "')][contains(text(),'SCHEDULE')]")))
        except WebDriverException:
            return None

    # PPC banner ------------------------------------------------------
    def get_ppc_banner(self):
        return WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located((tuple(self.ppc_banner))))

    def get_ppc_banner_image(self, name):
        return WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[3]/img[@src][contains(@alt,'"
                           + name + "')]")))

    def get_ppc_banner_stars(self):
        return WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located((tuple(self.ppc_banner_stars))))

    def get_ppc_banner_phone_btn(self, name):
        try:
            return WebDriverWait(self.driver, WAIT).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[4]/a[contains(@data-campaign,'" + name +
                               "')][contains(@href,'tel')]")))
        except WebDriverException:
            return None

    def click_ppc_banner_phone_btn(self, name):
        phone_btn = self.get_ppc_banner_phone_btn(name)
        self.scroll_into_element(phone_btn)
        time.sleep(2)
        phone_btn.click()

    def get_ppc_banner_visit_website_btn(self, name):
        try:
            return WebDriverWait(self.driver, WAIT).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[4]/a[contains(@data-campaign,'" + name +
                               "')][contains(text(),'Visit')] |"
                               "//div[4]/a[contains(@data-campaign,'" + name +
                               "')][contains(text(),'VISIT')]")))
        except WebDriverException:
            return None

    def click_ppc_banner_visit_website_btn(self, name):
        visit_btn = self.get_ppc_banner_visit_website_btn(name)
        self.scroll_into_element(visit_btn)
        visit_btn.click()
