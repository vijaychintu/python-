print("="*30)
print("LMS grade tracking system")
print("="*30)

student_id_valid = False
while not student_id_valid:
    student_id = input("enter your id")
    if student_id.isdigit():
        student_id = int(student_id)
        if student_id > 0:
            student_id_valid = True
        else:
            print("Please enter a positive number or above zero")
    else:
        print("please enter numbers only,other characters not allowed ")
#print(f"your id:{student_id}")
institue_code = "DE-"
formatted_id =institue_code+"STU"+str(student_id).zfill(5)
print(formatted_id)
student_name_valid = False
while not student_name_valid:
    student_name = input("Enter your full name:")
    student_name = student_name.strip().title()
    #print(student_name)
    name_check = student_name.replace(" ","")
    if name_check.isalpha() and len(student_name) >=3:
        student_name_valid = True
        print("Welcome,"+student_name)
    else:
        if not name_check.isalpha():
            print("name should contain only letters and spaces")
        elif len(student_name) < 3:
            print("name should contain atleast 3 characters")
name_parts = student_name.split()
first_name = name_parts[0].lower()
print(first_name)
student_email = first_name + "."+str(student_id)+"@edify.edu"
print(student_email)
base_course_fee_valid = False
while not base_course_fee_valid:
    base_course_fee = input("enter base course fee:")
    if base_course_fee.isdigit():
        base_course_fee = int(base_course_fee)
        if base_course_fee > 0:
            base_course_fee_valid = True
        else:
            print("enter course fee above zero or positive number")
    else:
        print("please enter numbers only,other characters not allowed")
discount = 0
description = input("enter description")
description = description.lower()

if "reference" in description:
    discount+= 5000
if "scholarship" in description:
    discount+= 7000
if "promo" in description:
    discount+= 3000

final_fee = base_course_fee - discount
print("="*30)
print("Fee details")
print("="*30)
print(f"Actual fee: {base_course_fee}")
print(f"discount given: {discount}")
print(f"final fee to pay: {final_fee}")

