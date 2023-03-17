# x =str(2)
# print(type(x))
# y=int(2.45)
# print(type(y))

# x,y,z= "orange","apple","mango"
# print(x)
# print(y)
# print(z)

# x=y=z ="orange"
# print(x)
# print(y)
# print(z)

# fruits =["apple","orange","cherry"]
# a,b,c = fruits
# print(a)
# print(b)
# print(c)

#global variable
# x = "python"
# def my_func():
#     print("I love",x)
# my_func()

# x ="python"
# def my_func():
#     x ="java"
#     print("I love",x)
# my_func()
# print("I love my",x)

# def my_func():
#     global x
#     x ="python"
# my_func()
# print(x,"is awsome")

# x="java"
# def my_func():
#     global x
#     x ="python"
# my_func()
# print(x,"is awesome")

# n =dict(Name="Jhon",Age=34)
# print(n)

#vvimp
# import random
# print(random.randrange(1,100))

# x =5
# print(complex(x))
# y =4
# z=5
# print(complex(y,z))

#casting
# print(type(str(3)))
# print(float(4))
# print(int(4.2))
# print(int("45"))

# lis =[33,87,987,999]
# print(max(lis))
# print(min(lis))

#Module1
# lis =[]
# num = int(input("Enter the number to define max length of list:- "))
# for i in range(1,num+1):
#     element=int(input("enter the numbers to add in the particular list:"))
#     lis.append(element)
# print("The Numbers Added in the list are as follows:-",lis)
# print("The Maximum number in list is",max(lis))
# print("Second maximum number is",max(lis)-1)
#
# #Module2
# even_list=[]
# odd_list=[]
# for i in lis:
#     if i%2==0:
#         even_list.append(i)
#     else:
#         odd_list.append(i)
# print("Even list is,",even_list)
# print("Maximum even number is ",max(even_list))
# print("Odd list is",odd_list)
# print("Maximum odd number is:-",max(odd_list))

lis =[]
num = int(input("Enter the number to decide the length of the list:-"))
for i in range(1,num+1):
    element = int(input("Enter the numbers as per the length  assigned before "))
    lis.append(element)
print("The numbers Added are ",lis)

even_list =[]
odd_list =[]
for i in lis:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)












































