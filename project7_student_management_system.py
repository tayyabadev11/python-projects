# Project 7 - Student Management System
print("===== Student Management System =====")
students = []
# Calculate student grade
def calculate_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


# Calculate pass or fail result
def calculate_result(marks):
    if marks >= 50:
        return "PASS"
    else:
        return "FAIL"


# Check scholarship eligibility
def check_scholarship(marks, attendance):
    if marks >= 80 and attendance >= 75:
        return "YES"
    else:
        return "NO"


# Get the number of students
total_students = int(input("How many students do you want to add? "))

count = 1

while count <= total_students:

    # Display decorative border
    for row in range(1):
        for star in range(45):
            print("*", end="")
        print()

    print("Student", count)

    # Get student information
    name = input("Enter Student Name: ").title()
    age = int(input("Enter Age: "))
    city = input("Enter City: ").title()
    marks = int(input("Enter Marks: "))
    attendance = int(input("Enter Attendance (%): "))

    # Add bonus marks
    marks += 5

    # Limit marks to a maximum of 100
    if marks > 100:
        marks = 100

    # Call functions
    grade = calculate_grade(marks)
    result = calculate_result(marks)
    scholarship = check_scholarship(marks, attendance)

    # Tuple
    favourite_subjects = (
        "Python",
        "Database",
        "AI",
        "Python"
    )

    print("\nFavourite Subjects:", favourite_subjects)
    print(
        "Python appears",
        favourite_subjects.count("Python"),
        "times"
    )
    print(
        "Database Index:",
        favourite_subjects.index("Database")
    )

    # Set
    skills = {"Python", "Communication", "Python"}
    skills.add("Problem Solving")
    skills.add("Team Work")

    if "Communication" in skills:
        skills.remove("Communication")

    print("\nStudent Skills:", skills)

    # Dictionary
    student = {
        "Name": name,
        "Age": age,
        "City": city,
        "Marks": marks,
        "Attendance": attendance,
        "Grade": grade,
        "Result": result,
        "Scholarship": scholarship
    }

    # Save record in list
    students.append(student)

    print("\nStudent record saved successfully.")

    # Loading message
    print("Preparing next student", end="")
    for i in range(3):
        print(".", end="")
    print("\n")

    count += 1


# Display all student records
print("===== All Student Records =====")

student_number = 1

for student in students:

    print("\nStudent", student_number)

    # Display dictionary information
    for key, value in student.items():
        print(key, ":", value)

    # Display performance message
    if student["Grade"] == "A":
        print("Message: Outstanding Performance!")
    elif student["Grade"] == "B":
        print("Message: Excellent Work! Keep It Up.")
    elif student["Grade"] == "C":
        print("Message: Good Job! Keep Improving.")
    elif student["Grade"] == "D":
        print("Message: You Passed! Aim Higher Next Time.")
    else:
        print("Message: Don't Give Up. Keep Practicing.")

    # Display scholarship status
    if student["Scholarship"] == "YES":
        print("Congratulations! You are eligible for a scholarship.")
    else:
        print("Scholarship Status: Not Eligible")

    student_number += 1


print("\nTotal Students:", len(students))
print("\nThank you for using the Student Management System.")
print("All student records have been saved successfully.")
print("Keep learning, keep practicing, and keep improving.")
print("Program Finished Successfully.")
