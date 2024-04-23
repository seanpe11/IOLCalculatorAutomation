from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from typing import cast
import pandas as pd



# @params: 
### item, which is a df row
def run_ecrs(item):
    driver = webdriver.Firefox()  # or webdriver.Chrome()
    driver.get('https://iolcalculator.escrs.org/')
    name = cast(str, item.get('Name'))
    target = cast(str, item.get('Target'))
    gender = cast(str, item.get('Gender'))
    device = cast(str, item.get('Device'))
    al = cast(str, item.get('AL'))
    cct = cast(str, item.get('CCT'))
    acd = cast(str, item.get('ACD'))
    lt = cast(str, item.get('LT'))
    k1 = cast(str, item.get('K1'))
    k2 = cast(str, item.get('K2'))
    wtw = cast(str, item.get('WTW'))
    surgeon_name = "TEST"

    # Find the input field by navigating to its preceding sibling

    # # TODO: gender FIX
    # gender_el = Select(driver.find_element(By.XPATH, "//label[contains(text(), 'Gender')]/preceding-sibling::div/input"))
    # gender_el.select_by_value("Male" if gender == "M" else "Female")

    # driver.find_element(By.XPATH, "//label[contains(text(), 'Device')]/preceding-sibling::div/input").send_keys(device)
    driver.find_element(By.XPATH, "//label[contains(text(), 'Surgeon')]/preceding-sibling::div/input").send_keys(surgeon_name)
    driver.find_element(By.XPATH, "//label[contains(text(), 'Patient Initials')]/preceding-sibling::div/input").send_keys(name)
    driver.find_element(By.XPATH, "//label[contains(text(), 'AL')]/preceding-sibling::div/input").send_keys(al)
    driver.find_element(By.XPATH, "//label[contains(text(), 'CCT')]/preceding-sibling::div/input").send_keys(cct)
    driver.find_element(By.XPATH, "//label[contains(text(), 'LT')]/preceding-sibling::div/input").send_keys(lt)
    driver.find_element(By.XPATH, "//label[contains(text(), 'ACD')]/preceding-sibling::div/input").send_keys(acd)
    driver.find_element(By.XPATH, "//label[contains(text(), 'K1')]/preceding-sibling::div/input").send_keys(k1)
    driver.find_element(By.XPATH, "//label[contains(text(), 'K2')]/preceding-sibling::div/input").send_keys(k2)
    driver.find_element(By.XPATH, "//label[contains(text(), 'CD (WTW)')]/preceding-sibling::div/input").send_keys(wtw)
    driver.find_element(By.XPATH, "//label[contains(text(), 'Target Refraction')]/preceding-sibling::div/input").send_keys(target)


    input("Form autofilled. Press enter after you've filled out the captcha and the output is showing:")
