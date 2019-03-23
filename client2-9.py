#coding=utf-8

import tkinter  #窗口模块
from tkinter import messagebox
import threading
import socket

def login_1(id,password,num1,phone_number):
	s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s1.connect(('45.76.119.50', 10001))
	s1.send(bytes(id, encoding = "utf8"))
	s1.recv(1024).decode('utf-8')
	s1.send(bytes(password, encoding = "utf8"))
	s1.recv(1024).decode('utf-8')
	s1.send(bytes(num1, encoding = "utf8"))
	s1.recv(1024).decode('utf-8')
	s1.send(bytes(phone_number, encoding = "utf8"))
	s1.recv(1024).decode('utf-8')
	s1.send(b'exit')
	ClassName = s1.recv(1024).decode('utf-8')
	s1.send(bytes(num1, encoding = "utf8"))
	ClassStatus = s1.recv(1024).decode('utf-8')
	s1.send(bytes(num1, encoding = "utf8"))
	tkinter.Label(window, text=ClassName).place(x=40, y= 370)
	status_1 = tkinter.Label(window, text=ClassStatus).place(x=650, y=370)
	if ClassStatus!="open":
		while ClassStatus!="open":
			ClassStatus = s1.recv(1024).decode('utf-8')
		status_1 = tkinter.Label(window, text="Added").place(x=654, y=370)

def login_2(id,password,num2,phone_number):
	s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s2.connect(('45.76.119.50', 10002))
	s2.send(bytes(id, encoding = "utf8"))
	s2.recv(1024).decode('utf-8')
	s2.send(bytes(password, encoding = "utf8"))
	s2.recv(1024).decode('utf-8')
	s2.send(bytes(num2, encoding = "utf8"))
	s2.recv(1024).decode('utf-8')
	s2.send(bytes(phone_number, encoding = "utf8"))
	s2.recv(1024).decode('utf-8')
	s2.send(b'exit')
	ClassName = s2.recv(1024).decode('utf-8')
	s2.send(bytes(num2, encoding = "utf8"))
	ClassStatus = s2.recv(1024).decode('utf-8')
	s2.send(bytes(num2, encoding = "utf8"))
	tkinter.Label(window, text=ClassName).place(x=40, y= 410)
	status_1 = tkinter.Label(window, text=ClassStatus).place(x=650, y=410)
	if ClassStatus!="open":
		while ClassStatus!="open":
			ClassStatus = s2.recv(1024).decode('utf-8')
		status_1 = tkinter.Label(window, text="Added").place(x=654, y=410)
		
def login_3(id,password,num3,phone_number):
	s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s3.connect(('45.76.119.50', 10003))
	s3.send(bytes(id, encoding = "utf8"))
	s3.recv(1024).decode('utf-8')
	s3.send(bytes(password, encoding = "utf8"))
	s3.recv(1024).decode('utf-8')
	s3.send(bytes(num3, encoding = "utf8"))
	s3.recv(1024).decode('utf-8')
	s3.send(bytes(phone_number, encoding = "utf8"))
	s3.recv(1024).decode('utf-8')
	s3.send(b'exit')
	ClassName = s3.recv(1024).decode('utf-8')
	s3.send(bytes(num3, encoding = "utf8"))
	ClassStatus = s3.recv(1024).decode('utf-8')
	s3.send(bytes(num3, encoding = "utf8"))
	tkinter.Label(window, text=ClassName).place(x=40, y=450)
	status_1 = tkinter.Label(window, text=ClassStatus).place(x=650, y=450)
	if ClassStatus!="open":
		while ClassStatus!="open":
			ClassStatus = s3.recv(1024).decode('utf-8')
		status_1 = tkinter.Label(window, text="Added").place(x=654, y=450)
		
