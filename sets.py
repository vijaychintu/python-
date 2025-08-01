empty_set = {}
print(type(empty_set))

empty_set = set()
print(type(empty_set))
list_nums = [10,20,30,40,50,10,20]
print(list_nums)
tuple_nums = (10,20,30,40,50,10,20)
print(tuple_nums)
set_nums = {10,20,30,40,50,10,20}
print(set_nums)
#print(set_nums[0])

obj1 = [1,2,3]
print(hasattr(obj1,'__getitem__'))
obj2 = {1,2,3}
print(hasattr(obj2,'__getitem__'))
set_nums = {10,20,30,40,50,10,20}
print(dir(set_nums))

for i in set_nums:
    print(i)

set_nums = {10,20,30,40,50,10,20}
print(set_nums)
set_nums.add(60)
print(set_nums)

set_nums.add((70,80))
print(set_nums)

set_nums = {10,20,30,40,50,10,20}
print(set_nums)
set_nums.update([70,80])
print(set_nums)

set_nums.update({90,100})
print(set_nums)
set_nums = {10,20,30,40,50,10,20}
set_nums.remove(10)
print(set_nums)
set_nums = {10,20,30,40,50,10,20}
set_nums.discard(100)
print(set_nums)

set_nums = {10,20,30,40,50,10,20}
print(set_nums)
removed_element = set_nums.pop()
print(removed_element)
set_nums.add(removed_element)
print(set_nums)

set_nums = {10,20,30,40,50,10,20}
print(set_nums)
set_nums.clear()
print(set_nums)

set_nums = {10,20,30,40,50,10,20}
print(set_nums)
removed_element = set_nums.pop()
print(removed_element)
set_nums.add(removed_element)
print(set_nums)

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
s3 = s1.union(s2)
print(s1.union(s2))

s4 = s1 | s2
print(s4)

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
s3 = s1.intersection(s2)
print(s1.intersection(s2))
print(s3)


s4 = s1 | s2
print(s4)
print(s1)
print(s2)


s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
s3 = s1.intersection(s2)
print(s1.intersection(s2))
print(s1)
print(s2)


s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
s3 = s1.difference(s2)
print(s1.difference(s2))
print(s1)
print(s2)
print(s2.difference(s1))
print(s1-s2)
print(s2-s1)

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
s3 = s1.difference_update(s2)
print(s1.difference_update(s2))
print(s1)
print(s2)
print(s2.difference_update(s1))
print(s1-s2)
print(s2-s1)

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference_update(s2))
print(s1)
print(s2)
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference_update(s2))
print(s1 ^ s2)
print(s1)
print(s2)

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference_update(s2))
print(s1)
print(s2)

s1 = {10,20,30,40,50}
s2 = {30,40,50}
s3 = {30,40,50,60}
print(s2.issubset(s1))
print(s3.issubset(s1))

s1 = {10,20,30,40,50}
s2 = {30,40,50}
print(s2.issuperset(s1))
print(s1.issuperset(s2))


s1 = {10,20,30,40,50}
s2 = {30,40,50}
s3 = {80,70,60}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))


s1 = {10,20,30,40,50}
s1.add(60)
print(s1)
fs1 = frozenset({10,20,30,40,50})
print(type(fs1))
print(fs1)