from selenium import webdriver
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import logging
logging.basicConfig(filename='D:/sanath/testingpost/test.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')

driver=webdriver.Chrome(executable_path='C:\Program Files (x86)\chromedriver.exe')
logging.debug(driver.get('https://www.atg.party/'))
driver.find_element_by_xpath('/html/body/header/div[1]/div[2]/div/ul/li[2]/a').click()
driver.find_element_by_xpath('//*[@id="email"]').send_keys(' wiz_saurabh@rediffmail.com')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('Pass@123')
driver.find_element_by_xpath('//*[@id="frm_landing_page_user_login"]/div[3]/button').click()
element=WebDriverWait(driver,10).until(Ec.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[3]/div[2]/a[1]')))
element.click()
nxt = WebDriverWait(driver, 10).until(Ec.presence_of_element_located((By.XPATH, '//*[@id="blog-landing"]/article[4]/div/div[2]/div[1]/a')))
nxt.click()
driver.find_element_by_xpath('//*[@id="create-btn-dropdown"]').click()
driver.find_element_by_xpath('/html/body/div[2]/div[1]/nav/div/div[3]/div/div[1]/div/div/a[1]').click()
driver.find_element_by_id('title').send_keys('testing post')
#upload=WebDriverWait(driver,10).until(Ec.visibility_of_element_located((By.XPATH,'//*[@type="file"]')))
driver.find_element_by_xpath('//input[@type="file"]').send_keys('D:/sanath/testingpost/FAST.png')
#upload.send_keys('D:/sanath-(college)/api testing internship/1095')
time.sleep(10)
driver.find_element_by_xpath('//*[@id="hpost_btn"]').click()
print(driver.current_url)
logging.debug((driver.current_url))
