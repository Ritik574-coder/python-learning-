# Lists in Python 
# A built_in data type that stores set of values
#it can store elements of different types (integer,float,string,etc.....)
# it's not batter to store data becouse its not change 
marks1 =89.8
marks2 =87.8
marks3 =76.8
marks4 =78.8
marks5 =56.8
marks6 =76.8
marks7 =89.8
# right rule using list data type 
marks = [98,98,78,67,56,87,98.76,98.76]
print(type(marks))
print(marks)
print(marks[7])
# slicing if list starting and ending index are not included
# positive index 
print(marks[1:4])
# length of the list 
print(len(marks))
# negative index
print(marks[-5:-1])
print(marks[0])
marks[0] = 98.09
print(marks)
print(marks[0])


