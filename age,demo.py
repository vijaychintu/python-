#sample code without match-case or simply elif ladder
age = 25

if age == 0 or age == 1 or age == 2 or age == 3 or age == 4:
    category = "Toddler"
elif age == 5 or age == 6 or age == 7 or age == 8 or age == 9 or age == 10 or age == 11 or age == 12:
    category =  "child"
elif age == 13 or age == 14 or age == 15 or age == 16 or age == 17 or age == 18 or age == 19:
    category = "Teenager"
elif age == 20 or age == 21 or age == 22 or age == 23 or age == 24 or age == 25 or age == 26:
    category = "Young adult"
else:
    category = "adult"

print(category)

#using mach-case
age = 4

match age:
    case 0 | 1 | 2 | 3 | 4:
        category = "Toddler"
    case 5 | 6 | 7 | 8 | 9 | 10 | 11 |12:
        category = "child"
    case _:
        category = "Adult"
print(category)

#using range()
if age in (0,1,2,3,4):
    category = "Toddler"
elif age in range(5,13):
      category =  "child"
elif age in range(13,20):
     category = "Teenager"
elif age in range(20,27):
     category = "Young adult"
else:
    category = "adult"

print(category)
     