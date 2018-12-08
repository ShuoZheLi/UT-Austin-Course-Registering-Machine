#coding=utf-8
import sys
import requests
from selenium import webdriver
import tkinter
from tkinter import messagebox
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import threading
from selenium.webdriver.common.action_chains import ActionChains

def thread_it(func, id,password,num1,num2,num3,num4,num5,num6):
	threads = []
	if (num1!=''):
		driver1 = webdriver.Chrome()
		t1 = threading.Thread(target=login_1, args=(id,password,num1,driver1))
		t1.setDaemon(True)
		t1.start()
		
	if (num2!=''):
		driver2 = webdriver.Chrome()
		t2 = threading.Thread(target=login_2, args=(id,password,num2,driver2))
		t2.setDaemon(True)
		t2.start()
	
	if (num3!=''):
		driver3 = webdriver.Chrome()
		t3 = threading.Thread(target=login_3, args=(id,password,num3,driver3))
		t3.setDaemon(True)
		t3.start()
		
	if (num4!=''):
		driver4 = webdriver.Chrome()
		t4 = threading.Thread(target=login_4, args=(id,password,num4,driver4))
		t4.setDaemon(True)
		t4.start()
		
	if (num5!=''):
		driver5 = webdriver.Chrome()
		t5 = threading.Thread(target=login_5, args=(id,password,num5,driver5))
		t5.setDaemon(True)
		t5.start()

	if (num6!=''):
		driver6 = webdriver.Chrome()
		t6 = threading.Thread(target=login_6, args=(id,password,num6,driver6))
		t6.setDaemon(True)
		t6.start()
	
def login_1 (id,password,n1,driver1):
	loginUrl = 'https://login.utexas.edu/login/UI/Login' #设定登陆地址
	driver1.get(loginUrl) #进入登陆界面
	driver1.find_element_by_name('IDToken1').send_keys(id) #输入用户名
	driver1.find_element_by_name('IDToken2').send_keys(password) #输入密码
	driver1.find_element_by_name('Login.Submit').click() #点击登陆
	try: #判断账号密码是否正确
		driver1.find_element_by_id('wordmark') #寻找账号密码错误页面的元素
	except NoSuchElementException: #如果找不到即报错
		check_course_1 (n1,driver1)
	else: #如果报错就执行账号密码错误弹窗
		wrong_pass()

def login_2 (id,password,n2,driver2):
	loginUrl = 'https://login.utexas.edu/login/UI/Login' #设定登陆地址
	driver2.get(loginUrl) #进入登陆界面
	driver2.find_element_by_name('IDToken1').send_keys(id) #输入用户名
	driver2.find_element_by_name('IDToken2').send_keys(password) #输入密码
	driver2.find_element_by_name('Login.Submit').click() #点击登陆
	try: #判断账号密码是否正确
		driver2.find_element_by_id('wordmark') #寻找账号密码错误页面的元素
	except NoSuchElementException: #如果找不到即报错
		check_course_2 (n2,driver2)
	else: #如果报错就执行账号密码错误弹窗
		wrong_pass()
		
def login_3 (id,password,n3,driver3):
	loginUrl = 'https://login.utexas.edu/login/UI/Login' #设定登陆地址
	driver3.get(loginUrl) #进入登陆界面
	driver3.find_element_by_name('IDToken1').send_keys(id) #输入用户名
	driver3.find_element_by_name('IDToken2').send_keys(password) #输入密码
	driver3.find_element_by_name('Login.Submit').click() #点击登陆
	try: #判断账号密码是否正确
		driver3.find_element_by_id('wordmark') #寻找账号密码错误页面的元素
	except NoSuchElementException: #如果找不到即报错
		check_course_3 (n3,driver3)
	else: #如果报错就执行账号密码错误弹窗
		wrong_pass()
		
