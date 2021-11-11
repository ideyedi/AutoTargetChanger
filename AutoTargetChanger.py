import time
import traceback
import os
import csv
#import numpy as np
#import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

'''
path_project: project path
WebDrv: chrome web driver
JenkinsURL : Target URL address
'''
path_project = os.getcwd()
WebDrv = '/chromedriver'
JenkinsURL = 'http://wdeploy.wemakeprice.kr'

#print(path_project)

Options = webdriver.ChromeOptions()
Options.add_argument('--incognito')
drv = webdriver.Chrome(path_project + WebDrv, options=Options)

# Input tab which is ServiceName
# ServiceName = input('Input ServiceName : ')
ServiceName = 'nd-epes-api'

try:
    # Login process
    drv.get(JenkinsURL)
    # find_elements_by_id function is deprecated... 
    j_username = drv.find_elements_by_id('j_username')
    print(drv)
    j_username[0].send_keys('esji')

    j_password = drv.find_elements_by_name('j_password')
    #print(j_password)
    j_password[0].send_keys('eyedi318!')

    login_btn = drv.find_elements_by_class_name('submit-button')
    #print(login_btn)
    login_btn[0].click()


    # Search service name at production level
    main_search = drv.find_elements_by_class_name('main-search__input')
    main_search[0].send_keys(ServiceName)
    main_search[0].send_keys(Keys.RETURN)

    # Get li object
    get_li = drv.find_elements(By.TAG_NAME, 'li')
    #print(get_li, len(get_li))

    # Move to service jenkins job
    for item in get_li:
        #print(item.text)

        if 'PROD' in item.text:
            tmp = item.find_elements(By.TAG_NAME, 'a')
            tmp[0].click()
            break

    # Go to configuration 
    get_task = drv.find_elements(By.CLASS_NAME, 'task')
    for item in get_task:
        if 'Configure' in item.text:
            tmp = item.find_elements(By.TAG_NAME, 'a')
            tmp[0].click()
            break

    # Get TargetList
    tmp = drv.find_elements(By.CLASS_NAME, 'repeated-chunk')
    print(len(tmp))
    for item in tmp:
        get_td = item.find_elements(By.TAG_NAME, 'td')
        for td in get_td:
            if 'Name' in td.text:
                inputcnt = td.find_elements(By.TAG_NAME, 'input')
                print(len(inputcnt))
                #print(inputcnt[0].value)
                #if len()
                #'input_target_list' == td.find_elements(By.TAG_NAME, 'input')[0].value:
                #print('find it')
                
        #print(tdls)

except:
    traceback.print_exc()


