# conditional statement and how it work (if , elif , else )
# if conditional staement
age = 12 
if(age >= 18):
    print("Can vote & apply for license")
# conditional statement elif 
Light = ""
if(Light == "Red"):
    print("Stop")
elif(Light == "Green"):
    print("Go")
elif(Light == "Yellow"):
    print("Look")
else:
    print("Light is Broken")
# write code again 
age = 10
if(age >= 18):
    print("Can Vote") # Indentation 
else:
    print("can't vote")

# Prastic note conditional statment gread student besed on markes 
# marks >= 90 , gread "A"
# 90 > mark >=80 , grade = "B"
# 80 > marks >= 70 ,grade = "C"
#70 > marks , grade = "D"
Name = input("Enter Your Name :")
print("Hello Dear -",Name)
Age = int(input("Enter Your age : "))
if(Age >= 18 and Age <=31):
    print("you can able to check your marks ")
    if(Age >= 31 and Age <=18):
     print("you can't able to check your marks ")
else:
    print("you can't able to check your marks ")

Marks = float(input("Enter your total Marks :"))
if(Marks >= 90):
    Grade = "A"
elif(Marks >= 80 and Marks < 90):
    Grade = "B"
elif(Marks >= 70 and Marks < 80):
    Grade = "C"
elif(Marks > 70 and Marks < 80):
    Grade = "D"
else:
    Grade = "Not quelified"
print("Greade of the student are -->",Grade)