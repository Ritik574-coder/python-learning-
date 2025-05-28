# Dictinary in python 
# Dictinary are used to store data values in key:value pairs 
#they are unordeared , mutable(changable) & don't allow duplicate keys

dictnory = {"ritik" : "all","Riya":"love","Muskan":"Nuksan","Divya":"Math"}
print(dictnory)
print("This is the type of data is -->>",type(dictnory))
print(dictnory["Divya"])

# a real dictonary dat type is here  

dictnory2 = {
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
# nested dictionary 
print(dictnory2["subject"]["C"])
# print(dictnory2["sirname"]) # this valuse given error becouse thsi type of data is not exists in this data 
dictnory2["Name"] = "Riya" # dictionary is mutable you able to change keyvalues pare not key
print(dictnory2)

# how to create null type data in dictionary 

null_dict = {} # this is the null type dictionary 
print(null_dict)
print(type(null_dict))
null_dict["Name"] = "Ritik"
print(null_dict)
print(null_dict["Name"])







