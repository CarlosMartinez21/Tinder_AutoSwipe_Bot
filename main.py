from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time

url = "https://tinder.com/"
chrome_driver_path = "/Users/CarlosMartinez/Desktop/Coding/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url)
time.sleep(3)
login_btn = driver.find_element(By.LINK_TEXT, "Log in")
login_btn.click()
time.sleep(2)
login_with_facebook_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[2]/button")
login_with_facebook_btn.click()
time.sleep(4)
tinder_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
username_field = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[1]/div/input")
username_field.send_keys("cmartinez21235@gmail.com")
password_field = driver.find_element(By.NAME, "pass")
password_field = password_field.send_keys("Madrid21")
facebook_login_btn = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]")
facebook_login_btn.click()
time.sleep(7)
driver.switch_to.window(tinder_window)
allow_location_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[3]/button[1]")
allow_location_btn.click()
not_interested_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[3]/button[2]")
not_interested_btn.click()
time.sleep(1)
disagree_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button")
disagree_btn.click()
time.sleep(10)
like_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button")

while True:
    time.sleep(2)
    try:
        like_btn.click()
    except NoSuchElementException:
        time.sleep(3)
        match_window = driver.window_handles[1]
        driver.switch_to.window(match_window)
        close_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[4]/button/svg/path")
        close_btn.click()
        driver.switch_to.window(tinder_window)


