import pytest
import qa_automation.qa_settings as qaset
from qa_automation.tools import webdriver_factory as wf
from qa_automation.qa_settings import BASE_URL
from selenium.common.exceptions import WebDriverException
from urllib.error import URLError


@pytest.yield_fixture(scope="function")
def setup(request, browser, on_localhost):
    if browser is None and hasattr(request, 'param'):
        browser = request.param
    """
    '--localhost True' or '--localhost true' to run on localhost is false
    remote WebDriver will be used.
    """
    on_localhost = qaset.BS_LOCAL = \
        on_localhost is not None and str.lower(on_localhost) == 'true'

    custom_web_driver = wf.WebDriverFactory(browser, on_localhost)

    if request.cls is not None:
        request.cls.custom_web_driver = custom_web_driver

    custom_web_driver.test_name = str(request.node.fspath) + '::' + str(
        request.node.name)
    custom_web_driver.bs_test_name = str(request.node.name)

    setup.a = custom_web_driver
    yield custom_web_driver

    if request.node.rep_call.failed \
            and custom_web_driver.get_web_driver() is not None:
        custom_web_driver.failed_result()
    else:
        custom_web_driver.passed_result()

    if custom_web_driver.driver is not None:
        try:
            custom_web_driver.driver.quit()
        except WebDriverException as e:
            if 'Session not started or terminated' in str(e):
                pass
            else:
                raise e
        except URLError as e:
            if 'urlopen error time out' in str(e):
                pass
            else:
                raise e


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--localhost", help="Execute tests on localhost")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def on_localhost(request):
    return request.config.getoption("--localhost")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    pytest_html = item.config.pluginmanager.getplugin('html')
    extra = getattr(rep, 'extra', [])
    if rep.when == 'call':
        xfail = hasattr(rep, 'wasxfail')
        try:
            extra.append(pytest_html.extras.url(setup.a.get_bs_session_url()))
        except AttributeError:
            extra.append(pytest_html.extras.url('Error! No a at setup object'))

        if (rep.skipped and xfail) or (rep.failed and not xfail):
            try:
                if setup.a.driver is not None:
                    try:
                        sc = str(setup.a.driver.get_screenshot_as_base64())
                    except Exception as e:
                        sc = "No screenshot! {}".format(e)
                        extra.append(pytest_html.extras.html(sc))
            except Exception as e:
                sc = "No screenshot! {}".format(e)
                extra.append(pytest_html.extras.html(sc))
        rep.extra = extra


def pytest_report_header():
    if BASE_URL in 'http://localhost':
        return "Local-identifier is not set on the " + BASE_URL + "."
    else:
        qaset.BS_LOCALIDENTIFIER
        return "Local-identifier: " + qaset.BS_LOCALIDENTIFIER + "."


def pytest_configure(config):
    if not hasattr(config, 'plan_name'):
        import datetime
        import time
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M')
        env = qaset.BS_LOCALIDENTIFIER
        config.plan_name = 'Automation ' + env + st


def pytest_configure_node(node):
    """xdist hook"""
    node.slaveinput['plan_name'] = node.config.plan_name
