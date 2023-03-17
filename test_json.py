# import json
# json_string ='{"name": "Mercedes", "model":2013 , "version":[2015,2018,2022,2023]}'
# print(type(json_string))
# json_load = json.loads(json_string)  #Convert from JSON to Python
# print(type(json_load))
# print(json_load["name"])
# print(json_load["model"])
# print(json_load["version"])
# print(json_load["version"][0])
# print(json_load["version"][0:3])
#
# json_string1 = {
#     "name":"Jhon",
#     "profession":"Software Enginneer",
#     "languages":["python","c++","java"]
# }
#
# json_dumps = json.dumps(json_string1) # convert into JSON:
# print(json_dumps)
# print(type(json_dumps))# the result is a JSON string:
#
#
#
# import  json
# j_string = '{"Company":"Apple", "Products":["Iphone","Macbook_Pro","Apple_air","I_Pod"],"Prices":[80000,150000,25000,15000]}'
# print(type(j_string))
# j_load = json.loads(j_string)
# print(j_load)
# print(type(j_load))
#
# print(j_load["Company"])
# print(j_load["Products"][0:4])
# print(j_load["Prices"])
#
# j_dumps = json.dumps(j_load)
# print(j_dumps)
# print(type(j_dumps))
#
# json_dict = {"Company":"Apple",
#              "Products":["Iphone","Macbook_Pro","Apple_air","I_Pod"],
#              "Prices":[80000,150000,25000,15000]
#              }
#
# with open("loading.json","w") as f:
#     json.dump(json_dict,f)
#
#
