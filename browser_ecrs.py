from typing import cast
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class BrowserECRS:
    def __init__(self):
        self.driver = webdriver.Firefox()  # or webdriver.Chrome()
        self.driver.get('https://iolcalculator.escrs.org/')

    def autofill(self, item):
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
        a_const = cast(str, item.get('A-consant'))
        surgeon_name = "TEST"

        def scroll_into_view(element):
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        def scroll_and_input(el, item):
            scroll_into_view(el)
            el.clear()
            el.send_keys(item)


        surgeon_nameEl = self.driver.find_element(By.XPATH, "//label[contains(text(), 'Surgeon')]/preceding-sibling::div/input")
        scroll_and_input(surgeon_nameEl, surgeon_name)
        nameEl = self.driver.find_element(By.XPATH, "//label[contains(text(), 'Patient Initials')]/preceding-sibling::div/input")
        scroll_and_input(nameEl, name)
        alEl = self.driver.find_element(By.XPATH, "//label[contains(text(), 'AL')]/preceding-sibling::div/input")
        scroll_and_input(alEl, al)
        acdEl = self.driver.find_element(By.XPATH, "//label[contains(text(), 'ACD')]/preceding-sibling::div/input")
        scroll_and_input(acdEl, acd)
        ltEl = self.driver.find_element(By.XPATH, "//label[contains(text(), 'LT')]/preceding-sibling::div/input")
        scroll_and_input(ltEl, lt)
        cctEl = self.driver.find_element(By.XPATH, "//label[contains(text(), 'CCT')]/preceding-sibling::div/input")
        scroll_and_input(cctEl, cct)
        wtwEl = self.driver.find_element(By.XPATH, "//label[contains(text(), 'CD (WTW)')]/preceding-sibling::div/input")
        scroll_and_input(wtwEl, wtw)
        k1El = self.driver.find_element(By.XPATH, "//label[contains(text(), 'K1')]/preceding-sibling::div/input")
        scroll_and_input(k1El, k1)
        k2El = self.driver.find_element(By.XPATH, "//label[contains(text(), 'K2')]/preceding-sibling::div/input")
        scroll_and_input(k2El, k2)
        a_constEl = self.driver.find_element(By.XPATH, "//label[contains(text(), 'Hill-RBF A-Constant')]/preceding-sibling::div/input")
        scroll_and_input(a_constEl, a_const)

        # special cases
        target_el = self.driver.find_element(By.XPATH, "//label[contains(text(), 'Target Refraction')]/preceding-sibling::div/input")
        self.driver.execute_script("arguments[0].value = arguments[1]", target_el, target)

        # # TODO: gender FIX
        # gender_el = self.driver.find_element(By.XPATH, "//label[contains(text(), 'Gender')]/preceding-sibling::div/input")
        #
        # # TODO: device FIX
        # device_el = self.driver.find_element(By.XPATH, "//label[contains(text(), 'Device')]/preceding-sibling::div/input")
