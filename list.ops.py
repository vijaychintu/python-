list_nums = [10,20,30,40,50]
print(list_nums)
list_nums.append(60)
print(list_nums)
list_nums.append([70,80])
print(list_nums)
list_nums.append("vijay")
print(list_nums)

list_nums.append(60)
list_nums.append("vijay")
print(list_nums)

list_nums = [10,20,30,40,50]
list_nums.extend([60])
print(list_nums)

list_nums.extend([70,80])
print(list_nums)
list_nums.extend("vijay")
print(list_nums)

#list_nums.extend([70,80],[90,100])


list_nums = [10,20,30,40,50]
print(list_nums)
list_nums.insert(1,20)
print(list_nums)

list_nums.insert(10,20)
print(list_nums)

list_nums.insert(0,5)
print(list_nums)

list_nums[0] = 15
print(list_nums)

list_nums = [10,20,30,40,50]
print(list_nums)
list_nums.pop()
print(list_nums)

list_nums = [10,20,30,40,50]
print(list_nums)
list_nums.pop(2)
print(list_nums)

list_nums = [10,20,30,40,50]
print(list_nums)
#list_nums.pop(10)
print(list_nums)


list_nums = [10,20,30,40,50]
print(list_nums)
list_nums.remove(20)
print(list_nums)
#list_nums.remove(60)
print(list_nums)

list_nums = [10,20,30,40,50]
print(list_nums)
list_nums.clear()
print(list_nums)

list_nums = [10,20,30,40,20,10,20,10,20,10]
print(list_nums)
print(list_nums.index(40))
print(list_nums.index(20,4,8))

list_nums = [10,20,30,40,20,10,20,10,20,10]
print(list_nums.count(50))

list_nums = [10,20,30,40,50]
print(list_nums)
backup_list_nums = list_nums.copy()
print(backup_list_nums)
backup_list_nums.append(60)
print("original:",list_nums)
print("updated:",backup_list_nums)

list_nums = [10,20,30,40,50]
print(list_nums)

backup_list_nums_soft = list_nums
backup_list_nums_soft.append(60)

print("original:",list_nums)
print("updated:",backup_list_nums_soft)

list_nums = [10,20,30,40,50]
print(list_nums)
print(list_nums.reverse())
print(list_nums)

list_nums = [10,20,30,40,50]
print(list_nums)
print(list_nums[::-1])
print(list_nums)

list_nums = [10,30,20,50,40]
print(list_nums)
print(list_nums.sort())
print(list_nums)

print(list_nums.sort(reverse=True))
print(list_nums)
print(list_nums.sort(reverse=False))
print(list_nums)

list_text = ["hi","abc","zero","vijay"]
print(list_text)
print(list_text.sort())
print(list_text)

