class CarModel: #Always Declare class name in CamelCase, its a protocol
    name="Bmw"
    color= "red"
    model= 2019
    speed= 180
    average= 15

    def car_function(self):
        print(self.name,"has an average of",self.average,"km/litre. And runs at speed of",self.speed,"km/hr in 10 seconds")


car_obj =CarModel()   #Always Declare object name in snakecase, its a protocol
print("This is my",car_obj.name,"car")
print("It has",car_obj.color,"color")
print("Its model was designed in year",car_obj.model)
car_obj.car_function()
class CarModel():
    def __init__(self,name,price,model,color,mob_no,speed,helpline):
        self.name =name
        self.price =price
        self.model =model
        self.color =color
        self.mob_no=mob_no
        self.speed = speed
        self.helpline = helpline
        print("contact Us:- ", self.helpline)

    def car_func(self):
        print(self.name,"has a speed of",self.speed,"km/hr")
    def contact(self):
        print("For more info Contact our number",self.mob_no)


car_obj = CarModel("BMW",50000,2019,"red",7977836829,180,"bmw@sales.com")
print("My car name is",car_obj.name,"It has color",car_obj.color)
print("Its price is",car_obj.price,"Rs")
print("Its Model released is in",car_obj.model)
car_obj.car_func()
car_obj.contact()

car_obj2 =CarModel("JeeepCompass",25000,2022,"Black",8237263108,150,"jeepcompass@sales.com")
print("My car name is",car_obj2.name,"It has color",car_obj2.color)
print("Its price is",car_obj2.price,"Rs")
print("Its Model released is in",car_obj2.model)
car_obj2.car_func()
car_obj2.contact()

















# class ListAcess:
#     def __init__(self,mylist):
#         self.mylist = mylist
#
#     def acess(self):
#         print(self.mylist)
#
# thislist = [1,23,"Python","Java",23.75, False]
# list_obj =ListAcess(thislist)
# list_obj.acess()




# class BankDetails:
#     def __init__(self,customer_name,acct_no,bank_name,branch_city):
#         self.customer_name = customer_name
#         self.acct_no = acct_no
#         self.bank_name =bank_name
#         self.branch_city = branch_city
#
#     def welcome(self):
#         print("Welcome to ",self.bank_name,"Bank",",",self.customer_name,"Your Accont Number is",self.acct_no)
#
#
# bank_obj =BankDetails("Amit Singh",520100,"SBI","Mumbai")
# print("Welcome To ",bank_obj.bank_name,"Bank")
# print("Dear",bank_obj.customer_name,"We Are Happy To help you")
# print("For Any Querry Contact Your",bank_obj.branch_city,"Branch")
# bank_obj.welcome()






























