def login_4 (id,password,n4,driver4):
	loginUrl = 'https://login.utexas.edu/login/UI/Login' #设定登陆地址
	driver4.get(loginUrl) #进入登陆界面
	driver4.find_element_by_name('IDToken1').send_keys(id) #输入用户名
	driver4.find_element_by_name('IDToken2').send_keys(password) #输入密码
	driver4.find_element_by_name('Login.Submit').click() #点击登陆
	try: #判断账号密码是否正确
		driver4.find_element_by_id('wordmark') #寻找账号密码错误页面的元素
	except NoSuchElementException: #如果找不到即报错
		check_course_4 (n4,driver4)
	else: #如果报错就执行账号密码错误弹窗
		wrong_pass()

def login_5 (id,password,n5,driver5):
	loginUrl = 'https://login.utexas.edu/login/UI/Login' #设定登陆地址
	driver5.get(loginUrl) #进入登陆界面
	driver5.find_element_by_name('IDToken1').send_keys(id) #输入用户名
	driver5.find_element_by_name('IDToken2').send_keys(password) #输入密码
	driver5.find_element_by_name('Login.Submit').click() #点击登陆
	try: #判断账号密码是否正确
		driver5.find_element_by_id('wordmark') #寻找账号密码错误页面的元素
	except NoSuchElementException: #如果找不到即报错
		check_course_5 (n5,driver5)
	else: #如果报错就执行账号密码错误弹窗
		wrong_pass()
		
def login_6 (id,password,n6,driver6):
	loginUrl = 'https://login.utexas.edu/login/UI/Login' #设定登陆地址
	driver6.get(loginUrl) #进入登陆界面
	driver6.find_element_by_name('IDToken1').send_keys(id) #输入用户名
	driver6.find_element_by_name('IDToken2').send_keys(password) #输入密码
	driver6.find_element_by_name('Login.Submit').click() #点击登陆
	try: #判断账号密码是否正确
		driver6.find_element_by_id('wordmark') #寻找账号密码错误页面的元素
	except NoSuchElementException: #如果找不到即报错
		check_course_6 (n6,driver6)
	else: #如果报错就执行账号密码错误弹窗
		wrong_pass()
		
def check_course_1 (num_1,driver1): #检查课程状态
	CourseList = 'https://utdirect.utexas.edu/apps/registrar/course_schedule/20192/' #需要判断的课程页面
	driver1.get(CourseList+num_1+'/') #进入选课界面
	ClassStatus=driver1.find_element_by_xpath('//*[@id="details_table"]/tbody/tr/td[6]').text #找出课程的状态
	ClassName=driver1.find_element_by_xpath('//*[@id="details"]/h2').text
	check_status = False #初始化课程状态变量
	tkinter.Label(window, text=ClassStatus).place(x=650, y=370)
	tkinter.Label(window, text=ClassName).place(x=40, y= 370)

	if ClassStatus=="open": #如已经开启则判断condition为真
		check_status = True

	while(check_status==False): #如没有开启则判断condition为否，并循环刷新
		driver1.refresh() #刷新页面
		ClassStatus=driver1.find_element_by_xpath('//*[@id="details_table"]/tbody/tr/td[6]').text #找出课程的状态
		if ClassStatus=="open": #如课程开启则判断condition为真
			check_status = True


	print (ClassStatus) #显示最新状态

def check_course_2 (num_1,driver2): #检查课程状态
	CourseList = 'https://utdirect.utexas.edu/apps/registrar/course_schedule/20192/' #需要判断的课程页面
	driver2.get(CourseList+num_1+'/') #进入选课界面
	ClassStatus=driver2.find_element_by_xpath('//*[@id="details_table"]/tbody/tr/td[6]').text #找出课程的状态
	ClassName=driver2.find_element_by_xpath('//*[@id="details"]/h2').text
	check_status = False #初始化课程状态变量
	tkinter.Label(window, text=ClassStatus).place(x=650, y=410)
	tkinter.Label(window, text=ClassName).place(x=40, y= 410)

	if ClassStatus=="open": #如已经开启则判断condition为真
		check_status = True

	while(check_status==False): #如没有开启则判断condition为否，并循环刷新
		driver2.refresh() #刷新页面
		ClassStatus=driver2.find_element_by_xpath('//*[@id="details_table"]/tbody/tr/td[6]').text #找出课程的状态
		if ClassStatus=="open": #如课程开启则判断condition为真
			check_status = True


	print (ClassStatus) #显示最新状态

