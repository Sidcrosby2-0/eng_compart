import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui


def clicker(link):
    browser.find_element(By.XPATH, link).click()
    time.sleep(10)


# eng_1 = input("Первый двигатель: ")
# eng_2 = input("Второй двигатель: ")
eng_1 = '33221841'

browser = webdriver.Chrome()
browser.get('https://parts.cummins.com/home')
window_before = browser.window_handles[0]

# закрываем окно cookies
try:
    time.sleep(5)
    cook = '//*[@id="onetrust-accept-btn-handler"]'
    browser.find_element(By.XPATH, cook).click()
    time.sleep(5)
except:
    time.sleep(5)
try:
    browser.find_element(By.XPATH, '//*[@id="app-section"]/my-app/cookie-popup/div/div/button').click()
except:
    time.sleep(2)

serial_number = 'criteria'
browser.find_element(By.ID, serial_number).send_keys(eng_1)
time.sleep(1)
pyautogui.hotkey('enter')
time.sleep(10)

clicker(
    '//*[@id="app-section"]/my-app/ng-component/div/div[2]/span/span[2]/div/div/div[3]/div/div/div/div/h4/div/span/a'
)
clicker('//*[@id="app-section"]/my-app/leftnav/article/div/aside/section/tree-node[2]/div/div[1]/span/span')

time.sleep(10)