def login_4(id,password,num4,phone_number):
	s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s4.connect(('45.76.119.50', 10004))
	s4.send(bytes(id, encoding = "utf8"))
	s4.recv(1024).decode('utf-8')
	s4.send(bytes(password, encoding = "utf8"))
	s4.recv(1024).decode('utf-8')
	s4.send(bytes(num4, encoding = "utf8"))
	s4.recv(1024).decode('utf-8')
	s4.send(bytes(phone_number, encoding = "utf8"))
	s4.recv(1024).decode('utf-8')
	s4.send(b'exit')
	ClassName = s4.recv(1024).decode('utf-8')
	s4.send(bytes(num4, encoding = "utf8"))
	ClassStatus = s4.recv(1024).decode('utf-8')
	s4.send(bytes(num4, encoding = "utf8"))
	tkinter.Label(window, text=ClassName).place(x=40, y=490)
	status_1 = tkinter.Label(window, text=ClassStatus).place(x=650, y=490)
	if ClassStatus!="open":
		while ClassStatus!="open":
			ClassStatus = s4.recv(1024).decode('utf-8')
		status_1 = tkinter.Label(window, text="Added").place(x=654, y=490)
		
def login_5(id,password,num5,phone_number):
	s5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s5.connect(('45.76.119.50', 10005))
	s5.send(bytes(id, encoding = "utf8"))
	s5.recv(1024).decode('utf-8')
	s5.send(bytes(password, encoding = "utf8"))
	s5.recv(1024).decode('utf-8')
	s5.send(bytes(num5, encoding = "utf8"))
	s5.recv(1024).decode('utf-8')
	s5.send(bytes(phone_number, encoding = "utf8"))
	s5.recv(1024).decode('utf-8')
	s5.send(b'exit')
	ClassName = s5.recv(1024).decode('utf-8')
	s5.send(bytes(num5, encoding = "utf8"))
	ClassStatus = s5.recv(1024).decode('utf-8')
	s5.send(bytes(num5, encoding = "utf8"))
	tkinter.Label(window, text=ClassName).place(x=40, y=530)
	status_1 = tkinter.Label(window, text=ClassStatus).place(x=650, y=530)
	if ClassStatus!="open":
		while ClassStatus!="open":
			ClassStatus = s5.recv(1024).decode('utf-8')
		status_1 = tkinter.Label(window, text="Added").place(x=654, y=530)
		
def login_6(id,password,num6,phone_number):
	s6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s6.connect(('45.76.119.50', 10006))
	s6.send(bytes(id, encoding = "utf8"))
	s6.recv(1024).decode('utf-8')
	s6.send(bytes(password, encoding = "utf8"))
	s6.recv(1024).decode('utf-8')
	s6.send(bytes(num6, encoding = "utf8"))
	s6.recv(1024).decode('utf-8')
	s6.send(bytes(phone_number, encoding = "utf8"))
	s6.recv(1024).decode('utf-8')
	s6.send(b'exit')
	ClassName = s6.recv(1024).decode('utf-8')
	s6.send(bytes(num6, encoding = "utf8"))
	ClassStatus = s6.recv(1024).decode('utf-8')
	s6.send(bytes(num6, encoding = "utf8"))
	tkinter.Label(window, text=ClassName).place(x=40, y=570)
	status_1 = tkinter.Label(window, text=ClassStatus).place(x=650, y=570)
	if ClassStatus!="open":
		while ClassStatus!="open":
			ClassStatus = s6.recv(1024).decode('utf-8')
		status_1 = tkinter.Label(window, text="Added").place(x=654, y=570)

