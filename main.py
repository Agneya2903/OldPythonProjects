#pyhthon
# x ="Welcome to World"
# def myfunc():
#     x = "Hello Python"
#     print(x)
# myfunc()
#
# print(x)


# Declaring global variable in python
# x = "Awesome"
#
# def my_func():
#     global x
#     x = "Fantastic"
#     print("Python is ", x)
# my_func()
#
# print("Python is ", x)


# def func1():
#     a = int(input("Enter First Number: "))
#     b = int(input("Enter Second Number: "))
#     print("Multiplication of First & Second number is ", a*b)
#     print("Addition of First & Second number is ", a + b)
#     print("Substraction of First & Second number is ", a - b)
#     print("Division of First & Second number is ", a / b)
# func1()


# Program To calculate Combine score using fuction method
# def Combine_Score_Method():
#     a = int(input("Enter Total Number of Right Questions "))
#     b = int(input("Enter Total Number Of Wrong Questions "))
#     c = (a-b/4)
#     if a > 100 or a < 0 and b < 0 or b > 100:
#         print("Please enter Valid number")
#     elif a+b > 100:
#         print("Total Number of Right & Wrong Questions Exceed the Limit of 100")
#     else:
#         print("Your Combine Score Is " , c)
# Combine_Score_Method()

# Range Function
# i = range(7)
# print(i)

# Bytes function
# x = b"Hello_World"
# print(x)
# print(type(x))

# a = 12
# b = 3.25
# c = 1+8j
#
# print(type(a))
# print(type(b))
# print(type(c))
#
# d = float(a)
# e = int(b)
# f = str(c)
# print(d)
# print(e)
# print(f)

# x = y = z = "Orange"
# print(x , y , z)
# a = "oranders"
# print(len(a))

# x = "Python"
# print(x[-3])
#
# i = 5
# while i < 100:
#     print(i)
#     if i == 50:
#         break
#     i += 5

# x = "Python is awesome"
# def fun_ction():
#     x = "Programming Language"
#     print(x)
# fun_ction()
# print(x)


# Strings in python

# Example no 1
# txt = "Python is an easy language"
# if input() in txt:
#     print("Yes it is presnt")
# else:
#     print("Not Presnt")


# Example 2
# text1 = "Python Is an easy Language"
# print("hard" not in text1)
# Gives ouput True

# String slicing
# a = "Welcome to python"
# print(a[-6:])

# print(len(a))

# print(a[11:18])

# age = 36
# text = "My name is Jhon I am {} Years Old"
# print(text.format(age))

# age =int(input("Enter Your age: "))
# text = "You are {} years old"
# print(text.format(age))

# x = "Welcome To Python Programming"
#
# def my_func1():
#     x = "Python"
#     print(x)
# my_func1()
# print(x)

# def funtion1():
#     num1 = int(input("Enter First Number: "))
#     num2 = int(input("Enter Second Number: "))
#     num3 = num1+num2
#     if num3 > 100:
#         print(" There Addition is greater than 100 ,because the total is", num3)
#
#     elif num3 < 100 :
#         print("There Addition Less than Hundred , because the total is", num3)
#
#     else:
#         print("Addition Equals to 100")
# funtion1()

# a = "I Love Python"
# print(a[-7:])
# print(len(a))

# i = 2
# while i < 36:
#     print(i)
#     i+=2

# a = int(input("Enter a  number: "))
#
# if a > 100:
#     print(True)
# elif a == 100:
#     print("Value Entered is 100 only")
# else:
#     print(False)

# num1 = int(input("Enter Total number of right questions: "))
# num2 = int(input("Enter Total number of wrong questions: "))
# score = (num1-num2/4)
# if num1 and num2 < -1:
#     print("Wrong Number mentioned, please mentioned proper number")
# elif num1 + num2 > 100:
#     print("Total number of questions cross 100+ limit")
# else:
#     print("Your combine Score is: ", score)

# String slicing

# a = "Geeks for Geeks"
# print(len(a))
# #To print "For" from variable using string slicing methos;
#
# print(a[6:9])
# print(a[-9:-6])
# print(a[0:5])
# print(a[-6:])

# a = int(input("Enter num 1 "))
# b = int(input("Enter num 2 "))
# c = int(input("Enter num 3 "))
# print("The greater number among there is: ", max(a,b,c))


