# 1. IMPORT LIBRARIES
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options

# 2. SPECIFY THE HIGH LEVEL VARIABLES
website = "https://www.facebook.com/"
email = input("Input you email: ")
password = input("Input your password: ")

# 3. DISABLE NOTIFICATIONS
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 5}
)

# 4. INSTALL WEB DRIVER
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options= option)
driver.get(website)

# 5. INSERT USERNAME + PASSWORD
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys(password)
driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys(Keys.RETURN)
sleep(5)

# 6 GO TO MESSAGES
driver.get('https://www.facebook.com/messages/')

sleep(10)

