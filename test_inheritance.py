class India:
    def capital(self):
        print("Capital Of India Is New Delhi")
    def language(self):
        print("There are 22 offical languages in india")

class USA:
    def capital(self):
        print("Capital Of USA Is Washington D.C")
    def language(self):
        print("English is an offical language of USA")

obj1= India()
obj2 =USA()
for country in (obj1,obj2):
    country.capital()
    country.language()































# class Parent:
#     def mom(self):
#         print("This is from mom parent:-")
#
#     def dad(self):
#         print("This is from dad parent:-")
#
# class Child(Parent):
#     def son(self):
#         print("This from son child:-")
#
# child_obj =Child()
# child_obj.mom()
# child_obj.dad()
# child_obj.son()
#
# parent_obj =Parent()
# parent_obj.dad()
# parent_obj.mom()







# class Square:
#     def square_fuct(self):
#         for i in range(1,11):
#             print("The Square of",i,"is",i**2)
# class Cube:
#     def cube_fuct(self):
#         for i in range(1,11):
#             print("The cube of ",i,"is",i**3)
#
# class Acess(Square,Cube):
#     def access_fuct(self):
#         print("This is Acess")
#
# obj = Acess()
# obj.square_fuct()

# class Grandfather:
#     def __init__(self,name):
#         self.name = name
#     def get_name(self):
#         return self.name
#
# class Father(Grandfather):
#     def __init__(self,name,age):
#         Grandfather.__init__(self,name)
#         self.age = age
#     def get_age(self):
#         return self.age
#
# class Child(Father):
#     def __init__(self,name,age,address):
#         Father.__init__(self,name,age)
#         self.address = address
#     def get_address(self):
#         return self.address
#
# obj =Child("Python",32,"Mumbai")
# print(obj.name)
# print(obj.age)
# print(obj.address)

































