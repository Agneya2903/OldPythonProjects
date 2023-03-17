# n =5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=' ')
#     for j in range(i+1):
#         print("*", end=' ')
#     for j in range(i):
#         print("*",end=' ')
#     print()


lis=[2,5,6,7,8,10]
def addition(n):
    sum =0
    for i in n:
        sum +=i
    return  sum
print(addition(lis))




# a=list((map(lambda i:i*i,range(1,11))))
# print(a)
#
# dic ={i:i**3 for i in range(1,11)}
# print(dic)

























#To find square using for loop and range function
# for i in range(1,11):
#     print("The Square of",i,"is",i**2)

# a,b,c=(22,34,88)
# if a>b and a>c:
#     print(a,"Is greatest num")
# elif b>c and b>a:
#     print(b,"is greatest num")
# else:
#     print(c,"is greatest number")


# a=int(input("enter the number"))
# b=int(input("enter the number"))
# c=int(input("enter the number"))
# def highest(a,b,c):
#     if a > b and a > c:
#         print(a, "Is greatest num")
#     elif b > c and b > a:
#         print(b, "is greatest num")
#     else:
#         print(c, "is greatest number")
# highest(a,b,c)
#


# def factorial(n):
#     if n==0:
#         return 1
#
#     else:
#         return n*factorial(n-1)
# factorial(6)

# def factorial(n):
#     if n == 0:
#        return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))