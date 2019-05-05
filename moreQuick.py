'''
# TODO (TOM):for quick
print ("hello")
'''

#第一个注释
#The first guy

"""
if False:
    print ("True")
else:
    print ("False")
"""

"""
#!/usr/bin/python3
str = 'runoob'
print(str)
print(str[0:-1])
print(str[0])
print(str[2:])
print(str + 'hello')
print(str * 2)
print(r'hello \n hello')
print(str,end=" " )
print('hello \n hello')
"""

"""
import  sys
for i in sys.argv:
    print("1")
    print (i)
print ('\n ',sys.path)
"""

'''
from sys import argv,path
print(argv,path)
'''
#
# #!/usr/bin/python3
# center = 100
# miles = 1000.0
# name = 'runboob'
# print (center)
# print (miles)
# print (name)
#
# a, b,c = 1, 2, 'run'
#

# list = ["abcd", 784, 2.23, "runboob", 30.3]
# tinylist = ["123", "xiao"]
# print (list)
# print (list[0])
# print (list[1:3])
# print (tinylist * 2)
# print (list + tinylist)
#
# print (list[1:4:2])
# print (list[0:4:2])

# tuple = ('abcd', 786, 2.23, 'runboob', 70.2)
# tinytuple = (123, 'runboob')
# print (tuple)
# print (tuple + tinytuple)

# student = {'Tom', 'Jim', 'Marry', 'Tom', 'Jack', 'Rose'}
# print (student)
# if 'Rose' in student:
#     print ("yes")
# else:
#     print ("no")
# a = set('abcdfe')
# b = set("abc")
# print(a)
# print(a - b)
# print(a | b)
# print(a & b)
# print(a ^ b)

# dict = {'name':"xiao", 'age':12}
# print (dict['name'])

#!/usr/bin/python3
# list1 = ['google', 'Ruboob', 1997, 2001]
# list2 = [1, 2, 3, 4, 5, 6, 7]
# print("list1[0] :", list1[0])
# print('list2[0:5]', list2[0:5])
# list1[1] = 'mi'
# print(list1[1])
# del list2[2]
# print(list2)
# print(len(list1))
# print(max(list2), min(list2))


# list1 = ['google', 'runboob', 'tao']
# list2 =list(range(50))
# list1.extend(list2)
# print(list1, list2)
# print(list2.index(0))
# list2.insert(1, 20)
# print (list2)
# list2.pop(1)
# list2.remove(9)
# print (list2)
# list2.reverse()
# print(list2)
# list6 = list2.copy()
#
# list2.sort(reverse = True)
# print('jj', list2)
# print('jj', list6)

# Tuple1 = (1.2, 3, 4)
# Tuple2 = (2,4)
# Tuple3 = Tuple1 + Tuple2
# print(Tuple3)
# Tuple4 = Tuple1[0:3]
# print(Tuple3, 23, len(Tuple2), max(Tuple1), min(Tuple2))
# print(len(Tuple2))
# list1 = [1,2,3]
# tuple1 = tuple(list1)
# print(tuple1)

# dict = {'Name': 'Runboob', 'Age': 5, 'Class': 'First'}
# print(dict['Name'])
# dict['Name'] = 'Xiao'
# print(dict['Name'], len(dict), str(dict), type(dict) )
# dict2 = dict.copy ()
# dict.clear()
# print(dict2, 3)

#!/usr/bin/python3
# seq = ('name', 'age', 'sex')
# dict = dict.fromkeys(seq)
# dict2 = dict.fromkeys(seq, 12)
# print(dict, dict2)
# print(dict2.get('name'))
# if 'sex' not in dict2:
#     print("This is  man")
# else:
#     print('This is plant')
# print(dict2.items())

# dict = {'name': 'run', 'age': 7}
# t = list(dict.keys())
# print (t)


# thisset = set(('google', 'tao', 'baidu'))
# thisset.add('face')
# thisset.add(2)
# thisset.remove('tao')
# thisset.pop()
# print(thisset,len(thisset))
# if 'baidu' in thisset:
#     print(2)

# a = 0
# b = 1
# while(b<12):
#     print(b)
#     b = a+b
#     a = b

