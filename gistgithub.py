from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import string

#driver = webdriver.Chrome()
driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()

driver.get("https://gist.github.com/discover")
time.sleep(2)

#LOGIN
driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/a[1]").click()
time.sleep(2)
driver.find_element_by_id("login_field").send_keys("a.nurul.fajrina@gmail.com")
time.sleep(2)
driver.find_element_by_id("password").send_keys("Annisanurulfajrina123")
driver.find_element_by_xpath("/html/body/div[3]/main/div/div[3]/form/div/input[12]").click()
time.sleep(2)

#CREATE A GIST
driver.get("https://gist.github.com/")
time.sleep(2)
#fill the description
gist_description = ''.join(random.choice(string.ascii_uppercase) for _ in range(8))
driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/form/div/div[1]/input").send_keys(gist_description)
time.sleep(2)
#fill the filename
filename = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
filewithextension = filename + ".txt"
driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/form/div/div[1]/div[2]/div/div[1]/div[1]/input[2]").send_keys(filewithextension)
time.sleep(2)
#fill the contents
contents = ''.join(random.choice(string.ascii_uppercase) for _ in range(20))
driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/form/div/div[1]/div[2]/div/div[2]/div/div/div[5]/div[1]/div/div/div/div[5]/div/pre").send_keys(contents)
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/form/div/div[2]/div/details/summary").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/form/div/div[2]/div/details/details-menu/label[2]/div/span[2]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/form/div/div[2]/div/button").click()
time.sleep(2)

#SEE THE LIST OF GIST
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/nav/a[1]").click()
time.sleep(3)
driver.execute_script("window.scrollTo(0, 200);")
time.sleep(2)
driver.execute_script("window.scrollTo(200, 400);")
time.sleep(2)
driver.execute_script("window.scrollTo(400, 600);")
time.sleep(2)
driver.execute_script("window.scrollTo(600, 800);")
time.sleep(2)
driver.execute_script("window.scrollTo(800, 1000);")
time.sleep(2)
driver.execute_script("window.scrollTo(1000, 0);")
time.sleep(2)

#DELETE A GIST
driver.find_element_by_xpath("/html/body/div[1]/div/div[6]/details/summary/span").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div/div[6]/details/details-menu/a[1]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[4]/div/main/div/div/div[2]/div[2]/div[1]/div/div[2]/span[1]/a[2]/strong").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[4]/div/main/div[1]/div/div[1]/ul/li[2]/form/button").click()
time.sleep(2)
Alert = driver.switch_to.alert.accept()

#EDIT A GIST
driver.find_element_by_xpath("/html/body/div[4]/div/main/div/div/div[2]/div[2]/div[1]/div/div[2]/span[1]/a[2]/strong").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[4]/div/main/div[1]/div/div[1]/ul/li[1]/a").click()
time.sleep(2)
contentsedit = ''.join(random.choice(string.ascii_uppercase) for _ in range(20))
driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/form/div/div[1]/div[2]/div/div[2]/div/div/div[5]/div[1]/div/div/div/div[5]/div/pre").send_keys(contentsedit)
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/form/div/div[2]/button").click()
time.sleep(2)

#LOGOUT
driver.find_element_by_xpath("/html/body/div[1]/div/div[6]/details/summary/span").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div/div[6]/details/details-menu/form/button").click()
time.sleep(2)
driver.close()