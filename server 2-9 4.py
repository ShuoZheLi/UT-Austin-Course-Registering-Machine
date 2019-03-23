import socket
import threading
import time
import re
from twilio.rest import Client
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
# coding=utf-8

s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s4.bind(('45.76.119.50', 10004))
s4.listen(20)

def register_1(sock, addr):
	driver4 = webdriver.Chrome()
	def check_course_1 (id,password,num_1,phone_number,driver_4):
		loginUrl = 'https://login.utexas.edu/login/UI/Login' #设定登陆地址
		driver_4.get(loginUrl) #进入登陆界面
		driver_4.find_element_by_name('IDToken1').send_keys(id) #输入用户名
		driver_4.find_element_by_name('IDToken2').send_keys(password) #输入密码
		driver_4.find_element_by_name('Login.Submit').click() #点击登陆
		CourseList = 'https://utdirect.utexas.edu/apps/registrar/course_schedule/20192/' #需要判断的课程页面
		driver4.get(CourseList+num_1+'/') #进入选课界面
		ClassStatus=driver4.find_element_by_xpath('//*[@id="details_table"]/tbody/tr/td[6]').text #找出课程的状态
		ClassName=driver4.find_element_by_xpath('//*[@id="details"]/h2').text
		sock.send((ClassName).encode('utf-8'))
		sock.recv(1024).decode('utf-8')
		sock.send((ClassStatus).encode('utf-8'))
		sock.recv(1024).decode('utf-8')
		check_status = False #初始化课程状态变量
		while(check_status==False): #如没有开启则判断condition为否，并循环刷新
			driver4.refresh() #刷新页面
			ClassStatus=driver4.find_element_by_xpath('//*[@id="details_table"]/tbody/tr/td[6]').text #找出课程的状态
			if ClassStatus=="open": #如课程开启则判断condition为真
				register_page = 'https://utdirect.utexas.edu/registration/chooseSemester.WBX' #需要判断的课程页面
				driver_4.get(register_page) #进入选课界面
				driver_4.find_element_by_name('submit').click()
				driver_4.find_element_by_name('s_unique_add').send_keys(num_1)
				driver_4.find_element_by_xpath('//*[@id="ds_request_STADD"]').click()
				driver_4.find_element_by_xpath('//*[@id="regform"]/input[4]').click()
				src = driver_4.page_source
				text_found = re.search(r'closed', src)
				if text_found:
					check_status = False
				else:
					check_status = True
					if (phone_number!="12345"):
						# Your Account SID from twilio.com/console
						account_sid = "AC4fcf8a0db1723e4559f480d686ebac53"
						# Your Auth Token from twilio.com/console
						auth_token  = "558a95128f806c5e675507386b6c063f"
						client = Client(account_sid, auth_token)
						message = client.messages.create(
						# 这里中国的号码前面需要加86
						to="+1"+phone_number,
						from_="+17372004519",
						body="Congratulation for getting in "+ClassName)
						print(message.sid)
					sock.send((ClassStatus).encode('utf-8'))
					
				
				
	print('Accept new connection from %s:%s...' % addr)
	list = []
	while True:
		data = sock.recv(1024)
		data.decode('utf-8')
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
		list.append('%s' % data.decode('utf-8'))
	check_course_1 (list[0],list[1],list[2],list[3],driver4)
	
while True:
	sock1, addr1 = s4.accept()
	t = threading.Thread(target=register_1, args=(sock1, addr1))
	t.start()