# age = int(input("input the age"))
# if age < 0:
#     print("oh no")
# elif age == 1:
#     print("so small")
# elif age == 2:
#     print('oh two')
# else:
#     print("bye")

# number = 8
# guess = -1
# print('input')
# while guess != number:
#     guess = int(input("now"))
#     if  guess < number:
#         print('more a little')
#     elif guess > number:
#         print('less a little')
#     elif  guess == number:
#         print(100)

# n = 100
# sum = 0
# counter = 1
# while counter <= n:
#     sum =sum + counter
#     counter += 1
# else:
#     print('out')
# print(sum)

# sites = ['baidu', 'XIAO']
# for site in sites:
#     print (site)
#     if site == 'baidu':
#         break

# for i in range(1, 10 , 4):
#     print (i)

# list = [1, 2, 3, 4]
# m = iter(list)
# # print (next(m))
# # print (next(m))
# for ml in m:
#     print (ml)
#
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
#
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# for x in myiter:
#     print(x)
#
# def hello():
#     print('hello')
# # hello()
#
# def area(width, height):
#     return width * height
# def print_welcome(name):
#     print('welcome', name)
#
#
# s = area(2, 4)
# print (s)
# print_welcome('mi')

# def ChangeInt(a):
#     a =10
#     print (a)
# b = 2
# ChangeInt(b)
# print(b)
#
# def changeme( mylist ):
#     mylist.append([1, 2, 3, 4])
#     print(mylist)
#     return
# mylist1 = [10, 20]
# changeme(mylist1)
# print(mylist1)

# def printme( str ):
#     print (str)
#     # return
# printme ("xiao")
#
# printme(str = "2")
# def printinf(name, age):
#     print (name, age)
# printinf(name = "mi", age = '2')
# printinf(age = 12, name = 'XUE')

# def printsec(name = "we",age ):
#     print(name, age)
#     return
# printsec( age=1)
#
# def printinfo(arg1, **vartuple):
#     print(arg1, vartuple)
#     return
#
#
# printinfo(1, a = 2, b = 29, c = 30)

# def f(a, b, *, c ):
#     print(a, b, c)
# f(1, 2,c = 3)

# sum = lambda arg1, arg2: arg1 + arg2
# print (sum(10, 20))



# num = 1
# def fun1():
#     global  num
#     num = 2
#     a = 0
#     def fun2():
#         nonlocal a
#         a = 10
#     fun2()
#     print (num, a)
# fun1()
# print (num )


# s =  '332'
# print( repr(s).zfill(10))
# print(s)

# print('{}next{}'.format("bird", 'dog'))
# print('{0}next{1}'.format("mi", 'snake'))
# print("{wang}next{miao}".format(wang ='dog', miao = "star"))
# print('{0:.2f}'.format(2))
# print('%10.7f'%3.1223455556)

# table = {'Google': 1, 'Baidu': 2, 'Mi': 3}
# print('{Google},{Baidu},{Mi}'.format(**table))
# print('{0[Google]}'.format(table))

# str = input('input now')
# print(str)
#
# f = open('fileLearn.txt','w')
#
# f2 = open('/fileLearn2.txt','w')
# f3 = open('../fileLearn3.txt','w')
# f.write("xiaomr")
# f2.close()
# f3.close()
# # # f4.close()
# f1 = open('file1.txt', 'w', encoding='utf-8')
# f1.write('当前目录？\n')
# f1.write('true')
# f1.close()
#
# # macOS系统下，不推荐在根目录直接创建文件，会产生PermissionError: [Errno 13] Permission denied，但可以在一些允许读写的文件夹下面操作，如'/Users/wuliytTaotao/Desktop/file2.txt'。
# f2 = open('/file2.txt', 'w', encoding='utf-8')
# f2.write('在哪儿？\n')
# f2.write('在根目录，windows系统下就是在此文件的盘的根目录下，如E:\\file2.txt，C:\Users\Administrator\Desktop\PythonEndStudy\fileLearn.txt，本例就是在c盘')
# f2.close()
#
# f3 = open('./file3.txt', 'w', encoding='utf-8')
# f3.write('当前目录？\n')
# f3.write('yes')
# f3.close()
#
# f4 = open('../file4.txt', 'w', encoding='utf-8')
# f4.write('在哪儿？\n')
# f4.write('该.py文件所在位置的上级目录')
# f4.close()
#
# f = open('file1.txt', 'r')
#
# str = f.readline()
# print(str)
# f.close()

