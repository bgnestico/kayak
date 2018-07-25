import django
from random import randint
from qa_automation.qa_settings import BASE_URL as URL
import requests
from qa_automation.tools.webdriverwait import WebDriverWait
from qa_automation.qa_settings import WAIT


def django_setup():
    django.setup()


"""
Auxiliary Steps
"""


def get_random(start, end):
    return randint(start, end)


def get_console_messages(driver):
    return driver.get_log('browser')


def get_page_status(url):
    return requests.get(URL + url).status_code


def check_status_code(url, status_code):
    response = requests.get(URL + url,
                            timeout=REQUEST_TIMEOUT['DEFAULT'])
    assert response.status_code == status_code, "Page not loaded"
    return response


def wait_for_complete(driver):
    WebDriverWait(driver, WAIT).until(
        lambda driver: driver.execute_script(
            "return document.readyState") == "complete")


def is_page_loaded(driver, page):
    wait_for_complete(driver)
    error_msg = "Page not loaded"
    assert page.get_body() is not None, error_msg


# timeout for requests, in seconds
REQUEST_TIMEOUT = {
    'ANALYTICS_OPTIMIZELY': 5,
    'API_VIEWS_ALPHA_DATA': 300,
    'API_VIEWS_VALIDATORS': 5,
    'BRANDS_CLIENT': 60,
    'BRANDS_DISTRIBUTION': 10,
    'DEFAULT': 30,
    'LEADS_CONVERSION': 60,
    'LEADS_RESEND': 3.05,
    'MATCHINGTOOL_API': 3.05,
    'RECAPTCHA': 1,
    'SALESFORCE': 6000,
    'EMPATHIQ': 5,
}
