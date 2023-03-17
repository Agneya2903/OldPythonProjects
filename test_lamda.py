#Write a function to print the number divisible by 5,using filter function
num =list(filter(lambda i:i%5==0,range(1,51)))
print(num)

#Write a map function to print the numbers square by using map functions
num = [3,5,6,7,8]
square=list(map(lambda i:i*i,num))
print(square)







# from functools import reduce
# lis =[3,4,5,6,7,8,9]
# add =(reduce(lambda x,y:x+y,lis))
# cond =(reduce(lambda x,y:x if x>y else y,lis))
# print(add)
# print(cond)
#to find cube using lamda function.

# cube=lambda y:y*y*y

#program to find factorial using lamda function

# factorial =lambda n: 1 if n==0 else n*factorial(n-1)
# print(factorial(5))
#
#
# def function(n):
#     return lambda x:x*n
#
# my_dubler =function(2)
# my_tripler = function(3)
# print(my_dubler(5))
# print(my_tripler(7))

#filtering out even number through filer method vvimp
# thislist =[1,2,3,4,5,6,7,8,9,10]
# z = list(filter(lambda x:x%2==0,thislist))
# print(z)

#different method
# n = list(filter(lambda x:x%2==0,range(1,21)))
# print(n)

#Map Method vvimp
# tup = (4,5,6,7,8,9,10,11)
# s =list(map(lambda x:x+1, tup))
# print(s)
#
# cube =tuple(map(lambda i:i**3,range(1,11))) #finding cube using map function
# print(cube)
#
# odd_num = list(filter(lambda i:i%2 ==1,range(1,11))) #finding odd numbers using fillter function
# print(odd_num)