# x =5
# print(x>3 and x<10 and x<7)


# a = int(input("Enter The Number1: "))
# b = int(input("Enter The Number2: "))
# c = int(input("Enter The Number3: "))
#
# if a > b and a > c:
#     print("The greater among three is ", a)
# elif b > a and b > c:
#     print("The greater among three is ", b)
# elif c > a and c > b:
#     print("The greater among three is ", c)
# else:
#     print("All the numbers are equal")

# a = [input(str("Enter Fruit Name: "))]
# # b = list[a]
# if "Mango" in a:
#     print(a," is Sweet")
# elif "Tamrind" in a:
#     print(a, "is Sour")
# elif "BetterGourd" in a:
#     print(a, "is Yuckk")
# elif "Apple" in a:
#     print(a, "Is Healty")
# else:
#     print("Please Check on Google")


# x = 123
# y = x
# # print(x==y)
#
# thislist = ["apple", "banana", "cherry", "banana", "Mango", "jam", "banana","pineapple","banana"]
# for i in thislist:
#     if i == "banana":
#         thislist.remove(i)
#
# print(thislist)


# fruits = ["apple","Cherry","banana","mango"]
# newlist =[]
# for i in fruits:
#     if "a" in i:
#         newlist.append(i)
# print(newlist)
# fruits =["apple", "cherry", "mango", "banana", "coconut"]
# newlist = []
# for i in fruits:
#     if "a" in i:
#         print(newlist.append(i))
#
# print(newlist)

# fruits = ["apple","Cherry","banana","mango","Cherry", "coco", "Cherry","Cherry"]
# for i in fruits:
#     if i == "Cherry":
#         fruits.remove(i)
#
#
#
# print(fruits)

# thistuple =(12, "MYDB", 2.1, True)
# print(type(thistuple[3]))

# txt ="  banana  "
# x = txt.strip()
# print("I Love fruit",x,"Very much ")

# thistuple = ("apple", "Banana", "cherry", "Mango", "Python","orange", "kiwi", "melon")
# print(thistuple)
# thislist =list(thistuple)
# print(thislist)


# thislist = ['apple', 'Banana', 'cherry', 'Mango', 'Python', 'orange', 'kiwi', 'melon']
# print(len(thislist))
# print(thislist[3:])
# for i in thislist:
#     if 'apple' in i:
#         print(True)
#
# thislist[1:3] = ["Watermelon", "Guava"]
# print(thislist)
# thislist.insert(3,"Strawberry")
# thislist.append("DragonFruit")
# print(thislist)

# thislist =['apple', 'Watermelon', 'Guava', 'Strawberry', 'Mango', 'Python',]
# thatlist =['orange', 'kiwi', 'melon', 'DragonFruit']
#
# thislist.extend(thatlist)
# thistuple = ("Blueberry", "Rosemerry", "CustardApple")
# thislist.extend(thistuple)
# print(thislist)
# thislist.remove("Guava")
# thislist.pop(3)
# del thislist[5]
# print(thislist)


# find the greatest number among 3 numbers?

# a = 23
# b = 233
# c = 1233
# if a > b and a > c:
#     print("Print a is Greater among all")
# elif b > a and b > c:
#     print("Print b is greater among all")
# else:
#     print("C is greater among all")
#
#
#
# a = 23
# b = 233
# c = 1233
# if a > b and a > c:
#     print("Print a is Greater among all")
# elif b > a and b > c:
#     print("Print b is greater among all")
# else:
#     print("C is greater among all")

# thislist = ["apple","orange","lemon","banana","cherry","guava"]
# newlist = []
# for x in thislist:
#     if x == "banana":
#         continue
#     print(x)

#Print 1 to 10 Values
# for i in range(1,11):
#     print(i)

# print Even Numbers 1 to 100
# for i in range(1,101): (type 1)
#     if i % 2 == 0:
#         print(i)

# print Even Numbers 1 to 100
# for i in range(0,101,2):  (type2)
#     print(i)


# print Odd Numbers 1 to 100
# for i in range(1,101,2):  (type 1)
#     print(i)

# for i in range(1,101):  (type 2)
#     if i % 2 == 1:
#         print(i)







#Print 1 to 10 Square
# for i in range(1,11):
#     print(i**2)

