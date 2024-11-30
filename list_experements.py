from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
from time import sleep
import pandas as pd


eng1 = '85009399'
test_old = ['FF5133-00', 'SD5029-00', 'CS5050-00', 'GG5730-04', 'LA5005-02', 'CF5008-04', 'SC50441-01', 'PH5767-11',
            'DO5543-00', 'IT5025-00', 'WF5032-05', 'PH5798-16', 'TB5822-07', 'TP5726-10', 'FD5725-00', 'EH5717-02',
            'FP57001-00', 'AP5116-02', 'WI5064-01', 'FR5381-00', 'LG5715-01', 'TB5127-01', 'EM5083-01', 'SM5724-05',
            'OP5167-02', 'FCAB58-00', 'AD5115-02', 'PP42858-17', 'RL5703-06', 'EE5113-02', 'FS5043-00', 'EH5031-03',
            'PP5722-03', 'AP5705-03', 'EO5006-01', 'FH5048-05', 'LC5709-01', 'BB5714-26', 'LF5121-04']
test_new = ['EH5046-02', 'PH5767-14', 'CF5005-01', 'EE5095-01', 'EH5712-02', 'LG5705-04', 'PH5791-16', 'TB5766-10',
            'GG5730-05', 'SM5724-06', 'WF5701-03', 'XS5059-05', 'AP5139-02', 'FP57001-01', 'PP42852-18', 'OP5731-00',
            'LF5089-04', 'LA5003-03', 'FF5090-02', 'WI5064-02', 'IT5004-02', 'SD5077-00', 'FD5712-00', 'FR50057-00',
            'TP5726-12', 'AP5717-00', 'OP5147-08', 'FCAA41-00', 'LC5709-03', 'DO5382-00', 'TB5076-05', 'RD5002-01',
            'WF5034-04', 'RL5703-07', 'SC50277-00', 'AD5112-02', 'EM5083-02', 'FF5769-04', 'FH5049-06', 'PP5721-03',
            'LT5062-00', 'BB5714-27']

test_old.sort()
test_new.sort()

options_old = []
for i in range(0, len(test_old)):
    opt = test_old[i][0:2]
    options_old.append(opt)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('user-data-dir=C:/Users/hatom/AppData/Local/Google/Chrome/User Data')

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get('https://parts.cummins.com/esn-entry/main')
window_before = driver.window_handles[0]
sleep(2)
driver.find_element(By.XPATH,
                    '//*[@id="app-section"]/my-app/header/div[2]/div/div[1]/nav/ul/li[3]/a').click()
sleep(1)
driver.find_element(By.XPATH,
                    '//*[@id="app-section"]/my-app/header/div[2]/div/div[1]/nav/ul/li[3]/ul/li[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="ebuSearchForm"]/div/input').send_keys(eng1)
pyautogui.hotkey('enter')
sleep(6)
driver.find_element(By.XPATH, '//*[@id="ebuSearchForm"]/div/input').send_keys(eng1)
pyautogui.hotkey('enter')
sleep(6)
driver.find_element(By.XPATH,
                    '//*[@id="app-section"]/my-app/leftnav/article/div/div[2]/section/div[2]/div/div/ng-component'
                    '/div/div[2]/span/span/div/div/div[3]/div/div/div/div/h4/div').click()
sleep(6)
driver.find_element(By.XPATH,
                    '//*[@id="app-section"]/my-app/leftnav/article/div/aside/section/tree-node[2]/div').click()
sleep(6)

elem = test_old[0]
driver.find_element(By.XPATH, f"//*[contains(text(), '{elem}')]").click()
sleep(4)
dict1 = {}
part_numbers = []
part_names = []
qtys = []
for j in range(1, 120):
    try:
        part_number = driver.find_element(By.XPATH, f'//*[@id="app-section"]/my-app/leftnav/article/div/div[2]/section/div'
                                                    f'[2]/div/div/optiondetail/section/div[2]/div/span/div/div/div[2]/p-tr'
                                                    f'eetable-custom/div/div/table/tbody[{j}]/div/td[4]/a[2]')
        part_name = driver.find_element(By.XPATH, f'//*[@id="app-section"]/my-app/leftnav/article/div/div[2]/section/div[2]'
                                                  f'/div/div/optiondetail/section/div[2]/div/span/div/div/div[2]/p-treet'
                                                  f'able-custom/div/div/table/tbody[{j}]/div/td[6]/span/span')
        qty = driver.find_element(By.XPATH, f'//*[@id="app-section"]/my-app/leftnav/article/div/div[2]/section/div[2]/div'
                                            f'/div/optiondetail/section/div[2]/div/span/div/div/div[2]/p-treetable-custom'
                                            f'/div/div/table/tbody[{j}]/div/td[7]/span')
        part_numbers.append(part_number.text)
        part_names.append(part_name.text)
        qtys.append(qty.text)
    except:
        continue


dict1 = {'part-number': part_numbers,
         'part-name': part_names,
         'qty': qtys
         }

df_eng1 = pd.DataFrame(dict1)

print(f'Опция {elem} сохранена...')
driver.execute_script("window.history.go(-1)")
sleep(2)
print(df_eng1)
