from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
from time import sleep
import pandas as pd
import getpass

eng1 = '33214109'

# задаю настройки браузера
username = getpass.getuser()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'user-data-dir=C:/Users/{username}/AppData/Local/Google/Chrome/User Data')

# открываю окно браузера
browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()  # разворачиваю окно во весь экран
browser.get('https://parts.cummins.com/esn-entry/main')  # открываю сайт
window_bef = browser.window_handles[0]  # настройка для открытия в то же окне браузера
sleep(2)
browser.find_element(By.XPATH,
                     '//*[@id="app-section"]/my-app/header/div[2]/div/div[1]/nav/ul/li[3]/a').click()
sleep(1)
browser.find_element(By.XPATH,
                     '//*[@id="app-section"]/my-app/header/div[2]/div/div[1]/nav/ul/li[3]/ul/li[1]/a').click()
# ищу окно поиска, вставляю туда серийник
browser.find_element(By.XPATH, '//*[@id="ebuSearchForm"]/div/input').send_keys(eng1)
pyautogui.hotkey('enter')  # нажимаю Enter
sleep(6)
# вторая попытка
browser.find_element(By.XPATH, '//*[@id="ebuSearchForm"]/div/input').send_keys(eng1)
pyautogui.hotkey('enter')  # нажимаю Enter
sleep(6)
browser.find_element(By.XPATH,
                     '//*[@id="app-section"]/my-app/leftnav/article/div/div[2]/section/div[2]/div/div/ng-component'
                     '/div/div[2]/span/span/div/div/div[3]/div/div/div/div/h4/div/span/a').click()
sleep(6)
browser.find_element(By.XPATH,
                     '//*[@id="app-section"]/my-app/leftnav/article/div/aside/section/tree-node[2]/div/div[1]').click()
sleep(6)

options = []
searchin = browser.find_elements(By.TAG_NAME, 'a')
for e in searchin:
    if '-' in e.text:
        options.append(e.text)
print(options)

data_list = []

for k in range(1, len(options)+1):
    elem = options[k-1]
    browser.find_element(By.XPATH, f'//*[@id="app-section"]/my-app/leftnav/article/div/div[2]/section/div[2]/div/div/'
                                   f'optionview/div[1]/div/div/div[2]/p-datatable1/div/div[2]/table/tbody/tr[{k}]/'
                                   f'td[1]/span/link-wrapper/a/span').click()
    sleep(3)
    for j in range(1, 120):
        try:
            part_number = browser.find_element(By.XPATH,
                                               f'//*[@id="app-section"]/my-app/leftnav/article/div/div[2]/section/div'
                                               f'[2]/div/div/optiondetail/section/div[2]/div/span/div/div/div[2]/p-tr'
                                               f'eetable-custom/div/div/table/tbody[{j}]/div/td[4]/a[2]')
            part_name = browser.find_element(By.XPATH,
                                             f'//*[@id="app-section"]/my-app/leftnav/article/div/div[2]/section/div[2]'
                                             f'/div/div/optiondetail/section/div[2]/div/span/div/div/div[2]/p-treet'
                                             f'able-custom/div/div/table/tbody[{j}]/div/td[6]/span/span')
            qty = browser.find_element(By.XPATH,
                                       f'//*[@id="app-section"]/my-app/leftnav/article/div/div[2]/section/div[2]/div'
                                       f'/div/optiondetail/section/div[2]/div/span/div/div/div[2]/p-treetable-custom'
                                       f'/div/div/table/tbody[{j}]/div/td[7]/span')
            data_list.append({
                'elem': elem,
                'part-number': part_number.text,
                'part-name': part_name.text,
                'qty': qty.text,
            })
        except Exception as e:
            continue


    print(f'Опция {elem} сохранена...')
    browser.execute_script("window.history.go(-1)")
    sleep(2)

df_eng1 = pd.DataFrame(data_list)
df_eng1.to_excel('output_data.xlsx', index=False, columns=['elem', 'part-number', 'part-name', 'qty'])
