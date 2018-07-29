import django
from random import randint
from qa_automation.qa_settings import BASE_URL as URL
import requests
from qa_automation.tools.webdriverwait import WebDriverWait
from qa_automation.qa_settings import WAIT
from datetime import date
from datetime import timedelta


def django_setup():
    django.setup()


"""
Auxiliary Steps
"""


def wait_for_complete(driver):
    WebDriverWait(driver, WAIT).until(
        lambda driver: driver.execute_script(
            "return document.readyState") == "complete")


def is_page_loaded(driver, page):
    wait_for_complete(driver)
    error_msg = "Page not loaded"
    assert page.get_body() is not None, error_msg


# to generate dates from the execution day spaced by 'delta' days
def generate_pickup_date(delta):
    pickup_date = date.now() + timedelta(days=delta)
    return pickup_date


def generate_dropoff_date(delta):
    dropoff_date = date.now() + timedelta(days=delta+2)
    return dropoff_date