# f = open("./file1.txt",'w+')
#
#
# num = f.write( "Python是xiaom,i"  )
# f.close()
# print (num)
# f = open("./file1.txt",'rb+' )
# str = f.readline()
# f.seek(-1,2)
# print(f.read())
# print(f.read())
# loction1 = f.tell()
# print(str, )
# print(loction1)
#
# # 关闭打开的文件
# f.close()

# import pickle
# data1 = {'a': [1, 2, 3],
#          'b':[2, 3, 4],
#          'c':None}
# se = [1,2,3]
# se.append(data1)
# print(se)
# output = open('file01.pkl','wb')
# pickle.dump(se,output)
# output.close()
# output2 = open('file01.pkl','rb')
# data1 = pickle.load(output2)
# print(data1)
# output2.close()


# while True: print("1919")
#
# while True:
#     try:
#         x = int(input('now'))
#         break
#     except :
#         print('no')

# import sys
# try:
# f = open("./file1.txt",'rb+' )
# f = open('file1.txt', 'r')
# s = f.readline()
# i = int(s.strip("3"))
# print(i)
# f.close()
# except OSError as err:
#     print("Os{0}".format(err))
# except ValueError:
#     print('blue')
# except:
#     print("'red")

# try :
# raise NameError("mi")
# except NameError:
#     print("uu")
    # raise

# try:
#     raise KeyboardInterrupt
# finally:
#     print('you')

# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("rr")
#     else:
#         print(result)
#     finally:
#         print ('you')
# divide(2,0)

# with open ('file1.txt','r') as f:
# for line in open('file1.txt','r'):
#         print(line)

# class MyClass:
#     i = 12345
#     def f(self):
#         return 'hello'
#
# x = MyClass()
# print(x.i)
# print(x.f())

# class Complex:
#     def __init__(self, realpt, imagpart):
#         self.r = realpt
#         self.i = imagpart
#
#
# x = Complex(2, 4)
# print (x.r, x.i)

# class Test:
#     def prt(self):
#         print(self)
#         print(self.__class__)
#
# t = Test()
# t.prt()

# class people:
#     name = ''
#     age = 2
#     __weight = 0
#     def __init__(self, n, a, m):
#         self.name = n
#         self.age = a
#         self.__weight = m
#
#     def speak(self):
#         print('%sspeak'%(self.name), self.age)
#
# p = people("xiao", 1, 23)
# p.speak()
#
# class Student(people):
#     grade = 8
#     def __init__(self, n, a, m, g):
#         self.grade = g
#         self.age = a
#         self.name = n
#     def speak(self):
#         print(self.grade, self.age, self.name)
#
# s = Student("ss", 12, 11, 9)
# s.speak()

# class Site:
#     def __init__(self, name, url):
#         self.name = name
#         self.__url = url
#     def who(self):
#         print(self.name,self.__url)
#         self.__xiao()
#     def __xiao(self):
#         print("hello")
# site = Site("xiao","www.like.com")
# site.who()

# def func(a,b):
#
#     def line(x):
#         return a * x + b
#
#     return line
#
#
# line = func(6, 3)
# print(line(3))
# x = 3
#
#
# def f1():
#     x = 3
#     x = x+1
#     print (x)
#
#
# f1()
#
# for i in range(3):
#     print (i)
#
# flist = []
# for i in range(3):
#     def foo(x):
#         print (x + i)
#     flist.append(foo)
# # for f in flist:
# #     foo(2)
# foo(2)

# for i in range(3):
#     print(i)
# def foo(x):
#     print (x+i)
# foo(1)
# print(i)

# def f1():
#  list1 = []
#  for i in range(5):
#   def n(x,i=i):
#     return i+x
#     list1.append(n)
#     return list1
#     print()
# f1()(2)


