# simple conditionals check ----> Boolean
# 5 > 2 ---> True
# 2 > 5 ----> False
if 5>2:
    print("5 is greater than 2")
    print("next statement")
    #if statement
  #  if conditions:
  #    statement
num = 5
if num > 0:
    print("positive number")
#tell me condition to check if the given number is in range
#10-20
num = 12
if num>=10 and num<=20:

    print(f"The number{num} is in range")

#if-else 
#if condition:
# statement
#else:
#statements
num = 10
if num > 0:
    print("positive number")
else:
    print("negative number")
num = -10
if num > 0:
    print("positive number")
else:
    print("negative number")

#vote app
age = 15
if age >=18:
    print("you can vote")
else:
    print("you cant vote")

age = 22
if age >=18:
    print("you can vote")
else:
    print("you cant vote")

#input function demo
# Input function demo
name = input("Enter your name: ")

age = input("Enter your age: ")  # This is a string
print(f"Welcome: {name}, your age is {age}")

age = int(input("Enter your age: "))  # Converts input to integer
print(type(age))


marks = int(input("enter your marks:"))
if marks >= 90:
    print("A")

elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
elif marks >= 40:
    print("E")
elif marks >= 30:
    print("F")
else:
    print("FAIL")

has_id = True
age = int(input("enter your age:"))
if age >= 18:
       print("you are allowed to voting center")
else:
    print("you cannot vote")

age = int(input("enter your age:"))
nationality = input("enter your nationaliy:")
if age >= 18 and nationality == "indian":
    print("you can vote")
else:
    print("you cant vote")


#match-case syntax
#    choice =2
#   match choice:
#        case 1:
#           print("one")
#       case 2:
#           print("two")
#        case 3:
#            print("three")
#       case _:
#           print("invalid")



        

       





