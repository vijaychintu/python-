student_id = 101
student_name = "vijay"
student_age = "22"

quiz_score = 80
assignment_score = 70
exam_score = 60

student_attendence = 65

total_score = quiz_score + assignment_score + exam_score
average_score = total_score / 3

is_passed = average_score >= 75 

student_attendence = student_attendence + 1
student_attendence += 1

qualified_award = student_attendence >= 90 and is_passed

print("============")
print(f"student id: {student_id}")
print(f"student name: {student_name}")
print(f"student age: {student_age}")
print(f"total score: {total_score}")
print(f"average score: {average_score}")
print("=======student report=========")
print(f"student passed: {is_passed}")
print(f"student QUALIFIED FOR AWARD: {qualified_award}")
