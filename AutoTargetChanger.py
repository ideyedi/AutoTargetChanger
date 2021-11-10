import time
import traceback
import os
#import numpy as np
#import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

path_project = os.getcwd()
WebDrv = 'chromedriver'

def InitializeDriver() -> int:
    print(path_project)

    return 0


InitializeDriver()
