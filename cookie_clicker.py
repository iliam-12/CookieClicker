from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import sys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
driver = webdriver.Chrome("./chromedriver.exe", chrome_options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

try:
    myElem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'bigCookie')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")
    driver.quit()
    sys.exit()

driver.implicitly_wait(10)

cursor_upgrade = driver.find_element_by_id("product0")
grandma_upgrade = driver.find_element_by_id("product1")
cursor_price = driver.find_element_by_id("productPrice0")
grandma_price = driver.find_element_by_id("productPrice1")
cookies = driver.find_element_by_id("cookies")
actions = ActionChains(driver)
buzzer = driver.find_element_by_id("bigCookie")

def prices_list(prices, upgrades):
    i = 0
    new_list = []
    for price in prices:
        if (i == len(upgrades)):
            return (new_list)
        new_list.append(int(real_int(driver.find_element_by_id("productPrice" + str(i)).text)))
        i+=1
    return (new_list)

def real_int(nb):
    numeric_filter = filter(str.isdigit, nb)
    numeric_string = "".join(numeric_filter)
    print(numeric_string)
    return (numeric_string)

def name_of_upgrade():
    i = 0
    new_list = []
    for name in driver.find_element_by_id("products").text.split():
        if (name == "???"):
            new_list.append("productName" + str(i))
            i+=1
    return (new_list)

def fusion_lists(upgrades, prices):
    double_list = []
    i = 0
    for param in prices:
        double_list.append([prices[i], upgrades[i]])
        i+=1
    return (double_list)

while 1:
    upgrades = name_of_upgrade()
    prices = prices_list(driver.find_element_by_id("products").text.split(), upgrades)
    double_list = fusion_lists(upgrades, prices)
    i = 0
    next_upgrade = min(double_list, key=lambda x: x[0])
    if (int(cookies.text.split(" ")[0]) >= next_upgrade[0]):
        actions.click(driver.find_element_by_id(next_upgrade[1]))
    actions.click(buzzer)
    actions.perform()

#driver.quit()