def check_course_3 (num_1,driver3): #检查课程状态
	CourseList = 'https://utdirect.utexas.edu/apps/registrar/course_schedule/20192/' #需要判断的课程页面
	driver3.get(CourseList+num_1+'/') #进入选课界面
	ClassStatus=driver3.find_element_by_xpath('//*[@id="details_table"]/tbody/tr/td[6]').text #找出课程的状态
	ClassName=driver3.find_element_by_xpath('//*[@id="details"]/h2').text
	check_status = False #初始化课程状态变量
	tkinter.Label(window, text=ClassStatus).place(x=650, y=450)
	tkinter.Label(window, text=ClassName).place(x=40, y= 450)

	if ClassStatus=="open": #如已经开启则判断condition为真
		check_status = True

	while(check_status==False): #如没有开启则判断condition为否，并循环刷新
		driver3.refresh() #刷新页面
		ClassStatus=driver3.find_element_by_xpath('//*[@id="details_table"]/tbody/tr/td[6]').text #找出课程的状态
		if ClassStatus=="open": #如课程开启则判断condition为真
			check_status = True


	print (ClassStatus) #显示最新状态

def check_course_4 (num_1,driver4): #检查课程状态
	CourseList = 'https://utdirect.utexas.edu/apps/registrar/course_schedule/20192/' #需要判断的课程页面
	driver4.get(CourseList+num_1+'/') #进入选课界面
	ClassStatus=driver4.find_element_by_xpath('//*[@id="details_table"]/tbody/tr/td[6]').text #找出课程的状态
	ClassName=driver4.find_element_by_xpath('//*[@id="details"]/h2').text
	check_status = False #初始化课程状态变量
	tkinter.Label(window, text=ClassStatus).place(x=650, y=490)
	tkinter.Label(window, text=ClassName).place(x=40, y= 490)

	if ClassStatus=="open": #如已经开启则判断condition为真
		check_status = True

	while(check_status==False): #如没有开启则判断condition为否，并循环刷新
		driver4.refresh() #刷新页面
		ClassStatus=driver4.find_element_by_xpath('//*[@id="details_table"]/tbody/tr/td[6]').text #找出课程的状态
		if ClassStatus=="open": #如课程开启则判断condition为真
			check_status = True


	print (ClassStatus) #显示最新状态
	
def check_course_5 (num_1,driver5): #检查课程状态
	CourseList = 'https://utdirect.utexas.edu/apps/registrar/course_schedule/20192/' #需要判断的课程页面
	driver5.get(CourseList+num_1+'/') #进入选课界面
	ClassStatus=driver5.find_element_by_xpath('//*[@id="details_table"]/tbody/tr/td[6]').text #找出课程的状态
	ClassName=driver5.find_element_by_xpath('//*[@id="details"]/h2').text
	check_status = False #初始化课程状态变量
	tkinter.Label(window, text=ClassStatus).place(x=650, y=530)
	tkinter.Label(window, text=ClassName).place(x=40, y= 530)

	if ClassStatus=="open": #如已经开启则判断condition为真
		check_status = True

	while(check_status==False): #如没有开启则判断condition为否，并循环刷新
		driver5.refresh() #刷新页面
		ClassStatus=driver5.find_element_by_xpath('//*[@id="details_table"]/tbody/tr/td[6]').text #找出课程的状态
		if ClassStatus=="open": #如课程开启则判断condition为真
			check_status = True


	print (ClassStatus) #显示最新状态
	
def check_course_6 (num_1,driver6): #检查课程状态
	CourseList = 'https://utdirect.utexas.edu/apps/registrar/course_schedule/20192/' #需要判断的课程页面
	driver6.get(CourseList+num_1+'/') #进入选课界面
	ClassStatus=driver6.find_element_by_xpath('//*[@id="details_table"]/tbody/tr/td[6]').text #找出课程的状态
	ClassName=driver6.find_element_by_xpath('//*[@id="details"]/h2').text
	check_status = False #初始化课程状态变量
	tkinter.Label(window, text=ClassStatus).place(x=650, y=570)
	tkinter.Label(window, text=ClassName).place(x=40, y= 570)

	if ClassStatus=="open": #如已经开启则判断condition为真
		check_status = True

	while(check_status==False): #如没有开启则判断condition为否，并循环刷新
		driver6.refresh() #刷新页面
		ClassStatus=driver6.find_element_by_xpath('//*[@id="details_table"]/tbody/tr/td[6]').text #找出课程的状态
		if ClassStatus=="open": #如课程开启则判断condition为真
			check_status = True


	print (ClassStatus) #显示最新状态
		

	
