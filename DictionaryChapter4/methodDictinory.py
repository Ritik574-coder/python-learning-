# Dictionary Methods 
dictnory = {
    "Name":"Ritik",
    "Age" : 19,
    "is_adult": True,
    "marks": 99.90,
    "subject":{"python" : 99,
               "java" : 99.87,
               "R" : 97.87,
               "C" : 96.98,
               "C++" : 98.98
        }
}
# myDict.keys() returns all keys 
print(dictnory.keys())
print(list(dictnory.keys()))
print(len(list(dictnory.keys())))
# myDict.values Return all values 
print(dictnory.values())
print(list(dictnory.values()))
# myDict.items() return all (key,values) paires as tuples 
print(dictnory.items())
print(list(dictnory.items()))
dictnory = list(dictnory.items())
print(dictnory[0])
# myDict.get("key") returns all key according to value
dictnory = dict(dictnory)
print(dictnory)
print(type(dictnory))
# print(dictnory["Name2"])  -->> error becouse this value not exists  
# print(dictnory.get("Name2")) -->> None becouse this value not exists
print(dictnory["Name"])   
print(dictnory.get("Name")) 
# myDict.update(newDict) inserts the spacified items to the dictonary
dictnory.update({"city":"Gujrat","patner":"riya"})
print(dictnory)
# Rules no second 
new_dict = {"city":"delhi",} # dictionary duplicate valuse ko print nahi karta hai agar ik key me do valus diya gay to dictionary old valuse ko replace kar deta hai 
dictnory.update(new_dict) 
print(dictnory)
