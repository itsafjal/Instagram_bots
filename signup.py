#! /usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

driver = webdriver.Firefox()

url = "https://www.instagram.com/"

driver.get("https://www.instagram.com/")

driver.implicitly_wait(20)

email = "Email id "                             #put your email id  here
pos = email.find("@")

fullname = "Full name" 				#put your full name 

username = "Username"				#pur your username

password = "Password"				#put your password here


driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_name("fullName").send_keys(fullname)
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("password").send_keys(password)


driver.find_elements_by_css_selector("button._1on88._k2yal._84y62._7xso1._nv5lf")[1].click()

driver.implicitly_wait(30)

adv = driver.find_element_by_css_selector("button._ibk5z").click()

