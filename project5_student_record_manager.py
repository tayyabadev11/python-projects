# Project 5 - Student Record Manager
print("      WELCOME TO STUDENT RECORD MANAGER")
students = []
total = int(input("How many students do you want to add? "))
count = 1
while count <= total:
    # Decorative Border (Nested Loop)
    for row in range(1):
        for star in range(40):
            print("*", end="")
        print()
    print("Student", count)
    name = input("Enter Student Name: ").title()
    marks = int(input("Enter Marks: "))
    attendance = int(input("Enter Attendance (%): "))
    # Bonus Marks
    marks += 5
    if marks > 100:
        marks = 100
    # Grade System
    if marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"
    # Result
    if marks >= 50:
        result = "PASS"
    else:
        result = "FAIL"
    # Scholarship
    if marks >= 80 and attendance >= 75:
        scholarship = "YES"
    else:
        scholarship = "NO"
    # Save Record in List
    student = [
        name,
        marks,
        attendance,
        grade,
        result,
        scholarship
    ]
    students.append(student)
    print("\nRecord saved successfully.")
    print("Preparing for the next student", end="")
    for i in range(3):
        print(".", end="")
    print("\n")
    count += 1
print("  STUDENT RECORDS")
number = 1
for student in students:
    print("\nStudent", number)
    print("Name         :", student[0])
    print("Marks        :", student[1])
    print("Attendance   :", student[2], "%")
    print("Grade        :", student[3])
    print("Result       :", student[4])
    print("Scholarship  :", student[5])
    if student[3] == "A":
        print("Message : Outstanding Performance!")
    elif student[3] == "B":
        print("Message : Excellent Work!")
    elif student[3] == "C":
        print("Message : Good Job! Keep Improving.")
    elif student[3] == "D":
        print("Message : You Passed. Aim Higher Next Time.")
    else:
        print("Message : Never Give Up. Practice More.")
    number += 1
print("All student records have been displayed.")
print("Thank you for using Student Record Manager.")
print("Program Finished.")