# Project 9 - Smart Student Record Analyzer
print(" SMART STUDENT RECORD ANALYZER")
try:
    # Student Information
    name = input("Enter Student Name: ").title()
    age = int(input("Enter Student Age: "))
    city = input("Enter Student City: ").title()
    marks = int(input("Enter Student Marks: "))
    # Check Marks
    if marks < 0 or marks > 100:
        raise ValueError
    # Grade
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
except ValueError:
    print("\nError: Please enter valid information.")
    print("Age and Marks must be numbers.")
    print("Marks must be between 0 and 100.")
else:
    file = open("student_analysis.txt", "w")
    file.write(" SMART STUDENT RECORD\n")
    file.write("Student Name : " + name + "\n")
    file.write("Age          : " + str(age) + "\n")
    file.write("City         : " + city + "\n")
    file.write("Marks        : " + str(marks) + "\n")
    file.write("Grade        : " + grade + "\n")
    file.write("Result       : " + result + "\n")
    file.close()
    print("\nStudent record saved successfully!")
    file = open("student_analysis.txt", "r")
    saved_record = file.read()
    file.close()
    print("SAVED STUDENT RECORD")
    print(saved_record)
    print("Record loaded successfully!")
finally:
    print("Student record process completed.")
    print("Thank you for using the program!")
print("PROGRAM CLOSED")