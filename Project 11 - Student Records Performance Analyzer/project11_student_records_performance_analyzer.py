# Project 11 - Student Records & Performance Analyzer
import json
import csv
import os
from pathlib import Path
from datetime import datetime
from collections import Counter


# ----------------------------------------------------------
# Data Storage
# ----------------------------------------------------------

data_folder = Path("student_analyzer_data")
data_folder.mkdir(exist_ok=True)

json_file = data_folder / "students.json"
csv_file = data_folder / "students.csv"


# ----------------------------------------------------------
# Functions
# ----------------------------------------------------------

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


def load_records():
    if not json_file.exists():
        return []

    try:
        with open(json_file, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_records(records):
    with open(json_file, "w") as file:
        json.dump(records, file, indent=4)

    fields = [
        "name",
        "age",
        "marks",
        "attendance",
        "grade",
        "result",
        "date_added"
    ]

    with open(csv_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(records)


def add_student(records):
    print("\nADD NEW STUDENT")


    try:
        name = input("Student name: ").strip().title()
        age = int(input("Age: "))
        marks = float(input("Marks: "))
        attendance = float(input("Attendance (%): "))

        if not name:
            print("Please enter a valid name.")
            return

        if age <= 0:
            print("Age must be greater than zero.")
            return

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

        if not 0 <= attendance <= 100:
            print("Attendance must be between 0 and 100.")
            return

        grade = calculate_grade(marks)
        result = "Pass" if marks >= 50 else "Fail"

        student = {
            "name": name,
            "age": age,
            "marks": marks,
            "attendance": attendance,
            "grade": grade,
            "result": result,
            "date_added": datetime.now().strftime("%d-%m-%Y %I:%M %p")
        }

        records.append(student)

        # Save automatically after adding a student
        save_records(records)

        print("\nStudent record added successfully.")
        print("The record has been saved to JSON and CSV files.")

    except ValueError:
        print("\nInvalid information.")
        print("Please enter the correct values.")


def view_students(records):
    if not records:
        print("\nNo student records are available.")
        return

    print("\nSTUDENT RECORDS")


    for number, student in enumerate(records, start=1):
        print(f"\nStudent {number}")
        print(f"Name       : {student['name']}")
        print(f"Age        : {student['age']}")
        print(f"Marks      : {student['marks']}")
        print(f"Attendance : {student['attendance']}%")
        print(f"Grade      : {student['grade']}")
        print(f"Result     : {student['result']}")
        print(f"Added      : {student['date_added']}")


def search_student(records):
    if not records:
        print("\nNo student records are available.")
        return

    name = input("\nEnter student name: ").strip().lower()

    matches = [
        student for student in records
        if name in student["name"].lower()
    ]

    if not matches:
        print("No matching record was found.")
        return

    view_students(matches)


def analyze_performance(records):
    if not records:
        print("\nNo records are available for analysis.")
        return

    grades = Counter(student["grade"] for student in records)
    results = Counter(student["result"] for student in records)

    average_marks = sum(
        student["marks"] for student in records
    ) / len(records)

    highest = max(records, key=lambda student: student["marks"])
    lowest = min(records, key=lambda student: student["marks"])

    print("\nPERFORMANCE ANALYSIS")

    print(f"Total Students : {len(records)}")
    print(f"Average Marks  : {average_marks:.2f}")
    print(f"Highest Marks  : {highest['name']} ({highest['marks']})")
    print(f"Lowest Marks   : {lowest['name']} ({lowest['marks']})")

    print("\nGrade Distribution:")
    for grade, count in sorted(grades.items()):
        print(f"{grade}: {count}")

    print("\nResult Summary:")
    for result, count in results.items():
        print(f"{result}: {count}")


def storage_information():
    print("\nDATA STORAGE")

    print("Storage Folder:", os.path.abspath(data_folder))
    print("JSON File:", json_file)
    print("CSV File:", csv_file)

    print("\nStored Files:")

    for item in data_folder.iterdir():
        print("-", item.name)

# Main Application

records = load_records()

print("=" * 55)
print("       STUDENT RECORDS & PERFORMANCE ANALYZER")
print("=" * 55)

while True:

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Analyze Performance")
    print("5. Save Records")
    print("6. Storage Information")
    print("7. Exit")

    choice = input("\nChoose an option: ").strip()

    if choice == "1":
        add_student(records)

    elif choice == "2":
        view_students(records)

    elif choice == "3":
        search_student(records)

    elif choice == "4":
        analyze_performance(records)

    elif choice == "5":
        save_records(records)
        print("\nAll student records have been saved successfully.")

    elif choice == "6":
        storage_information()

    elif choice == "7":
        save_records(records)
        print("\nYour records have been saved safely.")
        print("Thank you for using the Student Analyzer.")
        print("Keep learning, keep building, and keep improving.")
        break

    else:
        print("\nInvalid option.")
        print("Please choose a number from 1 to 7.")