#
# flist = []
# for i in range(3):
#     def foo(x,y=i): print (x + y)
#     flist.append(foo)
#
# for f in flist:
#     foo(2)


# for i in range(5):
#         def n():
#           print(i,12)
#
#         n()

# x = 1
# def b():
#     print(x)
# b()
#
# print(x)
# x = 1

# class Veter:
#     def __init__(self,a):
#         self.a = a
#     def __str__(self):
#         return '(%d)'%(self.a)
#     def __add__(self,other):
#         return  Veter(self.a + other.a)
#
# v0 = Veter(100)
# v1 = Veter(200)
#  print(v1+v0)
#
# for i in range (2,4):
#     print(i)

# import time
#
# def display_time(func):
#     def wrapper():
#         t1 = time.time()
#         func()
#         t2 = time.time()
#         print(t2 - t1)
#     return  wrapper
#
#
# def is_prime(num):
#     if num < 2:
#         return False
#     elif num == 2:
#         return True
#     else :
#         for i in range(2, num):
#             if num % i == 0:
#                 return False
#         return True
#
# @display_time
# def prime_nums():
#
#     for i in range(2,10000):
#         if is_prime(i):
#             print (i)
#
# prime_nums()

    # def prime_nums():
    #     t1 = time.time()
    #     for i in range(2, 10000):
    #         if is_prime(i):
    #             print (i)
    #     t2 = time.time()
    #     t3 = t2 - t1
    #     print (t3)




# is_prime(3)

# for j in range(2,1000):
#     if is_prime(j):
#         print(j)


# def hi(name = 'yasoob'):
#     def great():
#         return"ok"
#     def welcome():
#         return "no"
#     if name == "yasoob":
#         return great
#     else:
#         return welcome
#
# # a = hi()
# # b = a()
# # print(b)
#
# a =hi()()
# print(a)

# def hi():
#     return "hi"
# def doSomeThingBeforeHi(func):
#     print('first do')
#     print(func())
#
# doSomeThingBeforeHi(hi)

# def a_new_decorator(a_func):
#     def wrap_the_func():
#         print("yo")
#         a_func()
#         print("no")
#     return wrap_the_func
#
# @a_new_decorator
# def a_func():
#     print ('ku')
#
# # a_new_decorator(a_func)()
# a_func()
# #
# def mover(f):
#     def wrap(*args):
#         print("no use")
#         f(*args)
#     return wrap
#
#
#
# @mover
# def printr(a,b,c) :
#     print(a+b)

# c = printr(1,2,4)

# def hi(fun):
#     def inner():
#         print("Welcome " )
#         fun()
#     return inner
#
# @hi
# def hello():
#     print("hello world" )
#
# hello()

# -*- coding: UTF-8 -*-
# python3
# 1
# print ('Hello World')

# 2
# num1 = input('input fir')
# num2 = input('input sec')
# sum = float(num1) + float(num2)
# print('the {0} and {1} add is {2}'.format(num1, num2, sum))


#3
# num = float(input('the number'))
# num_aqrt = num ** 0.5
# print('%0.3f is %0.3f'%(num, num_aqrt))

#4
# a = float(input('the fir'))
# b = float(input('the sec'))
# c = float(input('the thir'))
# s = (a + b + c) / 2
# are = (s*(s-a)*(s-b)*(s-c)**0.5)
# print(are)

#5
# import random
# print(random.randint(0, 9))
#

# 6
# celsius = float(input('tem'))
# fahrenheit = (celsius * 1.8) + 32
# print('%0.2f is %0.2f' %(celsius, fahrenheit))

# 7.1
# x = input('the first')
# y = input('the sec')
# temp = x
# x = y
# y = temp
# print('{0}, {1}'.format(x, y))

#7.2
# x = input('x')
# y = input('y')
#
# x, y = y, x
#
# print(x, y)

# 8.1
# num = float(input('x'))
# if num >= 0:
#     if num == 0:
#         print('0')
#     else:
#         print('+')
# else:
#     print('-')

# 8.1

# num = float(input('x'))
# if num > 0:
#     print('+')
# elif num == 0:
#     print('0')
# else:
#     print('-')

