SYSTEM_INFO = ("LMS Students portal","v1.0","Edify University")
ADMIN_INFO = ("admin@edify.ai","+91-9876543210","201")

print("="*50)
print(f"welcome to {SYSTEM_INFO[0]} {SYSTEM_INFO[1]}")
print(f"Developed to {SYSTEM_INFO[2]} students")
print("="*50)

students = {}
while True:
    print("Enter choose an option:")
    print("1.Add student")
    print("2.Modify student")
    print("3.Delete student")
    print("4.List all students")
    print("5.exit application")

    choice = input("Enter your choice(1-5):")
    if choice == "1":
        print(f"performing choice 1 operation")
        student_id = input("enter student id:")
        if student_id in students:
            print("student already exists")
        else:
            name = input("enter student name:").strip().title()
            scores = []
            while True:
                score_input = input("enter a score or type done")
                if score_input == "done":
                    break
                if score_input.isdigit():
                    score = int(score_input)
                    if 0 <= score <= 100:
                        scores.append(score)
                    else:
                        print("Invalid score, only 0-100")
                else:
                    print("Ivalid score,only digits allowed")


            skills = set()
            while True:
                skill_input = input("enter a skill or type done")
                if skill_input == "done":
                    break
                skills.add(skill_input.strip().title())

            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills,

            }
            print("student added successfully")
            print(students)




    elif choice == "2":
        print(f"performing choice 2 operation")
    elif choice == "3":
        print(f"performing choice 3 operation")
    elif choice == "4":
        print(f"performing choice 4 operation")
    elif choice == "5":
        print(f"performing choice 5 operation")
        break
    else:
        print(f"Ivalid choice select only (1-5) ")

    

    








