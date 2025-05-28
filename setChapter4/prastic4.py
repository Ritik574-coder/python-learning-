#Qusation no 1 -->> store following word in a python dictonary 
dictionary = {
    "table":["A piece of furniture","list of facts & figurs"],
    "cat":["a small animal"]
}
print(type(dictionary))
print(dictionary)

# Quastion no 2 -->> you are given a list of student for students. one classroom is required for 
# 1 subject. How meany classrooms are needed by all students.

subject1 = {"python","java","C++","python","javascript","java","python","java","C++","C"}
print(subject1)
print("Tolal classroom required is equal to -->>",len(subject1))

#write a program to enter marks of 3 subject from the user and store them in a dictionary . 
# start with an empty dictionary & add one by one. use subject as key & marks as value.
subject = {}
print(type(subject))

x = float(input("Enter your Chemistry Marks :"))
subject.update({"Chemistry":x})
y = float(input("Enter your physic Marks :"))
subject.update({"physic":y})
z = float(input("Enter your Math Marks :"))
subject.update({"Math":z})
print(subject)
dict = {
    "chemastry":99,
    "physic":90,
    "Math":100
    }
subject.update(dict)
print(subject)
# Figure out a way to store 9 & 9.0 as seperate values in the set. (you can take help of 
# built-in data type)
# firskt method 
values = {(9,9.0)}
print(type(values))
print(values)
# second method 
values1 = {9,"9.0"}
print(values1)