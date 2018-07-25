import os
import time

# selenium
DEFAULT_BROWSER_NAME = 'chrome'
WAIT = 30
BASE_URL = 'https://reviews.'

# Selenium BS BROWSERS
DEVICES = ['WinChrome']

# browserstack
BS_USER = 'caqa1'
BS_KEY = 'hNLe27jcLtsKVQRuT436'
BS_COMMAND_EXECUTOR = 'http://' + BS_USER + ':' +\
                      BS_KEY + '@hub.browserstack.com:80/wd/hub'
BS_VIDEO = True
BS_SSLCERTS = True
BS_PROJECT = BASE_URL
BS_BUILD = "CA_"+str(os.getppid())+time.strftime("_%d.%m.%Y_%H")
BS_LOCAL = True
BS_DEBUG = True
BS_LOCALIDENTIFIER = BASE_URL[8:]
# BS_NETWORKLOGS = True  # reason of errors as BS support say
GRID_COMMAND_EXECUTOR = 'http://selenium-hub:4444/wd/hub'

# Env
os.environ["PYTHONWARNINGS"] = "ignore"

# Social Media connectors
QA_FB_LOGIN_TOKEN = '150298645070242|rYmENLwbuRedMdVUyDhKWms_Wio'
FB_LOGIN_APP_ID = '150298645070242'
FB_API_HOST = 'https://graph.facebook.com/v2.11/{}'
FB_CREATE_USER = '/accounts/test-users'

TEST_RAIL = True
TEST_RAIL_URL = 'https://consumeraffairs.testrail.com/index.php?/api/v2'
TEST_RAIL_USER = 'malzua@consumeraffairs.com'
TEST_RAIL_KEY = 'AUbdGW832ByX3I295uua-33JSaPVU1KcrdZp84o81'
TEST_RAIL_PROJECT = 8
TEST_RAIL_SUITE_ID = 52
