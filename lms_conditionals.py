print("========LMS FEE DISCOUNT CAL=====")
student_name = input("enter student_name")
student_grade = int(input("enter student_grade (1-12)"))
tuition_fee = float(input("enter tuition_fee"))

is_Academic_topper_input = input("Academic topper ? (yes/no)")
is_Academic_topper = is_Academic_topper_input == "yes"

#initial discount set
discount = 0.0

#input validation
if 1 <= student_grade <=12:
    #process discount for cal
    print(f"processing discount for{student_name}")
    #primary discount for 9-12
    if student_grade >=9 and student_grade <=12:
        if is_Academic_topper:
            discount = 0.20
            print("asademic topper discount applied")
        else:
            discount = 0.10
            print("primary school discount applied")

    elif student_grade >=6 and student_grade <=8:
            discount = 0.05
            print("middle school discount applied")
    else:
         discount = 0.0
         print("no discount applicable for this grades")
    #match - case
    match student_grade:
        case 10:
            discount += 0.03
        case  12:
            discount += 0.05
        case _:
            discount += 0.0
    discount_amount = tuition_fee * discount
    discounted_fee = tuition_fee - discount_amount

    print("=======LMS FEE DISCOUNT CALCULATOR====")
    print("Processing discount for {student_name}")
    print(f"student name{student_name}")
    print(f"student grade{student_grade}")
    print(f"academic topper status{is_Academic_topper}")
    
    print(f"base tuition fee{tuition_fee}")
    print(f"discount amount saved{discount_amount}")
    print(f"final tuition fee{discount_amount}")

    
else:
    print(f"Invalid Grade!,please enter in between 1-12")
