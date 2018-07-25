# -*- coding: utf-8 -*-
"""
Base class for the base of all pages, for all screen resolutions.
"""

import time
from qa_automation.base.base import Base
from qa_automation.qa_settings import WAIT
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CategoryList(Base):
    """
    Locators:
    """
    body = (By.CSS_SELECTOR, "[class='main-cnt__col h-coll-vert tpc-nav']")
    categories = (By.XPATH, "//a[@class='ca-a tpc-nav__item']")

    """
    Methods:
    """

    def get_partner_city_name(self, city):
        return WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located(
                (By.XPATH, "//h1[contains(text(),'" + city +
                           "’s Best Companies')]")))

    def get_all_categories(self):
        return WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_all_elements_located((tuple(self.categories))))

    def count_categories(self):
        found = self.get_all_categories()
        categories_found = len(found)
        return categories_found

    def get_category(self, cat_name):
        return WebDriverWait(self.driver, WAIT).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[@class='ca-a tpc-nav__item']"
                           "//span[contains(text(),'" + cat_name + "')]")))

    def click_on_category(self, cat_name):
        category = self.get_category(cat_name)
        self.scroll_into_element(category)
        time.sleep(1)
        category.click()
