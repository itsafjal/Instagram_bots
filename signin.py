username = "Username"
password = "Password"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

driver = webdriver.Firefox()
driver.get("https://www.instagram.com/")
#driver.find_elements_by_tag_name("a")[1].click()
driver.implicitly_wait(30)
driver.find_element_by_class_name("_k6cv7").click()
#print "Perimene file....".upper()
driver.implicitly_wait(30)
driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(password)
#driver.find_element_by_class_name("button-green").click()
driver.find_element_by_css_selector("button._rz1lq._k2yal._84y62._7xso1._nv5lf").click()

driver.implicitly_wait(60)
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#driver.execute_script("window.scrollTo(0, Y)")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
