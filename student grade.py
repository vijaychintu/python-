def student_grade_tracker():
    print("=== Student Grade Tracker ===")

    # Collect Student Information
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")

    # Get and validate attendance
    while True:
        try:
            attendance = float(input("Enter Attendance Percentage (%): "))
            if 0 <= attendance <= 100:
                break
            else:
                print("Please enter a valid percentage between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    total_score = 0
    subject_count = 0

    # Input Subject Scores
    while True:
        try:
            score = float(input(f"Enter score for subject {subject_count + 1}: "))
            if 0 <= score <= 100:
                total_score += score
                subject_count += 1
            else:
                print("Score should be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric score.")
            continue

        cont = input("Do you want to enter another score? (yes/No): ")
        if cont.lower() != "yes":
            break

    # Calculate Average
    if subject_count > 0:
        average_score = total_score / subject_count
    else:
        average_score = 0

    # Determine Performance Level
    if average_score >= 85:
        performance = "Excellent"
    elif 70 <= average_score < 85:
        performance = "Good"
    elif 50 <= average_score < 70:
        performance = "Average"
    else:
        performance = "Needs Improvement"

    # Check Attendance
    if attendance < 75:
        attendance_status = "WARNING: Low Attendance"
    else:
        attendance_status = "OK: Attendance Satisfied"

    # Display Final Results
    print("\n=== Final Student Report ===")
    print(f"Student ID       : {student_id}")
    print(f"Student Name     : {student_name}")
    print(f"Subjects Entered : {subject_count}")
    print(f"Total Score      : {total_score}")
    print(f"Average Score    : {average_score:.2f}")
    print(f"Performance      : {performance}")
    print(f"Attendance       : {attendance}% - {attendance_status}")

# Run the tracker
student_grade_tracker()
