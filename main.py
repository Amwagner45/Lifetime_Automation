import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

load_dotenv()

driver = webdriver.Chrome()

url = r"https://my.lifetime.life/login.html?resource=%2Fclubs%2Ffl%2Fmiami.html"
driver.get(url)

driver.implicitly_wait(10)
# --------------------------------------------------------------------------------------------------------------

username_textbox = driver.find_element(By.XPATH, '//*[@id="account-username"]')
password_textbox = driver.find_element(By.XPATH, '//*[@id="account-password"]')
login_button = driver.find_element(By.XPATH, '//*[@id="login-btn"]')

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

username_textbox.send_keys(username)
time.sleep(2)
password_textbox.send_keys(password)
time.sleep(2)
login_button.click()
time.sleep(2)

# wait for page to load
driver.implicitly_wait(10)

# --------------------------------------------------------------------------------------------------------------

# reserve class
reservations_page_button = driver.find_element(
    By.XPATH, '//*[@id="main-content"]/div[3]/div[2]/div/div/div/div/div/div/p[3]/a'
)
reservations_page_button.click()
time.sleep(2)

# wait for page to load
driver.implicitly_wait(10)
# --------------------------------------------------------------------------------------------------------------

url = "https://my.lifetime.life/clubs/fl/miami/classes.html?selectedDate=2024-09-21&mode=day&location=Miami+at+The+Falls"
driver.get(url)

# wait for page to load
driver.implicitly_wait(10)

search_for = "EDG"
verbose = False
class_selector = driver.find_elements(By.CLASS_NAME, "planner-entry-title")
for c in class_selector:
    if verbose == True:
        print(
            "========================================================",
            c.find_element(By.TAG_NAME, "a").find_element(By.TAG_NAME, "span").text,
            "--------------------------------------------------------",
            c.find_element(By.TAG_NAME, "a").get_attribute("href"),
            "========================================================",
        )
    if (
        c.find_element(By.TAG_NAME, "a").find_element(By.TAG_NAME, "span").text
        == search_for
    ):
        amp_sculpt_reservation_link = c.find_element(By.TAG_NAME, "a").get_attribute(
            "href"
        )
        break

# Navigate to registration page
print(amp_sculpt_reservation_link)
driver.get(amp_sculpt_reservation_link)


driver.implicitly_wait(10)
# --------------------------------------------------------------------------------------------------------------
# Registration page

# confirm_user_checkbox = (
#     driver.find_element(By.CLASS_NAME, "transition-wrapper")
#     .find_element(
#         By.CLASS_NAME,
#         "c-input.c-checkbox",
#     )
#     .find_element(By.CLASS_NAME, "c-indicator")
# )
# confirm_user_checkbox.click()

# driver.implicitly_wait(2)

amp_sculpt_page_reservation_button = (
    driver.find_element(By.CLASS_NAME, "transition-wrapper")
    .find_element(By.CLASS_NAME, "btn-wrap.m-b-2")
    .find_element(By.TAG_NAME, "button")
)
amp_sculpt_page_reservation_button.click()

driver.implicitly_wait(10)
# --------------------------------------------------------------------------------------------------------------
# Choose seat and finalize registration

# seat selection grid
# seat_selection_grid = driver.find_element(
#     By.XPATH,
#     '//*[@id="schedules-component-element-b0e79ab7c0ec1"]/div/section/div[1]/div/div[2]/div/div/div[2]/div',
# )
# seat_selection_grid = driver.find_element(
#     By.CLASS_NAME,
#     "card-section",
# )

# '//*[@id="schedules-component-element-6a25bdd093ec8"]/div/section/div[1]/div/div[2]/div/div/div[2]'
# "/html/body/main/div[4]/div/section/div[1]/div/div[2]/div/div/div[2]"
# "/html/body/main/div[4]/div/section/div[1]/div/div[2]/div/div/div[2]/div/svg/"

# sixth_seat = seat_selection_grid.find_element(By.TAG_NAME, "div").find_element(
#     By.XPATH, "//*[name()='svg']/g[6]"
# )
# sixth_seat.click()
# print(sixth_seat.find_element(By.XPATH, "text").text)

seat_to_find = 6
for seat in driver.find_elements(
    By.XPATH,
    "//*[name()='div' and @class='card-section-cell spot-map spot-change-mode']//*[name()='g']",
):
    # print(seat.find_element(By.TAG_NAME, "text").text)
    seat_number = seat.find_element(By.XPATH, "//*[name()='text']").text
    print(seat_number)
    if seat_number == seat_to_find:
        seat.find_element(By.XPATH, "//*[name()='circle']").click()

# seat_selection_number_button = seat_selection_grid.find_element(
#     By.NAME,
#     "6",
# )
# seat_selection_number_button.click()

driver.implicitly_wait(10)
# --------------------------------------------------------------------------------------------------------------

# accept terms and conditions
accept_terms_button = driver.find_element(
    By.XPATH,
    "//*[name()='label' and @class='c-input c-checkbox-sm m-b-0']",
)
accept_terms_button.click()

# finish_button = driver.find_element(
#     By.XPATH,
#     '//*[@id="schedules-component-element-b0e79ab7c0ec1"]/div/section/div[1]/div/div[6]/div/div/button[2]',
# )
finish_button = driver.find_element(
    By.XPATH,
    "//*[@class='btn-wrap text-xs-right']//*[name()='button' and normalize-space(text())='Finish']",
).click()

print("Done!")

driver.implicitly_wait(10)
# //*[name()='div' and @class='card-section-cell spot-map spot-change-mode']//*[name()='g']
