# Project 9 - Smart Student Record Analyzer

print("===== Smart Student Record Analyzer =====")

try:
    # Get student information
    name = input("Enter Student Name: ").title()
    age = int(input("Enter Student Age: "))
    city = input("Enter Student City: ").title()
    marks = int(input("Enter Student Marks: "))

    # Validate marks
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

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

except ValueError as error:
    print("\nError: Please enter valid information.")

    if str(error) == "Marks must be between 0 and 100.":
        print("Marks must be between 0 and 100.")
    else:
        print("Age and Marks must be numbers.")

else:
    # Write student information to a file
    with open("student_analysis.txt", "w") as file:
        file.write("===== Smart Student Record =====\n")
        file.write("Student Name : " + name + "\n")
        file.write("Age          : " + str(age) + "\n")
        file.write("City         : " + city + "\n")
        file.write("Marks        : " + str(marks) + "\n")
        file.write("Grade        : " + grade + "\n")
        file.write("Result       : " + result + "\n")

    print("\nStudent record saved successfully!")

    # Read student information from the file
    with open("student_analysis.txt", "r") as file:
        saved_record = file.read()

    # Display saved record
    print("\n===== Saved Student Record =====")
    print(saved_record)

    print("Record loaded successfully!")

finally:
    print("\nStudent record process completed.")
    print("Thank you for using the program!")
    print("===== Program Closed =====")