def UI(window): #窗口函数
	# welcome image
	window.title('my window')
	window.geometry("800x600")
	canvas = tkinter.Canvas(window, height=500, width=500)#创建画布
	image_file = tkinter.PhotoImage(file='welcome.png')#加载图片文件
	image = canvas.create_image(0,0, anchor='nw', image=image_file)#将图片置于画布上
	canvas.pack(side='top')#放置画布（为上端）

	# user information
	tkinter.Label(window, text='EID: ').place(x=50, y= 250)#创建一个`label`名为`User name: `置于坐标（50,150）
	tkinter.Label(window, text='Password: ').place(x=50, y=290)
	tkinter.Label(window, text='Name').place(x=200, y=330)
	tkinter.Label(window, text='Unique#').place(x=450, y=330)
	tkinter.Label(window, text='Status').place(x=650, y=330)
	
	var_usr_name = tkinter.StringVar()#定义变量
	var_usr_name.set('ab1234')#变量赋值'example@python.com'
	entry_usr_name = tkinter.Entry(window, textvariable=var_usr_name)#创建一个`entry`，显示为变量`var_usr_name`即图中的`example@python.com`
	entry_usr_name.place(x=150, y=250)
	var_usr_pwd = tkinter.StringVar()
	entry_usr_pwd = tkinter.Entry(window, textvariable=var_usr_pwd, show='*')#`show`这个参数将输入的密码变为`***`的形式
	entry_usr_pwd.place(x=150, y=290)
	

	var_usr_num_1 = tkinter.StringVar()
	entry_usr_num_1 = tkinter.Entry(window, textvariable=var_usr_num_1)
	entry_usr_num_1.place(x=450, y=370)
	
	
	var_usr_num_2 = tkinter.StringVar()
	entry_usr_num_2 = tkinter.Entry(window, textvariable=var_usr_num_2)
	entry_usr_num_2.place(x=450, y=410)

	
	var_usr_num_3 = tkinter.StringVar()
	entry_usr_num_3 = tkinter.Entry(window, textvariable=var_usr_num_3)
	entry_usr_num_3.place(x=450, y=450)

	
	var_usr_num_4 = tkinter.StringVar()
	entry_usr_num_4 = tkinter.Entry(window, textvariable=var_usr_num_4)
	entry_usr_num_4.place(x=450, y=490)

	
	var_usr_num_5 = tkinter.StringVar()
	entry_usr_num_5 = tkinter.Entry(window, textvariable=var_usr_num_5)
	entry_usr_num_5.place(x=450, y=530)


	var_usr_num_6 = tkinter.StringVar()
	entry_usr_num_6 = tkinter.Entry(window, textvariable=var_usr_num_6)
	entry_usr_num_6.place(x=450, y=570)

	

	def hit_me():
		send_id=var_usr_name.get()
		send_pw=var_usr_pwd.get()
		send_nm=var_usr_num.get()
		tkinter.messagebox.showinfo(title='Welcome', message='How are you? ' + send_id)
		login (send_id,send_pw,send_nm)
	
	# login and sign up button
	btn_login = tkinter.Button(window, text='Start', command=lambda :thread_it(login_1, var_usr_name.get(),var_usr_pwd.get(),var_usr_num_1.get(),var_usr_num_2.get(),var_usr_num_3.get(),var_usr_num_4.get(),var_usr_num_5.get(),var_usr_num_6.get()))#定义一个`button`按钮，名为`Login`,触发命令为`usr_login`
	btn_login.place(x=350, y=250)
	window.mainloop()


	
def wrong_pass():
	tkinter.messagebox.showinfo(title='error', message='Wrong Password')

window = tkinter.Tk()
UI(window)

