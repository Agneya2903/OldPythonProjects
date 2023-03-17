# txt = "Jio Net is for free"
# if "airtel" in txt:
#     print("Reliance")
# elif "Idea" in txt:
#     print("Hotspot")
# else:
#     print("Good bye")

# txt = "Jio Net is for free"
# print("idea" not in txt)
# print("Jio" not in txt)
# if "Idea" not in txt:
#     print("So Sad....")

# txt = "Jio Net is for free"
# brand ="idea"
# print(txt.upper())
# print(txt.lower())
# print(txt.strip()) #The strip() method removes any whitespace from the beginning or the end:
# print(txt.replace("Jio","Idea"))
# print(txt.split(",")) #The split() method splits the string into substrings if it finds instances of the separator:
# print(txt.replace("Jio",brand))

# txt = "My Name is Jhon , and I am {} years old"
# age = 36
# print(txt.format(age))

# txt ="{} car cost {} US Dollars in {}"
# car ="Bmw"
# price = 50000
# country ="India"
# print(txt.format(car,price,country))

#Escape Characters
# print("We Are \"North Indians\" By genetics")
# print("I love \\bmw\\audi\\jeep and Tata Cars")
# print("I Am in \n Usa")
# print("I Am in \r Usa newyork")

# txt = "ravindra is BOWLER"
# print(txt.capitalize())
# x = "36 is my AGE"
# print(x.capitalize())

# class MyClass:
#     def __len__(self):
#         return 0
# obj =MyClass()
# print(bool(obj))


# class MyClass:
#     def __len__(self):
#         return 1
# obj = MyClass()
# print(bool(obj))








# x ="Python"
# print(x[1])

# for i in "Maharashtra":
#     print(i)

# txt = "Jio Net is for free"
# print("free" in txt)
# print("airtel" in txt)

# x ="Jhon"
# print(isinstance(x,str))
# print(isinstance(x,int)) #isinstance() function, which can be used to determine if an object is of a certain data type:

# lis=[]
# for i in range(1,21):
#     if i%2==0:
#         lis.append(i)
# print(lis)


# print(list((filter(lambda i:i%2==0,range(1,21)))))

# dic={i:i*i for i in range(1,11)}
# print(dic)


str =("hello world")
print(str[::-1])


str ="Python"
reverse =""
for i in str:
    reverse = i+reverse
print(reverse)


from functools import functools
lis =(1,3,4,56,5)
n=red