def swap_1(id,password,class_to_drop,class_to_add,phone_number):
	s7 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s7.connect(('45.76.119.50', 10007))
	s7.send(bytes(id, encoding = "utf8"))
	s7.recv(1024).decode('utf-8')
	s7.send(bytes(password, encoding = "utf8"))
	s7.recv(1024).decode('utf-8')
	s7.send(bytes(class_to_drop, encoding = "utf8"))
	s7.recv(1024).decode('utf-8')
	s7.send(bytes(class_to_add, encoding = "utf8"))
	s7.recv(1024).decode('utf-8')
	s7.send(bytes(phone_number, encoding = "utf8"))
	s7.recv(1024).decode('utf-8')
	s7.send(b'exit')
	name_class_to_drop = s7.recv(1024).decode('utf-8')
	s7.send(bytes(password, encoding = "utf8"))
	name_class_to_add = s7.recv(1024).decode('utf-8')
	s7.send(bytes(password, encoding = "utf8"))
	status_class_to_add = s7.recv(1024).decode('utf-8')
	s7.send(bytes(password, encoding = "utf8"))
	tkinter.Label(window, text=name_class_to_drop).place(x=50,y=640)
	tkinter.Label(window, text=name_class_to_add).place(x=350,y=640)
	tkinter.Label(window, text=status_class_to_add).place(x=490,y=610)
	if status_class_to_add!="open":
		while status_class_to_add!="open":
			status_class_to_add = s7.recv(1024).decode('utf-8')
		tkinter.Label(window, text="swap done").place(x=654, y=570)
	
def thread_it(id,password,num1,num2,num3,num4,num5,num6,phone_number):
		if (num1!=''): #如果unique number 1 非空格则执行
			t1 = threading.Thread(target=login_1, args=(id,password,num1,phone_number)) #以独立的线程执行下列代码
			t1.setDaemon(True) #建立线程
			t1.start() #启动线程
		
		if (num2!=''):
			t2 = threading.Thread(target=login_2, args=(id,password,num2,phone_number))
			t2.setDaemon(True)
			t2.start()
	
		if (num3!=''):
			t3 = threading.Thread(target=login_3, args=(id,password,num3,phone_number))
			t3.setDaemon(True)
			t3.start()
		
		if (num4!=''):
			t4 = threading.Thread(target=login_4, args=(id,password,num4,phone_number))
			t4.setDaemon(True)
			t4.start()
		
		if (num5!=''):
			t5 = threading.Thread(target=login_5, args=(id,password,num5,phone_number))
			t5.setDaemon(True)
			t5.start()

		if (num6!=''):
			t6 = threading.Thread(target=login_6, args=(id,password,num6,phone_number))
			t6.setDaemon(True)
			t6.start()
			
def swap_thread_it(id,password,class_to_drop,class_to_add,phone_number):
	if (class_to_drop!='') or (class_to_add!=''):
		t7 = threading.Thread(target=swap_1, args=(id,password,class_to_drop,class_to_add,phone_number))
		t7.setDaemon(True)
		t7.start()

def login_0(id,password):
	s0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s0.connect(('45.76.119.50', 9999))
	s0.send(bytes(id, encoding = "utf8"))
	s0.recv(1024).decode('utf-8')
	s0.send(bytes(password, encoding = "utf8"))
	s0.recv(1024).decode('utf-8')
	s0.send(b'exit')
	if (s0.recv(1024).decode('utf-8')=='correct'):
		button_register = tkinter.Button(window, text='Start', state='normal', command=lambda :thread_it( var_usr_name.get(),var_usr_pwd.get(),var_usr_num_1.get(),var_usr_num_2.get(),var_usr_num_3.get(),var_usr_num_4.get(),var_usr_num_5.get(),var_usr_num_6.get(),var_phone_number.get()))#定义一个按钮，名为`Start`,触发命令为`usr_login`,command=lambda 这里的意思是用按钮来传达参数给多线程
		button_register.place(x=350, y=290)		
		button_swap = tkinter.Button(window, text='swap', command=lambda :swap_thread_it(var_usr_name.get(),var_usr_pwd.get(),var_class_to_drop.get(),var_class_to_add.get(),var_phone_number.get()))#定义一个按钮，名为`Start`,触发命令为`usr_login`,command=lambda 这里的意思是用按钮来传达参数给多线程
		button_swap.place(x=650, y=610)
		tkinter.Label(window, text='login successfully').place(x=400, y=250)
	else:
		tkinter.Label(window, text='wrong EID/PASS').place(x=400, y=250)
def empty_input():
	tkinter.messagebox.showinfo(title='error', message='need your EID & PASSWORD')
	
