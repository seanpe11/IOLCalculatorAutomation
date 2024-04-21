import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the browser
driver = webdriver.Chrome()  # or webdriver.Chrome()

# Open the website
driver.get('https://bootstrapious.com/tutorial/recaptcha/')

dict_map = {
        'form_name':'Sean',
        'form_lastname': 'Lastname',
        'form_phone': 'sean@email',
        'form_message': 'hello',
}

for key, value in dict_map.items():
    input_el = driver.find_element(By.ID, key)
    input_el.send_keys(value)

input("Waiting for captcha completion (press enter when done):")

submit_button = driver.find_element(By.ID, 'submit')
submit_button.click()



# Read the CSV file

# with open('./data/input.csv', 'r') as csvfile:
#     reader = csv.reader(csvfile)
#     with open('./data/output.csv', 'w', newline='') as outfile:
#         writer = csv.writer(outfile)
#         for row in reader:
#             # Fill out the form
#             for i, value in enumerate(row):
#                 input_element = driver.find_element(By.ID, f'input{i+1}')
#                 input_element.send_keys(value)

#             # Wait for the captcha to appear
#             captcha_element = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.ID, 'captcha'))
#             )

#             # Pause execution and wait for the user to complete the captcha
#             input("Please complete the captcha and press Enter...")

#             # Submit the form
#             submit_button = driver.find_element(By.ID, 'submit')
#             submit_button.click()

#             # Wait for the output to appear
#             output_element = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.ID, 'output'))
#             )

#             # Write the output to the CSV file
#             writer.writerow([output_element.text])
