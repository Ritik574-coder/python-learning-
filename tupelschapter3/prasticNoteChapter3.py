'''
#Quastion -->> THREE to count the number of student with the "A" grade in the following tuple.
# tuple1 = ("A","B","C","B","C",'A','D','A','D','A')# LET'S PRACTICE
# Quastion-->> ONE write a prigramm to ask the user to entry names of their 3 favorate move & store them in a list.
movis1 = input("Enter you first favorate Movis -->")
movis2 = input("Enter you second favorate Movis -->")
movis3 = input("Enter you third favorate Movis -->")
movis_list = []
movis_list.append(movis1)
movis_list.append(movis2)
movis_list.append(movis3)
print("Your all favorate Movis List is here -->>",movis_list)
# second rulesr is here 
movis_list.append(input("Enter you first favorate Movis -->"))
movis_list.append(input("Enter you second favorate Movis -->"))
movis_list.append(input("Enter you third favorate Movis -->"))
print("Your all favorate Movis List is here -->>",movis_list)

# Quastion -->> TWO WAP to check if a list contains a palindrome of elements.(Hint: use copy() method)
list1 = [1,2,3,4,5,4,3,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")

# second not palindrome check 
list2 = [1,2,3,4,5,6,7,8,9]

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("palindrome")
else:
    print("not palindrome")'''

#Quastion -->> THREE to count the number of student with the "A" grade in the following tuple.
tuple1 = ("A","B","C","B","C",'A','D','A','D','A')
print("Thise is The type -->",type(tuple1))
print("Total time your values A is -->>",tuple1.count("A"))
print("count here and look your tuple-->>",tuple1)

# Quastion -->> Store the above valuse in a list & sort them from "A" to "D".
tuple2 = ("A","B","C","B","C",'A','D','A','D','A')
tuple2 = list(tuple2) # tuple tha usko list me convert kardiya nai me kon jay ga jayda dimag pechi kare 
print(type(tuple2))
tuple2.sort()
print("Ascinding order-->>",tuple2) 
tuple2.sort(reverse=True)
print("Discinding order -->>",tuple2)  # smar socho smar samjhe ki nahi hahahahaha