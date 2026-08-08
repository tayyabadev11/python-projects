# Project 8 - Student File Manager
print(" STUDENT FILE MANAGER")
print("\nWelcome! Let's create a student record.")
name = input("Enter Student Name: ").title()
age = int(input("Enter Student Age: "))
city = input("Enter Student City: ").title()
marks = int(input("Enter Student Marks: "))
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
# Writing Data to File
file = open("student_records.txt", "w")
file.write("          STUDENT RECORD\n")
file.write("Student Name : " + name + "\n")
file.write("Age          : " + str(age) + "\n")
file.write("City         : " + city + "\n")
file.write("Marks        : " + str(marks) + "\n")
file.write("Grade        : " + grade + "\n")
file.write("Result       : " + result + "\n")
file.close()
print("\nStudent record saved successfully!")
print("Your information is now stored in a file.")
# Reading Data from File
file = open("student_records.txt", "r")
saved_record = file.read()
file.close()
print(" SAVED STUDENT RECORD")
print(saved_record)
print("Record loaded successfully!")
print("\nThank you for using Student File Manager.")
print("Keep learning and keep building!")
