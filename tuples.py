empty_tuples = ()
print(type(empty_tuples))
print(empty_tuples)

tuple_nums = (10,20,30,40,50)
print(tuple_nums)

tuple_text = ("vijay","kumar","agurla")
print(tuple_text)

tuple_mixed = (10, "vijay", 20.5)
print(tuple_mixed)

empty_tuples = tuple()
print(empty_tuples)

#list_nums = list(10)
#print(list_nums)

one_tuple = tuple((10,))

print(one_tuple)

list_nums = [10,20,30,40,50]
tuple_nums = tuple(list_nums)
print(tuple_nums)

tuple_new = tuple(range(0,26,5))
print(tuple_new)

tuple_nums = (10,20,30,40,50)
print(tuple_nums[0])
print(tuple_nums[3])


print(tuple_nums[:])
print(tuple_nums[::])
print(tuple_nums[::2])
print(tuple_nums[::-1])

list_nums = [10,20,30,40,50]
tuple_nums = (10,20,30,40,50)
list_nums[0] = 100
print(list_nums)

list_nums[0] = 100
print(list_nums)

tuple_nums = (10,20,30,40,50)
for i in tuple_nums:
    print(i)

for i in list_nums:
    print(i,end=" ")

for i in tuple_nums:
    print(i,end="-")

tuple_nums = (10,20,30,40,50)
print(dir(tuple_nums))

location_info = {(17.8900,78.7989): "HITECH CITY"}
print(type(location_info))