#10
# num = int(input('x'))
# if(num % 2) == 0:
#     print('yes')
# else:
#     print('no')

#11
# num = float(input('input x'))
# if num % 4 ==0:
#     if num % 100 ==0:
#         if num % 4 == 0:
#             print ('yes1')
#         else :
#             print('no2')
#     else:
#
#         print('no1')
#
# else:
#     print('not2')

# 12
# print(max(1, 3))
# print(max([1, 4, 6]))

#13
# num = int(input("x"))
# if num > 1:
#     if num == 2:
#         print ('yes')
#     else:
#         for i in range(2, num):
#             if num % i == 0:
#                 print('no')
#                 break
#             else:
#                 print('yes')
# else:
#     print('no')

# 15
# num = int(input('x'))
# factorial = 1
# if num < 0:
#     print('no')
# elif num == 0:
#     print ('1')
# else:
#     for i in range(1, num+1):
#         factorial = factorial * i
#     print(factorial)

# 16
# for i in range(1, 10):
#     for j in range(1,i + 1):
#         print('{0} * {1} = {2}  '.format(j, i, i * j),end ="")
#     print('')

# print ('qq' ,end='\t')
# print ('qq' ,end='\t')

# 17
# nterms = int(input('x'))
#
# n1 = 0
# n2 = 1
# count = 2
# if nterms <= 0:
#     print('no')
# elif nterms == 1:
#     print (n1)
# else:
#     print(n1,"\n",n2)
#     while count < nterms:
#         print (n1 + n2)
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth
#         count +=1

# 18
# num = int(input('x'))
# sum = 0
# n = len(str(num))
#
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum = sum + digit ** n
#     temp = temp // 10
#
# if sum == num:
#     print('yes')
# else:
#     print('no')


# 19
# dec = int(input('x'))
# print(dec)
# print(bin(dec))
# print(oct(dec))
# print(hex(dec))

# 20
# c = input('str')
# a = int(input("x"))
# print(ord(c))
# print(chr(a))

# 21
# def hcf(x, y):
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#
#     for i in range(1, smaller + 1):
#         if (x % i == 0) and (y % i == 0):
#             hcf = i
#     return hcf
#
# num1 = int(input("x"))
# num2 = int(input("y"))
# print(hcf(num1,num2))

# 22
# def lcm(x, y):
#     if x >y :
#         greater = x
#     else:
#         greater = y
#     while True:
#         if (greater % x == 0) and (greater % y == 0):
#             lcm = greater
#             break
#         greater += 1
#     return lcm
#
# num1 = int(input('x'))
# num2 = int(input('y'))
# print(lcm(num1, num2))

#23
# def add(x,y):
#     return x + y
#
# def substract(x, y):
#     return x - y
# def multipy(x, y):
#     return x * y
# def divide(x, y):
#     return x / y
#
# print(1, 2, 3, 4 )
#
# choice = int(input('choice'))
# num1 = int(input('x'))
# num2 = int(input("y"))
#
# if choice == 1:
#     a = add(num1, num2)
# elif choice == 2:
#     a = substract(num1, num2)
# elif choice == 3:
#     a = multipy(num1, num2)
# else :
#     a = divide(num2, num2)
#
# print(a)

#24
# import calendar
# yi = int(input('year'))
# mm = int(input('month'))
#
# print(calendar.month(yi, mm))

#25
# def recv_fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return(recv_fibo(n-1) + recv_fibo(n-2))
#
# nterms = int(input('x'))
# if nterms <=0 :
#     print('no')
# else:
#     print('yes')
#     for i in range(0, nterms):
#
#         print (i, recv_fibo(i))
#26

# with open("file1.txt","wt") as out_file:
#     out_file.write('you')
# with open("file1.txt","rt")as in_file:
#     print(in_file.read())

#27
# str = 'xiaomi'
# print(str.isalnum())
# print(str.isalpha())
# print(str.islower())
# print(str.isspace())
# print(str.istitle())
# print(str.isupper())
#
# print(str.upper())
# # print(str.lower())
# print(str.title())
# print(str)
# print(str.capitalize())

