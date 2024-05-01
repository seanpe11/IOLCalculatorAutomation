from typing import cast
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import random

class BrowserHillRBF:
    def __init__(self):
        self.driver = webdriver.Firefox()  # or webdriver.Chrome()
        self.driver.get('https://rbfcalculator.com/online/index.html')

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

        def scroll_into_view(element):
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        def scroll_and_input(el, item):
            scroll_into_view(el)
            el.clear()
            el.send_keys(item)

        # Random value generators for the fields
        def random_float(min, max, precision):
            return round(random.uniform(min, max), precision)
        self.driver.find_element(By.ID, "pat_id").send_keys("ABC")
        self.driver.find_element(By.ID, "pat_lastname").send_keys("ABC")

        device_select = Select(self.driver.find_element(By.NAME, "measuringDevice"))
        device_select.select_by_value("ZEISS IOLMASTER 700")
        surgeon_name = "TEST"

        # Fill the target refraction
        target_refr = self.driver.find_element(By.ID, "od_target_refr")
        target_refr.clear()
        target_refr.send_keys(str(random_float(-2.5, 1.0, 2)))

        # Fill other IOL calculation parameters
        self.driver.find_element(By.ID, "od_al").send_keys(str(random_float(19.0, 35.0, 2)))
        self.driver.find_element(By.ID, "od_cct").send_keys(str(random_float(260, 760, 0)))
        self.driver.find_element(By.ID, "od_acd").send_keys(str(random_float(1.25, 5.25, 2)))
        self.driver.find_element(By.ID, "od_lt").send_keys(str(random_float(2.6, 7.4, 2)))
        self.driver.find_element(By.ID, "od_k1").send_keys(str(random_float(37, 52, 2)))
        self.driver.find_element(By.ID, "od_k1Axis").send_keys(str(random_float(0, 180, 0)))
        self.driver.find_element(By.ID, "od_k2").send_keys(str(random_float(37, 52, 2)))
        self.driver.find_element(By.ID, "od_k2Axis").send_keys(str(random_float(0, 180, 0)))
        self.driver.find_element(By.ID, "od_wtw").send_keys(str(random_float(8.8, 14.5, 1)))

        # Select a random option for the keratometric refraction index
        n_select = Select(self.driver.find_element(By.ID, "od_n"))
        n_options = [o.get_attribute('value') for o in n_select.options]
        n_select.select_by_value(random.choice(n_options[1:]))  # Skip the first placeholder option

