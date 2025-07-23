value = 10
values = 10,20,30
print(type(value))
print(type(values))

empty_list = []
print(type(empty_list))
print(empty_list)

list_nums= [10,20,30,40,50]
print(type(list_nums))
print(list_nums)

list_courses = ["python","java","cloud"]
print(list_courses)

list_mixed = [1,2,3,4,5,"python"]
print(list_mixed)

list_nums = [10,20,30,40,50]
print(list_nums[0])
print(list_nums[-1])

print(list_nums[:])
print(list_nums[::])
print(list_nums[::2])
print(list_nums[::-1])

list_nums_1 = [10,20,30,40,50]
list_nums_2 = [10,20,30,40,50]
print(id(list_nums_1))
print(id(list_nums_2))

print(id(list_nums_1[0]))
print(id(list_nums_2[0]))

value = 10
print(id(value))

list_nums = [10,20,30,40,50]
#print(list_nums[10])

for i in list_nums:
    print(i,end=" ")
for i in list_nums:
    print(i,end="_")

list_nums = list()
print(list_nums)

list_nums = list([10])
print(list_nums)

value = 10
print(dir(value))
list_value = [10]
print(dir(list_nums))

string_value = "vijay"
print(dir(string_value))

range_values = range(6)
for i in range_values:
    print(i)

range_values_list = list(range(0,51,5))
print(range_values_list)

for i in range_values_list:
    print(i+2)

days = ["sun","mon","tue","wed","thu","fri","sat"]
print("wed" in days)
check_day = input("enter  day name in a week:")
if check_day in days:
    print(f"({check_day})")
    