def thread_it_try_login(EID,PASSWORD):
	if (EID =='') or (PASSWORD =='') or (EID =='ab1234'):
		empty_input()
	else:
		threads = [] #创建线程组
		t0 = threading.Thread(target=login_0, args=(EID,PASSWORD))
		t0.setDaemon(True)
		t0.start()
		

window = tkinter.Tk() #用tkinter模块new 一个窗口出来
window.title('my window') #定义窗口名称
window.geometry("800x700") #定义窗口大小
canvas = tkinter.Canvas(window, height=500, width=700) #在窗口里创建并定义一个画布的大小
image_file = tkinter.PhotoImage(file='welcome.png') #定义画布上的图片
image = canvas.create_image(0,0, anchor='nw', image=image_file) #将图片置于画布上
canvas.pack(side='top') #放置画布为上端
	
	#开始定义窗口的按钮
tkinter.Label(window, text='EID:').place(x=50, y=250)#创建一个label名为EID 置于坐标(50,150)
tkinter.Label(window, text='Password:').place(x=50,y=290)#创建一个label名为Password 置于坐标(50,290)
tkinter.Label(window, text='Phone Number for notification').place(x=550, y=250)#创建一个label名为Unique# 置于坐标(450,330)
var_phone_number = tkinter.StringVar()#定义在窗口内文字框里显示的文字
var_phone_number.set('12345')
entry_phone_number = tkinter.Entry(window, textvariable=var_phone_number)#创建一个输入框，淡化显示变量var_usr_name
entry_phone_number.place(x=550, y=275)
tkinter.Label(window, text='Name').place(x=200,y=330)#创建一个label名为Name 置于坐标(200,330)
tkinter.Label(window, text='class to drop').place(x=50,y=590)
tkinter.Label(window, text='class to add').place(x=350,y=590)



var_class_to_drop = tkinter.StringVar() #定义窗口输入变量的类型
entry_class_to_drop = tkinter.Entry(window, textvariable=var_class_to_drop) #定义窗口输入变量的窗口
entry_class_to_drop.place(x=50,y=610) #定义窗口的位置

var_class_to_add = tkinter.StringVar() #定义窗口输入变量的类型
entry_class_to_add = tkinter.Entry(window, textvariable=var_class_to_add) #定义窗口输入变量的窗口
entry_class_to_add.place(x=350,y=610) #定义窗口的位置




tkinter.Label(window, text='Unique#').place(x=450, y=330)#创建一个label名为Unique# 置于坐标(450,330)
tkinter.Label(window, text='Status').place(x=650, y=330)#创建一个label名为Unique# 置于坐标(650,330)
	
	#定义账号与密码的输入框
var_usr_name = tkinter.StringVar()#定义在窗口内文字框里显示的文字
var_usr_name.set('ab1234')#定义变量的内容
entry_usr_name = tkinter.Entry(window, textvariable=var_usr_name)#创建一个输入框，淡化显示变量var_usr_name
entry_usr_name.place(x=150, y=250) #定义变量输入框的位置
var_usr_pwd = tkinter.StringVar() #定义在窗口内文字框里显示的文字
entry_usr_pwd = tkinter.Entry(window, textvariable=var_usr_pwd, show='*')#show这个参数将输入的密码转为*
entry_usr_pwd.place(x=150, y=290)
	
	#定义课程unique number的输入框
var_usr_num_1 = tkinter.StringVar() #定义窗口输入变量的类型
entry_usr_num_1 = tkinter.Entry(window, textvariable=var_usr_num_1) #定义窗口输入变量的窗口
entry_usr_num_1.place(x=450,y=370) #定义窗口的位置
	
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
	
button_login = tkinter.Button(window, text='Login', command=lambda :thread_it_try_login(var_usr_name.get(),var_usr_pwd.get()))#定义一个按钮，名为`Start`,触发命令为`usr_login`,command=lambda 这里的意思是用按钮来传达参数给多线程
button_login.place(x=350, y=250)

	#定义窗口里的按钮函数

	

window.mainloop() #保持窗口循环不消失
