fruits = {"a":"apple","b":"banana"}
print(fruits)

fruits["c"] = "cherry"
print(fruits)

fruits["a"] = "apricot"
print(fruits)

empty_dict = dict()
print(empty_dict)
print(type(empty_dict))

person_dict = dict(name="Ravi",age=30,city="hyd")
print(person_dict)
print(fruits)

for i in fruits:
    print(i)

print(dir(fruits))
fruits = {"a":"apple","b":"banana"}
print(fruits)

fruits.update({"c":"cherry"})
print(fruits)

fruits.update({"a":"apricot"})
print(fruits)

fruits.update({"a":"apple","d":"dragon fruit"})

print(fruits)

fruits.pop("b")
print(fruits)

fruits.clear()
print(fruits)

print(fruits)

dict_nums = {1:100,2:200,3:300,4:400}
dict_courses = {"course1":"python","course2":"java","course3":"cloud"}
print(dict_nums[1])
print(dict_courses["course2"])

print(dict_nums.get(1))
print(dict_courses.get("course2"))
print(dict_courses.get("course3"))
print(dict_courses.get("course4","upcoming course"))

dict_courses = {"course1":"python","course2":"java","course3":"cloud"}
print(dict_courses.keys())

keys_courses = dict_courses.keys()
for i in keys_courses:
    print(i,end=" ")

dict_courses = {"course1":"python","course2":"java","course3":"cloud"}
print(dict_courses.values())
values_courses = dict_courses.values()
for i in values_courses:
    print(i,end=" ")


dict_courses = {"course1":"python","course2":"java","course3":"cloud"}
print(dict_courses.items())

keys_values_courses = dict_courses.items()
for i in keys_values_courses:
    print(i,end=" ")

for key in dict_courses.keys():
    print(i,end=" ")


for values in dict_courses.values():
    print(i,end=" ")


dict_courses = {"course1":"python","course2":"java","course3":"cloud"}
print(dict_courses)

dict_courses_copy = dict_courses.copy()
print(dict_courses_copy)

dict_courses_copy["courses3"] = "devops"
print(dict_courses_copy)
print(dict_courses)

dict_courses = {"course1":"python","course2":"java","course3":"cloud"}
dict_courses_copy_soft = dict_courses
dict_courses_copy_soft["course3"] = "devops"
print(dict_courses_copy_soft)
print(dict_courses)

dict_courses = {"course1":"python","course2":"java","course3":"cloud"}
print(dict_courses)
dict_courses.setdefault("courses2","devops")
print(dict_courses)
values = dict_courses.setdefault("course2","devops")
print(values)
print(dict_courses)


dict_courses = {"course1":"python","course2":"java","course3":"cloud"}
print(dict_courses)
value = dict_courses.setdefault("course4","devops")
print(values)
print(dict_courses)


