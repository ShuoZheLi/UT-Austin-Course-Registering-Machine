#coding=utf-8
import requests
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()


loginUrl = 'https://login.utexas.edu/login/UI/Login' 
driver.get(loginUrl) #进入登陆界面
driver.find_element_by_name('IDToken1').send_keys('XXXX') #输入用户名
driver.find_element_by_name('IDToken2').send_keys('XXXX') #输入密码
driver.find_element_by_name('Login.Submit').click() #点击登陆
CourseList = 'https://utdirect.utexas.edu/acct/fb/my_tuition/my_tuition_home.WBX'
driver.get(CourseList) #进入选课界面

s1=Select(driver.find_element_by_xpath('//*[@id="find"]/select'))
s1.select_by_value("20192")
#driver.find_element_by_name('action_sw').send_keys('20192') 输入用户名

driver.find_element_by_name('GET').click()





