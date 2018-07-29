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


class Cars(Base):
    url = '/cars/'

    """
    Locators:
    """
    # search section elements --------------------------------------------
    dropoff_menu = (By.XPATH, "//div[contains(@class,'returningUser')]"
                              "//*[contains(@id,'switch-display')]"
                              "[contains(@class,'_ew')]")
    same_dropoff = (By.XPATH, "//*[contains(@id,'switch-option-1')]")
    different_dropoff = (By.XPATH, "//*[contains(@id,'switch-option-2')]")

    # pickup_location elements are used for same_dropoff option ----------
    pickup_location_display = (By.XPATH, "//*[contains(@id,'pickup')]"
                                         "[contains(@class,'_bq7')]")
    pickup_location_input = (By.XPATH, "//*[@name='pickup']")
    dropoff_location_display = (By.XPATH, "//*[contains(@id,'dropoff')]"
                                          "[contains(@class,'_bq7')]")
    dropoff_location_input = (By.XPATH, "//*[@name='dropoff']")

    dateRange_display = (By.XPATH, "//div[contains(@class,'returningUser')]"
                                   "//*[contains(@id,'RangeInput')]"
                                   "[contains(@class,'DateModal')]")
    pickup_date_input = (By.XPATH, "//*[contains(@id,'pickup-date-input')]")
    dropoff_date_input = (By.XPATH, "//*[contains(@id,'dropoff-date-input')]")

    search_btn = (By.XPATH, "//*[contains(@class,'searchBtn')]")

    # results section elements --------------------------------------------
    sortBy_display = (By.XPATH, "//*[contains(@class,'sortBy')]")
    sortBy_price_low = (By.XPATH, "//*[contains(@id,'sorting-option-2')]")
    results = (By.XPATH, "//*[contains(@class,'js-result')]")

    first_price_pos = (By.XPATH, "//div[2]/div[1]/div[2]/div[1]/div[1]"
                                 "[@class='_uZ _eP']")

    """
    Methods:
    """
    # dropoff options -------------------------------------------------
    def get_dropoff_menu(self):
        try:
            return WebDriverWait(self.driver, WAIT).until(
                EC.element_to_be_clickable((tuple(self.dropoff_menu))))
        except WebDriverException:
            return None

    def click_dropoff_menu(self):
        self.get_dropoff_menu().click()

    def get_same_dropoff(self):
        try:
            return WebDriverWait(self.driver, WAIT).until(
                EC.element_to_be_clickable((tuple(self.same_dropoff))))
        except WebDriverException:
            return None

    def click_same_dropoff(self):
        self.get_same_dropoff().click()

    def get_different_dropoff(self):
        try:
            return WebDriverWait(self.driver, WAIT).until(
                EC.element_to_be_clickable((tuple(self.different_dropoff))))
        except WebDriverException:
            return None

    def click_different_dropoff(self):
        self.get_different_dropoff().click()

    # pickup and dropoff locations ----------------------------------
    def get_pickup_location_display(self):
        try:
            return WebDriverWait(self.driver, WAIT).until(
                EC.element_to_be_clickable(
                (tuple(self.pickup_location_display))))
        except WebDriverException:
            return None

    def click_pickup_location_display(self):
        self.get_pickup_location_display().click()

    def get_pickup_location_input(self):
        try:
            return WebDriverWait(self.driver, WAIT).until(
                EC.element_to_be_clickable(
                (tuple(self.pickup_location_input))))
        except WebDriverException:
            return None

    def enter_pickup_location(self, location_data):
        self.get_pickup_location_input().clear()
        self.get_pickup_location_input().send_keys(location_data)
        self.get_pickup_location_input().send_keys(u'\ue007')

    def get_dropoff_location_display(self):
        try:
            return WebDriverWait(self.driver, WAIT).until(
                EC.element_to_be_clickable(
                (tuple(self.dropoff_location_display))))
        except WebDriverException:
            return None

    def click_dropoff_location_display(self):
        self.get_dropoff_location_display().click()

    def get_dropoff_location_input(self):
        try:
            return WebDriverWait(self.driver, WAIT).until(
                EC.element_to_be_clickable(
                (tuple(self.dropoff_location_input))))
        except WebDriverException:
            return None

    def enter_dropoff_location(self, location_data):
        self.get_dropoff_location_input().clear()
        self.get_dropoff_location_input().send_keys(location_data)
        self.get_dropoff_location_input().send_keys(u'\ue007')

    # pickup and dropoff date range -----------------------------------
    def get_dateRange_display(self):
        try:
            return WebDriverWait(self.driver, WAIT).until(
                EC.element_to_be_clickable((tuple(self.dateRange_display))))
        except WebDriverException:
            return None

    def click_dateRange_display(self):
        self.get_dateRange_display().click()

    def get_pickup_date_input(self):
        try:
            return WebDriverWait(self.driver, WAIT).until(
                EC.element_to_be_clickable((tuple(self.pickup_date_input))))
        except WebDriverException:
            return None

    def get_dropoff_date_input(self):
        try:
            return WebDriverWait(self.driver, WAIT).until(
                EC.element_to_be_clickable((tuple(self.dropoff_date_input))))
        except WebDriverException:
            return None

    def enter_dateRange(self, pickup_date, dropoff_date):
        self.get_pickup_date_input().clear()
        self.get_pickup_date_input().send_keys(pickup_date)
        self.get_pickup_date_input().send_keys(u'\ue007')
        self.get_dropoff_date_input().clear()
        self.get_dropoff_date_input().send_keys(dropoff_date)
        self.get_dropoff_date_input().send_keys(u'\ue007')

    # search button ------------------------------------------------
    def get_search_btn(self):
        try:
            return WebDriverWait(self.driver, WAIT).until(
                EC.element_to_be_clickable((tuple(self.search_btn))))
        except WebDriverException:
            return None

    def click_search_btn(self):
        self.get_search_btn().click()

    # results loaded section ---------------------------------------
    def get_first_price_pos(self):
        try:
            return WebDriverWait(self.driver, WAIT).until(
                EC.presence_of_element_located((tuple(self.first_price_pos))))
        except WebDriverException:
            return None

    def get_first_price_value(self):
        return self.get_first_price_pos().get_attribute("value")
