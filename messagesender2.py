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
email = input("Input your email: ")
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

# 6 GO TO MESSAGES
driver.get('https://www.facebook.com/friends/list')
sleep(3)

# 6. GET FRIEND LIST
# Scroll down - You can increase or decrease the size of loop according to your friend list
i=0
while i<3:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    i=i+1
    print(i)
    sleep(3)

friend_list = driver.find_elements(By.XPATH, '//div[@class="x1qjc9v5 x1q0q8m5 x1qhh985 xu3j5b3 xcfux6l x26u7qi xm0m39n x13fuv20 x972fbf x9f619 x78zum5 x1r8uery xdt5ytf x1iyjqo2 xs83m0k x1qughib xat24cr x11i5rnm x1mh8g0r xdj266r x2lwn1j xeuugli x4uap5 xkhd6sd xz9dl7a xsag5q8 x1n2onr6 x1ja2u2z"]')
friends = []
for friend in friend_list:
    friends.append(friend.text)

print(friends)

# 6 GO TO MESSAGES
driver.get('https://www.facebook.com/messages/')
sleep(3)

# 7 SEND MESSAGE
for friend in friends:
    driver.find_element(By.XPATH,
                            '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/label/input').send_keys(
        friend)

    action = ActionChains(driver)
    action.click(driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[1]/ul/li[2]'))
    action.perform()

    sleep(2)
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p').send_keys(
        message)
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p').send_keys(
        Keys.RETURN)
    sleep(2)
    driver.get('https://www.facebook.com/messages/')
    sleep(2)
