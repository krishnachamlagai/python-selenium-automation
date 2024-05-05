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
driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&prevRID=SH53XV92P57WZP7Z12Q2&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
sleep(5)

# select elements using css selector
# 1. amazon logo
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')

# 2. Form heading
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# 3. Customer name field
driver.find_element(By.CSS_SELECTOR, "input.a-input-text[name='customerName']")

# 4. Mobile number or email field
driver.find_element(By.CSS_SELECTOR, "input.a-input-text[name='email']")

# 5. Password
driver.find_element(By.CSS_SELECTOR, "input.a-input-text[name='password']")

# 6. Locating by xpath for "Passwords must be at least 6 characters.".
driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Passwords must be at least 6 characters.')]")

# 7. Password check
driver.find_element(by=By.CSS_SELECTOR, value="input.a-input-text[name='passwordCheck']")

# 8. Continue button
driver.find_element(by=By.CSS_SELECTOR, value="input.a-button-input[id='continue']")

# 9. Condition of Use
driver.find_element(by=By.CSS_SELECTOR, value="#legalTextRow > a:first-child")

# 10. Privacy
driver.find_element(by=By.CSS_SELECTOR, value="#legalTextRow > a:last-child")

# 11. Signin
driver.find_element(by=By.CSS_SELECTOR, value="a.a-link-emphasis")







