# Project 4 - Student Result System
print(" WELCOME TO STUDENT RESULT SYSTEM")
students = int(input("How many students do you want to check? "))
count = 1
while count <= students:
    # Nested Loop 
    for row in range(1):
        for star in range(40):
            print("*", end="")
        print()
    print("Student", count)
    # Taking Input
    name = input("Enter Student Name: ")
    marks = int(input("Enter Marks: "))
    attendance = int(input("Enter Attendance (%): "))
    # Arithmetic + Assignment Operator
    marks += 5
    # Marks should not be greater than 100
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
    # Pass / Fail
    if marks >= 50:
        result = "PASS"
    else:
        result = "FAIL"
    # Logical Operator + Nested if
    if marks >= 80 and attendance >= 75:
        if result == "PASS":
            scholarship = "YES"
        else:
            scholarship = "NO"
    else:
        scholarship = "NO"
    # Report
    print("\n STUDENT REPORT ")
    print("Name          :", name)
    print("Marks         :", marks)
    print("Attendance    :", attendance, "%")
    print("Grade         :", grade)
    print("Result        :", result)
    print("Scholarship   :", scholarship)
    # Motivational Messages
    if grade == "A":
        print("Outstanding! Keep up the great work.")
    elif grade == "B":
        print("Excellent work! Keep improving.")
    elif grade == "C":
        print("Good job! Keep practicing every day.")
    elif grade == "D":
        print("You passed! Aim even higher next time.")
    else:
        print("Don't give up. Practice makes you better.")
    # Loading Message
    print("\nLoading next student", end="")
    for i in range(3):
        print(".", end="")
    print("\n")
    count += 1
print(" ALL RESULTS HAVE BEEN SAVED")
print("Thank you for using the Student Result System!")
print("Keep learning and keep improving.")