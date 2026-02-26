from selenium import webdriver
import numpy as np
import pandas as pd
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

for i in range(10):
    driver = webdriver.Chrome()
    driver.get(f'https://www.heritage.go.kr/heri/cul/culSelectViewList.do?gbn=2&pageNo=1_1_0_0&ccbaCndt=&region=1&searchCondition=&s_kdcdArr=00&s_ctcdArr=00&ccbaPcd1Arr=99&stCcbaAsdt=&endCcbaAsdt=&ccbaGcodeArr=00')
    element = driver.find_element(By.CSS_SELECTOR, "a#thumbnail")
    element.click()