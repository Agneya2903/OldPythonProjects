# 1.)1. Check if a list contains an element

# thislist=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# if "cherry" in thislist:
#     print("Yes Its there in the list")


#2. Is a list mutable?
# thislist=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(id(thislist))
# thislist.append("guava")
# print(thislist)
# print(id(thislist))

#3. Does a list need to be homogeneous/Hetrogeneous?
#Can be both
# list_homo=["a","b","c"]
# list_hetro=[1,2.1,"abc",True,["abc",123,2.1,False]]
# print(list_hetro[4])

#4. What is the difference between append and extend?

# list_hetro=[1,2.1,"abc",True,["abc",123,2.1,False]]
# list_homo=["a","b","c","string"]
# list_hetro.append("Hello")
# print(list_hetro)
# print(id(list_hetro))
# list_hetro.extend(list_homo)
# print(list_hetro)
# print(id(list_hetro))

#5. What does “del” do?
# list_hetro=[1,2.1,"abc",True,["abc",123,2.1,False]]
# del list_hetro[4]
# print(list_hetro)

#6. What is the difference between “remove” and “pop”?

# list_hetro=[1,2.1,"abc",True,False,["abc",123,2.1,False]]
# list_hetro.remove("abc")
# print(list_hetro)
# list_hetro.pop(2)
# print(list_hetro)



# thislist =[1,True]
# thislist.remove(True)
# print(thislist)
#
# thatlist =[True,1]
# thatlist.remove(True)
# print(thatlist)


mylist=["cat","dog","rat","cat","cat","lion"]
print(mylist.index("rat"))
print(set(mylist))




















