# Project 3 - Student Grade Checker
print("===== Student Grade Checker =====")
# Get student information
student_name = input("Enter Student Name: ")
marks = int(input("Enter Student Marks: "))
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
# Determine result
if marks >= 50:
    result = "PASS"
else:
    result = "FAIL"
# Comparison operation
passed = marks >= 50
# Logical operation
scholarship = marks >= 80 and result == "PASS"
# Display student report
print("\n===== Student Report =====")
print("Student Name         :", student_name)
print("Final Marks          :", marks)
print("Grade                :", grade)
print("Result               :", result)
print("Passed               :", passed)
print("Scholarship Eligible :", scholarship)
# Display appropriate message
if scholarship:
    print("Excellent! You are eligible for a scholarship.")
elif result == "PASS":
    print("Congratulations! You have passed.")
else:
    print("Keep practicing and try again.")
print("\nThank you for using the Student Grade Checker!")
