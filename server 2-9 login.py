import socket
import threading
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
#coding=utf-8

s0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s0.bind(('45.76.119.50', 9999))
s0.listen(20)

def login(sock, addr):
	driver0 = webdriver.Chrome()
	def login_0 (id,password,driver_1):
		loginUrl = 'https://login.utexas.edu/login/UI/Login' #设定登陆地址
		driver_1.get(loginUrl) #进入登陆界面
		driver_1.find_element_by_name('IDToken1').send_keys(id) #输入用户名
		driver_1.find_element_by_name('IDToken2').send_keys(password) #输入密码
		driver_1.find_element_by_name('Login.Submit').click() #点击登陆
		try: #判断账号密码是否正确
			driver_1.find_element_by_id('wordmark') #寻找账号密码错误页面的元素
		except NoSuchElementException: #如果找到就执行下列代码
			sock.send(('correct').encode('utf-8'))
			driver_1.close()
		else: #如果报错就执行账号密码错误弹窗
			sock.send(('wrong password').encode('utf-8'))
			driver_1.close()

	print('Accept new connection from %s:%s...' % addr)

	list = []
	while True:
		data = sock.recv(1024)
		if not data or data.decode('utf-8') == 'exit':
			break
		list.append('%s' % data.decode('utf-8'))
		sock.send((data.decode('utf-8')).encode('utf-8'))
	login_0 (list[0],list[1],driver0)

while True:
	sock0, addr0 = s0.accept()
	t0 = threading.Thread(target=login, args=(sock0, addr0))
	t0.start()