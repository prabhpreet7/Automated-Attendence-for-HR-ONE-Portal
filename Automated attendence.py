from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
import time
from datetime import datetime

'''Dates for which attendence has to be approved
or you can input dates form user'''
dates = ['09/11/2020' ,'10/11/2020', '11/11/2020', '12/11/2020', '13/11/2020']

res = input('Attendence for today (y or n) : ').lower()

'''if res=='y', attendence will be marked for today's date'''
if res=='y':
    dates = [datetime.strftime(datetime.now(),'%d/%m/%Y')]

'''download and install chrome driver'''
driver = webdriver.Chrome(executable_path='path to chrome driver executable or add it to python environment variables')

# driver.get('https://bluejayfinleaselimited.hrone.cloud/Account/Index')
driver.get('your HR-One portal link')
driver.find_element_by_id('UserName').send_keys('your id')
time.sleep(2)

while(True):
    try:
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID,"anchor66")))
        break
    except:
        driver.find_element_by_id('Password').send_keys('your passwrod')
        driver.find_element_by_id('Password').clear()
        driver.find_element_by_id('Password').send_keys('your password')
        driver.find_element_by_id('btnLogin').click()
        
try:
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID,"anchor66"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID,"anchor72"))).click()

    for date in dates:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT,"Apply New"))).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT,"On Duty"))).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,"//select[@name='ODTypeDDL']/option[text()='Client Visit']"))).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID,"odDate1"))).send_keys(date)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID,"txtOdRemark"))).send_keys('Work From Home')
        driver.find_element_by_id('btnOdSave').click()
        time.sleep(2)
        if "Request already exists" in driver.page_source:
            driver.find_element_by_id('btnOdClose').click()

except:
    driver.close()
    
finally:
    driver.close()