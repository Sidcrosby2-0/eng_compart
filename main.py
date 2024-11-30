from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
from time import sleep
import pandas as pd


def options_list(serial):
    # открываю окно браузера
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()  # разворачиваю окно во весь экран
    driver.get('https://parts.cummins.com/esn-entry/main')  # открываю сайт
    window_before = driver.window_handles[0]  # настройка для открытия в то же окне браузера
    sleep(2)
    driver.find_element(By.XPATH,
                        '//*[@id="app-section"]/my-app/header/div[2]/div/div[1]/nav/ul/li[3]/a').click()
    sleep(1)
    driver.find_element(By.XPATH,
                        '//*[@id="app-section"]/my-app/header/div[2]/div/div[1]/nav/ul/li[3]/ul/li[1]/a').click()
    # ищу окно поиска, вставляю туда серийник
    driver.find_element(By.XPATH, '//*[@id="ebuSearchForm"]/div/input').send_keys(serial)
    pyautogui.hotkey('enter')  # нажимаю Enter
    sleep(6)
    # вторая попытка
    driver.find_element(By.XPATH, '//*[@id="ebuSearchForm"]/div/input').send_keys(serial)
    pyautogui.hotkey('enter')  # нажимаю Enter
    sleep(6)
    driver.find_element(By.XPATH,
                        '//*[@id="app-section"]/my-app/leftnav/article/div/div[2]/section/div[2]/div/div/ng-component'
                        '/div/div[2]/span/span/div/div/div[3]/div/div/div/div/h4/div').click()
    sleep(6)
    driver.find_element(By.XPATH,
                        '//*[@id="app-section"]/my-app/leftnav/article/div/aside/section/tree-node[2]/div').click()
    sleep(6)

    options = []
    searchin = driver.find_elements(By.TAG_NAME, 'a')
    for e in searchin:
        if '-' in e.text:
            options.append(e.text)
    print(options)
    return options


def option_list(opt):
    options = []
    for i in range(0, len(opt)):
        index = opt[i][0:2]
        options.append(index)
    return options


# eng1 = input('Введите двигатель 1: ')
# eng2 = input('Введите двигатель 2: ')
eng1 = '85009399'
eng2 = '85018026'

# создаю пустой датафрейм
df_eng1 = pd.DataFrame(columns=['option', 'part-number', 'part-name', 'qty'])

# задаю настройки браузера
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('user-data-dir=C:/Users/hatom/AppData/Local/Google/Chrome/User Data')
# chrome_options.add_argument('--headless=new')

engine1 = options_list(eng1)
engine2 = options_list(eng2)

engine1_unic = list(set(engine1) - set(engine2))
engine2_unic = list(set(engine2) - set(engine1))
engine1_unic.sort()
engine2_unic.sort()

print(f'Уникальные опции старого двигателя: {engine1_unic}')
print(f'Уникальные опции нового двигателя: {engine2_unic}')

options_old = option_list(engine1_unic)
options_new = option_list(engine2_unic)

# driver = webdriver.Chrome(options=chrome_options)
# driver.maximize_window()
# driver.get('https://parts.cummins.com/esn-entry/main')
# window_before = driver.window_handles[0]
# sleep(2)
# driver.find_element(By.XPATH,
#                     '//*[@id="app-section"]/my-app/header/div[2]/div/div[1]/nav/ul/li[3]/a').click()
# sleep(1)
# driver.find_element(By.XPATH,
#                     '//*[@id="app-section"]/my-app/header/div[2]/div/div[1]/nav/ul/li[3]/ul/li[1]/a').click()
# driver.find_element(By.XPATH, '//*[@id="ebuSearchForm"]/div/input').send_keys(eng1)
# pyautogui.hotkey('enter')
# sleep(6)
# driver.find_element(By.XPATH, '//*[@id="ebuSearchForm"]/div/input').send_keys(eng1)
# pyautogui.hotkey('enter')
# sleep(6)
# driver.find_element(By.XPATH,
#                     '//*[@id="app-section"]/my-app/leftnav/article/div/div[2]/section/div[2]/div/div/ng-component'
#                     '/div/div[2]/span/span/div/div/div[3]/div/div/div/div/h4/div').click()
# sleep(6)
# driver.find_element(By.XPATH,
#                     '//*[@id="app-section"]/my-app/leftnav/article/div/aside/section/tree-node[2]/div').click()
# sleep(6)
#
# for i in range(0, len(options_old)):
#     elem = options_old[i]
#     print(elem)
#     driver.find_element(By.XPATH, f"//*[contains(text(), '{elem}')]").click()
#     sleep(4)
#
#     driver.execute_script("window.history.go(-1)")
#     sleep(2)






