#first WAP to check if a number enterd by the user is odd or even
Number = float(input("Enter Your Number :"))
if(Number %2 == 0 ):
    print("Youre Number is Even")
elif(Number %2 != 0):
    print("Youre Number is Odd")
# secent is batter then first
Number = float(input("Enter your number: "))

# Check if the number is actually an integer
if Number.is_integer():
    if int(Number) % 2 == 0:
        print("Your number is Even")
    else:
        print("Your number is Odd")
else:
    print("This is not a whole number, so it can't be classified as odd or even.")

# i prastic like second code 
num = float(input("Enter your Number :"))
if num.is_integer():
    if int(num) %2 == 0 :
        print("your Number is even")
    else:
        print("Your Number is Odd")
else:
    print("This is not a whole number , so it can't be classified as odd or even.")
