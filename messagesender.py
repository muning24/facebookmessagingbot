# 1. IMPORT LIBRARIES
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

# 2. SPECIFY THE HIGH LEVEL VARIABLES
website = "https://www.facebook.com/"
email = input("Input you email: ")
password = input("Input your password: ")
message = input("Message to be sent: ")

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

driver.get(f'https://www.facebook.com/{account}/friends')

# 6. GET FRIEND LIST
# Scroll down - You can increase or decrease the size of loop according to your friend list
i=0
while i<3:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    i=i+1
    print(i)
    sleep(5)

links = driver.find_elements(By.XPATH, '//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv"]')

friends = []
for link in links:
    l = link.get_attribute('href')
    friends.append(l)


# 7. SEND MESSAGES
i = 0
while i < len(friends):
    frd_account = friends[i].split("https://www.facebook.com/")[1]
    driver.get(f'https://www.facebook.com/messages/t/{frd_account}') # open the Facebook Messages page for the friend
    sleep(5)
    try:
        driver.find_element(By.XPATH, '//*[@aria-label="Message"]').send_keys(message) # input the message
    except:
        print("Unable to find it")

    sleep(2)

    try:
        # create action chain object
        action = ActionChains(driver)
        action.click(driver.find_element(By.XPATH, '//*[@aria-label="Press Enter to send"]')) # click the send button
        action.perform()
    except:
        print("Unable to send")

    sleep(5)
    i = i + 1
