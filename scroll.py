# Scroll down - You can increase or decrease the size of loop according to your friend list
i=0
while i < 3:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    i=i+1
    print(i)
    sleep(3)