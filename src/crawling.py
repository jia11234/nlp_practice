from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import numpy as np
import pandas as pd

import pandas as pd

treasure_df = pd.read_csv('./data/heritage_search_list.csv')
treasure_df2 = pd.read_csv('./data/heritage_exp.csv')
treasure_df['exp'] = treasure_df2['exp']

driver = webdriver.Chrome() 
actions = ActionChains(driver)
j=0
for i in range(819,len(treasure_df)):
    try:
        if(j==5):
            treasure_df.to_csv('./data/heritage_exp.csv', index=False)
            j=0
        driver.get('https://www.heritage.go.kr/heri/cul/culSelectView.do?pageNo=1_1_0_0')
        driver.find_element(By.CSS_SELECTOR, "#searchCondition").send_keys(treasure_df['title'].iloc[i])
        driver.find_element(By.CSS_SELECTOR, ".sch-input button").click()
        time.sleep(0.2)
        element = driver.find_element(By.CSS_SELECTOR, "ul.board-list > li > a")
        actions.move_to_element(element).perform()
        element.click()
        time.sleep(0.2)
        element_text = driver.find_element(By.CSS_SELECTOR, "p.hide_exp.krExp")
        time.sleep(0.2)
        actions.move_to_element(element_text).perform()
        treasure_df.loc[i, 'exp'] = element_text.text
        time.sleep(0.5)
        j+=1
    except Exception as e:
        print(f"index {i} 오류!!!!{e}")
        continue

treasure_df.to_csv('./data/heritage_exp.csv', index=False)