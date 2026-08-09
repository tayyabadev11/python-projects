# Project 4 - Student Result System
print("===== Welcome to Student Result System =====")
# Get the number of students
students = int(input("How many students do you want to check? "))
count = 1
while count <= students:
    # Display separator
    for row in range(1):
        for star in range(40):
            print("*", end="")
        print()
    print("Student", count)
    # Get student information
    name = input("Enter Student Name: ")
    marks = int(input("Enter Marks: "))
    attendance = int(input("Enter Attendance (%): "))
    # Add bonus marks
    marks += 5
    # Limit marks to a maximum of 100
    if marks > 100:
        marks = 100
    # Determine grade
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
    # Determine pass or fail
    if marks >= 50:
        result = "PASS"
    else:
        result = "FAIL"
    # Determine scholarship eligibility
    if marks >= 80 and attendance >= 75:
        if result == "PASS":
            scholarship = "YES"
        else:
            scholarship = "NO"
    else:
        scholarship = "NO"
    # Display student report
    print("\n===== Student Report =====")
    print("Name        :", name)
    print("Marks       :", marks)
    print("Attendance  :", attendance, "%")
    print("Grade       :", grade)
    print("Result      :", result)
    print("Scholarship :", scholarship)
    # Display motivational message
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
    # Loading message
    print("\nLoading next student", end="")
    for i in range(3):
        print(".", end="")
    print()
    count += 1
print("\n===== All Student Records Processed =====")
print("Thank you for using the Student Result System!")
