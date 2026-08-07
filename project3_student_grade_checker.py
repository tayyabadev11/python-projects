# Project 3 - Student Grade Checker
print("      STUDENT GRADE CHECKER")
# Taking Input
student_name = input("Enter Student Name: ")
marks = int(input("Enter Student Marks: "))
# Bonus Marks (Assignment Operator)
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
# Result
if marks >= 50:
    result = "PASS"
else:
    result = "FAIL"
# Comparison Operator
passed = marks >= 50
# Logical Operator
scholarship = marks >= 80 and result == "PASS"
# Display Result
print("  STUDENT REPORT")
print("Student Name        :", student_name)
print("Final Marks         :", marks)
print("Grade               :", grade)
print("Result              :", result)
print("Passed              :", passed)
print("Scholarship Eligible:", scholarship)
if scholarship:
    print("Excellent! You are eligible for a scholarship.")
elif result == "PASS":
    print("Congratulations! Keep working hard.")
else:
    print("Don't give up. Practice and try again!")
print("Thank you for using the Student Grade Checker!")
