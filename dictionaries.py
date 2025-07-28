empty_dist = {}
print(type(empty_dist))

dist_nums = {1:100,2:200,3:300}
print(type(dist_nums))
print(dist_nums)

dict_courses = {"course1":"python","course":"java","course3":"cloud"}
print(dict_courses)

dict_mixed = {1:"python","two":2,"course":"cloud"}
print(dict_mixed)

sample_data = {(10,20):"ten"}
print(sample_data)

dict_courses = {"course1":"python","course":"java","course3":"cloud"}
print(dict_courses["course1"])
print(dict_mixed[1])

print(dir(dict_courses))

student_data = {
    "student1": {
    
        "name": "alice",
        "age": 20,
        "courses":["math","physics"]
    
    },
    "student2": {
        "name":"bob",
        "age":22,
        "courses":["chemistry","biology"]
    }
    
}