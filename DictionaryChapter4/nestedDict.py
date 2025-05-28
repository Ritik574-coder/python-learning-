# a  dictonary data type is here  
# nested dictionary 
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
print("Nested in dictinory-->>",dictnory2["subject"]["C"])
print(dictnory2["subject"])
print(dictnory2)