import socket
import threading
import time
import re
from twilio.rest import Client
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
# coding=utf-8

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.bind(('45.76.119.50', 10007))
s1.listen(20)

def register_1(sock, addr):
	driver1 = webdriver.Chrome()
	def check_course_1 (id,password,class_to_drop,class_to_add,phone_number,driver_1):
		loginUrl = 'https://login.utexas.edu/login/UI/Login' #设定登陆地址
		driver_1.get(loginUrl) #进入登陆界面
		driver_1.find_element_by_name('IDToken1').send_keys(id) #输入用户名
		driver_1.find_element_by_name('IDToken2').send_keys(password) #输入密码
		driver_1.find_element_by_name('Login.Submit').click() #点击登陆
		CourseList = 'https://utdirect.utexas.edu/apps/registrar/course_schedule/20192/' #需要判断的课程页面
		driver1.get(CourseList+class_to_drop+'/') #进入选课界面
		ClassName_drop=driver1.find_element_by_xpath('//*[@id="details"]/h2').text
		driver1.get(CourseList+class_to_add+'/') #进入选课界面
		ClassName_add=driver1.find_element_by_xpath('//*[@id="details"]/h2').text
		driver1.get(CourseList+class_to_add+'/') #进入选课界面
		ClassStatus=driver1.find_element_by_xpath('//*[@id="details_table"]/tbody/tr/td[6]').text #找出课程的状态
		sock.send((ClassName_drop).encode('utf-8'))
		sock.recv(1024).decode('utf-8')
		sock.send((ClassName_add).encode('utf-8'))
		sock.recv(1024).decode('utf-8')
		sock.send((ClassStatus).encode('utf-8'))
		sock.recv(1024).decode('utf-8')
		check_status = False #初始化课程状态变量
		while(check_status==False): #如没有开启则判断condition为否，并循环刷新
			driver1.refresh() #刷新页面
			ClassStatus=driver1.find_element_by_xpath('//*[@id="details_table"]/tbody/tr/td[6]').text #找出课程的状态
			if ClassStatus=="open": #如课程开启则判断condition为真
				register_page = 'https://utdirect.utexas.edu/registration/chooseSemester.WBX' #需要判断的课程页面
				driver_1.get(register_page) #进入选课界面
				driver_1.find_element_by_name('submit').click()
				driver_1.find_element_by_xpath('//*[@id="s_request_STSWP"]').click()
				sel=Select(driver_1.find_element_by_xpath('//*[@id="regform"]/table/tbody/tr[4]/td[2]/select'))
				sel.select_by_value(class_to_drop)
				driver_1.find_element_by_name('s_swap_unique_add').send_keys(class_to_add)
				driver_1.find_element_by_xpath('//*[@id="regform"]/input[4]').click()
				src = driver_1.page_source
				text_found = re.search(r'closed', src)
				if text_found:
					check_status = False
				else:
					check_status = True
					if (phone_number!="12345"):
						account_sid = "AC4fcf8a0db1723e4559f480d686ebac53"
						auth_token  = "558a95128f806c5e675507386b6c063f"
						client = Client(account_sid, auth_token)
						message = client.messages.create(
						to="+1"+phone_number,
						from_="+17372004519",
						body="Congratulation for getting in "+ClassName_add)
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
	check_course_1 (list[0],list[1],list[2],list[3],list[4],driver1)
	
while True:
	sock1, addr1 = s1.accept()
	t = threading.Thread(target=register_1, args=(sock1, addr1))
	t.start()

