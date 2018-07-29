import os
import time

# selenium
DEFAULT_BROWSER_NAME = 'chrome'
WAIT = 30
BASE_URL = 'https://www.kayak.com'

# Selenium BS BROWSERS
DEVICES = ['WinChrome']

# browserstack
BS_USER = 'bnestico@hotmail.com'
BS_KEY = 'pM2yRtPgWAxM1uyMBKps'
# '4F8bifrP#QJM'
BS_COMMAND_EXECUTOR = 'http://' + BS_USER + ':' +\
                      BS_KEY + '@hub.browserstack.com:80/wd/hub'
BS_VIDEO = True
BS_SSLCERTS = True
BS_PROJECT = BASE_URL
BS_BUILD = "Kayak_"+str(os.getppid())+time.strftime("_%d.%m.%Y_%H")
BS_LOCAL = True
BS_DEBUG = True
BS_LOCALIDENTIFIER = BASE_URL[8:]
GRID_COMMAND_EXECUTOR = 'http://selenium-hub:4444/wd/hub'

# Env
os.environ["PYTHONWARNINGS"] = "ignore"
