import json
from selenium import webdriver
from qa_automation.qa_settings import (
    WAIT,
    DEFAULT_BROWSER_NAME,
    BS_COMMAND_EXECUTOR,
    BS_VIDEO,
    BS_SSLCERTS,
    BS_PROJECT,
    BS_BUILD,
    BS_LOCALIDENTIFIER,
    BS_LOCAL,
    BS_USER,
    BS_KEY,
    BS_DEBUG,
    # BS_NETWORKLOGS,
)
import requests
from django.conf import settings
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import qa_automation.tools.bs_browser_caps as bs_cap
from qa_automation.qa_settings import BASE_URL


class WebDriverFactory:

    def __init__(self, browser_name, on_localhost):
        self.browser_name = browser_name
        self.mobile = False
        self.driver = None
        self.on_localhost = on_localhost
        self.test_name = ""
        self.bs_test_name = ""

    def get_web_driver(self):
        if self.driver is not None:
            return self.driver
        elif self.on_localhost:
            if self.browser_name is not None and str.lower(
                    self.browser_name) == 'iexplorer':
                # TODO: Set ie driver
                self.driver = webdriver.Ie()
            elif self.browser_name is not None and str.lower(
                    self.browser_name) == 'firefox':
                self.driver = webdriver.Firefox()
            elif self.browser_name is not None and str.lower(
                    self.browser_name) == 'safari':
                # Set safari driver
                self.driver = webdriver.Safari()
            elif self.browser_name is not None and str.lower(
                    self.browser_name) == 'chrome':
                """
                Set chrome driver, iexplorer and others
                For example:
                chromedriver = "C:/.../chromedriver.exe"
                os.environ["webdriver.chrome.driver"] = chromedriver
                self.driver = webdriver.Chrome(chromedriver)
                """
                # TODO: Set chrome driver
                self.driver = webdriver.Chrome()
            else:
                self.driver = WebDriverFactory(
                    DEFAULT_BROWSER_NAME,
                    on_localhost=True).get_web_driver()

            self.driver.implicitly_wait(WAIT)
            self.driver.maximize_window()

            return self.driver
        elif self.browser_name in bs_cap.DESIRED_CAP:
            return self.get_bs_web_driver()
        else:
            return None

    def get_bs_web_driver(self):
        desired_cap = bs_cap.DESIRED_CAP[self.browser_name]
        if (('platform' in desired_cap) and
                (desired_cap['platform'] in ['ANDROID', 'MAC'])):
            self.mobile = True
        desired_cap['browserstack.local'] = BS_LOCAL

        if BASE_URL in 'http://localhost':
            pass
        else:
            desired_cap['browserstack.localIdentifier'] = BS_LOCALIDENTIFIER

        desired_cap['build'] = BS_BUILD
        desired_cap['project'] = BS_PROJECT
        desired_cap['acceptSslCerts'] = BS_SSLCERTS
        desired_cap['browserstack.video'] = BS_VIDEO
        desired_cap['browserstack.debug'] = BS_DEBUG
        desired_cap['name'] = self.bs_test_name[:254]
        # desired_cap['browserstack.networkLogs'] = BS_NETWORKLOGS

        self.driver = webdriver.Remote(
            command_executor=BS_COMMAND_EXECUTOR,
            desired_capabilities=desired_cap)

        self.driver.implicitly_wait(WAIT)

        return self.driver

    def hide_debug_toolbar(self):
        """
        If visible, debug toolbar may cover links on mobile devices
        """
        if (settings.DEBUG is False or 'debug_toolbar' not in settings
                .LOCAL_INSTALLED_APPS):
            return

        dr = self.get_web_driver()

        try:
            # TODO fix this, cause some time it is now closed!!!
            WebDriverWait(dr, WAIT).until(
                EC.visibility_of_element_located(
                    (By.ID, "djHideToolBarButton"))
            )
            dr.find_element(By.ID, "djHideToolBarButton").click()
            WebDriverWait(dr, WAIT).until(
                EC.invisibility_of_element_located(
                    (By.ID, "djDebugToolbar"))
            )
        except Exception:
            # no debug toolbar
            pass

    def get_bs_session_url(self):
        response = requests.get(
            'https://' + BS_USER + ':' + BS_KEY +
            '@api.browserstack.com/automate/sessions/'+str(
                self.driver.session_id)+'.json')
        try:
            parsed = json.loads(response.text)
            bs_session_url = parsed['automation_session']['browser_url']
        except Exception:
            return "Something wrong"
        return bs_session_url

    def failed_result(self):
        if self.get_web_driver() is not None:
            requests.put(
                'https://' + BS_USER + ':' + BS_KEY +
                '@www.browserstack.com/automate/sessions/'+str(
                    self.driver.session_id)+'.json',
                data={"status": "failed", "reason": ""})

    def passed_result(self):
        if self.get_web_driver() is not None:
            requests.put(
                'https://' + BS_USER + ':' + BS_KEY +
                '@www.browserstack.com/automate/sessions/'+str(
                    self.driver.session_id)+'.json',
                data={"status": "passed", "reason": ""})
