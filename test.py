import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

url = "https://www.google.com/"
driver.get(url)
driver.implicitly_wait(10)

# test_var = driver.find_element(By.XPATH, "(//*[name()='a' and @class='pHiOh'])[1]")

# Expecting About on PC and Advertising using Selenium because of smaller window
# print(test_var.text)
print(driver.title)
