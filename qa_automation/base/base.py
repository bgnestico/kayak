"""
Base class for the base of all pages, for all screen resolutions.
"""
import pytest
import requests
import json
import time
from qa_automation.qa_settings import (WAIT, BASE_URL, BS_USER, BS_KEY)
from qa_automation.tools.webdriverwait import WebDriverWait
from qa_automation.tools.steps_helper import wait_for_complete
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Base(object):
    main_window = ''
    test_name = ''

    def __init__(self, setup):
        self.driver = setup.get_web_driver()
        self.mobile = setup.mobile
        self.test_name = setup.test_name

    def get_page(self, url="", base=BASE_URL):

        try:
            self.driver.get(base + url)

        except WebDriverException as e:
            if 'unknown server-side error' in str(e):
                self.driver.get(base + url)
                pass

            elif 'Unable to communicate to node' in str(e):

                # Rerun the correct test again
                args_str = ["-v", "-s", self.test_name[:len(
                    self.test_name.split('[')[0])]]
                pytest.main(args_str)

                # Delete failed BS session
                s = 'https://' + BS_USER + ':' + BS_KEY + \
                    '@api.browserstack.com/automate/sessions/' + \
                    self.driver.session_id + '.json'
                self.driver.quit()
                r = requests.delete(s)
                try:
                    parsed = json.loads(r.text)
                    status = parsed['status']
                except Exception:
                    return "Statuserror:" + status

                pytest.skip("SUCCESSFUL rerun: {0}!".format(self.test_name))

            else:
                raise e

        if self.mobile is False:
            try:
                self.driver.maximize_window()
            except WebDriverException:
                pass

        wait_for_complete(self.driver)
        self.main_window = self.driver.current_window_handle

    def get_body(self):
        return WebDriverWait(self.driver, WAIT).until(
            EC.presence_of_element_located((tuple(self.body))))

    def scroll_down(self, px):
        self.driver.execute_script('window.scroll(0, {0});'.format(px))

    def scroll_into_element(self, element):
        self.driver.execute_script(
                        "arguments[0].scrollIntoView(false)", element)

    def moveover_element(self, element):
        self.scroll_into_element(element)
        ActionChains(self.driver).move_to_element(element).perform()

    def waiting_page_by_title(self, title):
        try:
            if 'safari' in str(self.get_browser_name()).lower():
                count = WAIT
                for num in range(int(count)):
                    flag = title in self.driver.execute_script(
                        "return document.title")
                    if not flag:
                        time.sleep(1)
                        continue
                    else:
                        break
            else:
                assert WebDriverWait(self.driver, WAIT).until(
                    lambda driver: title in driver.execute_script(
                        "return document.title"))
        except WebDriverException:
            pytest.fail("{} =/= {}".format(title, self.driver.title), True)

    def click_btn_by_class_name_script(self, name):
        self.driver.execute_script(
            'document.getElementsByClassName("{}")[0].click()'.format(name))

    def click_btn_by_id_script(self, element):
        self.driver.execute_script(
            'document.getElementById("{}").click()'.format(element[1]))

    def get_browser_name(self):
        return self.driver.capabilities['browserName']

    def get_browser_version(self):
        return self.driver.capabilities['version']

    def get_browser_os(self):
        return self.driver.capabilities['platform']

    def get_window_width(self):
        return self.driver.execute_script('return window.innerWidth')

    def switch_to_frame(self, frame):
        return self.driver.switch_to.frame(frame)

    def switch_to_active_tab(self):
        if len(self.driver.window_handles) > 1:
            return self.driver.switch_to.window(self.driver.window_handles[1])

    def jump_window(self, page_title=''):
        if not self.mobile:
            if page_title == '':
                WebDriverWait(self.driver, WAIT).until(
                    lambda h: len(self.driver.window_handles) == 1)
                self.driver.switch_to.window(self.main_window)
                wait_for_complete(self.driver)
            else:
                index = 0
                WebDriverWait(self.driver, WAIT).until(
                    lambda w: len(self.driver.window_handles) > 1)
                for x in self.driver.window_handles:
                    if x == self.main_window:
                        index = index + 1
                    else:
                        break
                sec_window = self.driver.window_handles[index]
                self.driver.switch_to.window(sec_window)
                WebDriverWait(self.driver, WAIT).until(
                    lambda x: self.driver.current_window_handle == sec_window)
                self.waiting_page_by_title(page_title)

    def get_screenshot(self):
        return self.driver.get_screenshot_as_base64()

    def refresh_page(self):
        return self.driver.refresh()
