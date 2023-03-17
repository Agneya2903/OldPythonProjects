import json
dic ={
    "name":["Python","Java","R"],
    "year": 2019,
    "update": True
}

with open("sample.json","w") as f:
    json.dump(dic,f)