#Print 1 to 10 Cube
# for i in range(1,11):
#     print(i**3)



# num = int(input("Enter a any number to find factorial:- "))
# factorial = 1
# if num < 0:
#     print("Invalid Number")
# elif num ==0:
#     print("The Factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print("The factorial for number",num,"is",factorial)


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# num = int(input("Enter a number: "))
#
# print("The factorial of", num, "is", factorial(num))

# def factorial(n):
#     if n ==0:
#         return 1
#     else:
#         return n * factorial(n-1)
# num = int(input("Enter the number:- "))
# print("The factorial for ",num,"is",factorial(num))


# adj = ["Red","Green","Black","Pink","Yellow"]
# noun = ["Apple","Guava","Grapes","DragonFruit","Pineapple"]
# for i in adj:
#     for j in noun:
#         print(i,j)


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# num =int(input("Enter the Number:- "))
# print("The Factorial of number" ,num, "is",factorial(num))

# for i in range(1,11):
#     print(i**2)

# thistuple =("Apple", 12, True, 3.2)
# print(type(thistuple[3]))


# thistuple =("apple","orange","banana","cherry")
# print(thistuple)
# thislist =list(thistuple)
# print(thislist)
# thislist[3] ="Kiwi"
# print(thislist)
# thistuple =tuple(thislist)
# print(thistuple)



# i = 0
# while i < 7:
#     i += 1
#     if i == 4:
#         continue
#     print(i)

# def square_func():
#     i = int(input("Enter The Number:- "))
#     print("The Square of ",i,"is",i**2)
# square_func()


# def combine_func():
#     num1 = int(input("Enter total right questions:- "))
#     num2 = int(input("Enter total wrong questions:- "))
#     score =(num1-num2/4)
#     if num1 < 0 or num2 < 0:
#         print("Invalid Number entered")
#     elif num1 > 100 or num2 > 100:
#         print("Please enter number 100 or less than 100")
#     elif num1+num2 > 100:
#         print("Error:- Either you have mentioned wrong input")
#     else:
#         print("Your Combine Score is:- ",score)
# combine_func()


# i=1
# while i<10:
#     print(i)
#     if i == 6:
#         break
#     i+=1

# i = 0
# while i <10:
#     i += 1
#     if i ==7:
#         continue
#     print(i)




# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

# for i in range(0 ,306 ,6):
#     print(i)

# def my_func(fname):
#     print(fname + " Palkhe")
# my_func("Agneya")

# def my_func(fname, lname):
#     print(fname + " "+ lname)
# my_func("Agneya", "Palkhe")


# def my_kids(*kids):
#     print("The youngest kid ",kids[1])
# my_kids("Neha","Aman","Amit","Richa","jhon","sam")

# def my_func(**kids):
#     print("She Has two kids",kids["last_kid"],"and",kids["first_kid"])
# my_func(first_kid ="Rohan", last_kid= "Radha")


# def my_func(country = "Norway"):
#     print("I am from ",country)
# my_func()
# my_func("India")
# my_func("Japan")

# def my_func(food):
#     for i in food:
#         if i ==food[3]:
#             break
#         print(i)
#
# fruits =["cherry","apple","chikoo","guava","custardapple","kiwi","jam","mango"]
# my_func(fruits)


# def my_factorial(n):
#     if n ==0:
#         return 1
#
#     else:
#         return  n * my_factorial(n-1)
# num = int(input())
# print(my_factorial(num))


# num = int(input("Enter the number:"))
# factorial = 1
# for i in range(1,num+1):
#     if num==0:
#         print(1)
#     else:
#         for i in range(1,num+1):
#             factorial = factorial*i
#             print(factorial)

# def my_func(n):
#     return lambda a : a * n
# x = my_func(4)
# print(x(9))


# n=5
#
#
# for i in range(n):
#   for j in range(i, n):
#     print('-', end=' ')
#   for j in range(i + 1):
#     print('#', end=' ')
#   for j in range(i):
#     print('&', end=' ')
#   for j in range(i, n -1):
#     print('|', end=' ')
#   for j in range(i, n - 1):
#     print('^', end=' ')
#   for j in range(i + 1):
#     print('*', end=' ')
#   for j in range(i):
#     print('*', end=' ')
#   print()


print("lorem ipsum(20)")

















