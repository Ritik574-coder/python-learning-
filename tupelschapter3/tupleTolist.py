# how to insert data in tuple data tuble is immutable so wi don't append data in python dut 
# one rule is work change your data in tuple to list type and insert data and again change list
tup = ("ritik","riya","divya","muskan","florida","sonaryta","karl-x")
list = list(tup)
list.append("ritik")
tup = tuple(list)
print(tup)
# index method in tuple 
print(tup.index("muskan"))
# count method in tuple 
print(tup.count("ritik"))