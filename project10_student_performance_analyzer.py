# Project 10 - Student Performance Analyzer
import math
import random
print("=" * 55)
print("  STUDENT PERFORMANCE ANALYZER")
print("=" * 55)
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

def calculate_result(marks):
    if marks >= 50:
        return "PASS"
    else:
        return "FAIL"
def get_performance(grade):
    if grade == "A":
        return "Excellent Performance"
    elif grade == "B":
        return "Very Good Performance"
    elif grade == "C":
        return "Good Performance"
    elif grade == "D":
        return "Needs Improvement"
    else:
        return "More Practice Required"
def generate_challenge():
  
    return random.randint(1, 10)


try:

    name = input("\nEnter Student Name: ").title()
    age = int(input("Enter Student Age: "))
    marks = float(input("Enter Marks (0-100): "))
    if age <= 0:
        raise ValueError("Age must be greater than zero.")

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")
    grade = calculate_grade(marks)
    result = calculate_result(marks)
    performance = get_performance(grade)
    marks_square = math.pow(marks, 2)
    marks_square_root = math.sqrt(marks)
    challenge_number = generate_challenge()
    print("\n" + "-" * 55)
    print("  STUDENT REPORT")
    print("-" * 55)

    print("Student Name       :", name)
    print("Age                :", age)
    print("Marks              :", marks)
    print("Grade              :", grade)
    print("Result             :", result)
    print("Performance        :", performance)

    print("\n----- Mathematical Analysis -----")
    print("Marks Square       :", marks_square)
    print("Marks Square Root  :", round(marks_square_root, 2))

    print("\n----- Random Learning Challenge -----")
    print("Challenge Number   :", challenge_number)

    
    file = open("student_performance.txt", "w")

    file.write("STUDENT PERFORMANCE REPORT\n")
    file.write("=" * 40 + "\n")
    file.write("Student Name      : " + name + "\n")
    file.write("Age               : " + str(age) + "\n")
    file.write("Marks             : " + str(marks) + "\n")
    file.write("Grade             : " + grade + "\n")
    file.write("Result            : " + result + "\n")
    file.write("Performance       : " + performance + "\n")
    file.write("Marks Square      : " + str(marks_square) + "\n")
    file.write(
        "Marks Square Root : "
        + str(round(marks_square_root, 2))
        + "\n"
    )
    file.write(
        "Challenge Number  : "
        + str(challenge_number)
        + "\n"
    )

    file.close()

    print("\nStudent report saved successfully!")

   

    file = open("student_performance.txt", "r")

    saved_report = file.read()

    file.close()

    print("\n" + "-" * 55)
    print("             SAVED REPORT")
    print("-" * 55)

    print(saved_report)

except ValueError as error:

    print("\n" + "-" * 55)
    print("  ERROR")
    print("-" * 55)

    print("Invalid student information.")
    print("Please enter valid values.")
    print("Details:", error)


else:

    print("\n" + "-" * 55)
    print("  PROCESS COMPLETED SUCCESSFULLY")
    print("-" * 55)

    print("Student information was analyzed successfully.")
    print("The report was saved and loaded successfully.")

finally:

    print("\n" + "=" * 55)
    print(" STUDENT PERFORMANCE ANALYZER")
    print(" PROGRAM CLOSED")
    print("=" * 55)