# Project 8 - Student File Manager
print("===== Student File Manager =====")
print("\nWelcome! Let's create a student record.")
# Get student information
name = input("Enter Student Name: ").title()
age = int(input("Enter Student Age: "))
city = input("Enter Student City: ").title()
marks = int(input("Enter Student Marks: "))
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
# Write student data to a file
with open("student_records.txt", "w") as file:
    file.write("===== Student Record =====\n")
    file.write("Student Name : " + name + "\n")
    file.write("Age          : " + str(age) + "\n")
    file.write("City         : " + city + "\n")
    file.write("Marks        : " + str(marks) + "\n")
    file.write("Grade        : " + grade + "\n")
    file.write("Result       : " + result + "\n")
print("\nStudent record saved successfully!")
print("Your information is now stored in a file.")
# Read student data from the file
with open("student_records.txt", "r") as file:
    saved_record = file.read()
# Display saved record
print("\n===== Saved Student Record =====")
print(saved_record)
print("Record loaded successfully!")
print("\nThank you for using Student File Manager.")
print("Keep learning and keep building!")
