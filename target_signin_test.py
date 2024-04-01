from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')
sleep(7)

# Click SignIn button
driver.find_element(By.XPATH, "//span[@class='styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3']").click()

sleep(3)

# Click SignIn from side navigation
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
sleep(3)

# Verify SignIn page opened:
# Sign into your Target account” text is shown,
# SignIn button is shown (you can just use driver.find_element() to check for element’s presence, no need to assert here)
signin_text = driver.find_element(By.XPATH, "//h1[@class='styles__StyledHeading-sc-1xmf98v-0 styles__AuthHeading-sc-kz6dq2-2 jhKFiw kcHdEa']")
signin_button = driver.find_element(By.XPATH, "//button[@type='submit']")

sleep(5)
