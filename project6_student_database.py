# Project 6 - Student Database Pro
print("WELCOME TO STUDENT DATABASE")
students = []
def add_student():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    age = int(input("Enter Age: "))
    marks = float(input("Enter Marks: "))
    student = {
        "Name": name,
        "Roll Number": roll,
        "Age": age,
        "Marks": marks
    }
    students.append(student)
    print("Student Added Successfully!")
def view_students():
    if len(students) == 0:
        print("No Student Record Found")
    else:
        print("\nSTUDENT RECORDS")

        for student in students:
            print("-------------------")
            for key in student:
                print(key, ":", student[key])
def search_student():
    roll = input("Enter Roll Number to Search: ")
    found = False
    for student in students:
        if student["Roll Number"] == roll:
            print("\nStudent Found")
            for key in student:
                print(key, ":", student[key])
            found = True
            break
    if found == False:
        print("Student Not Found")
def update_student():
    roll = input("Enter Roll Number to Update: ")
    for student in students:
        if student["Roll Number"] == roll:
            new_marks = float(input("Enter New Marks: "))
            student["Marks"] = new_marks
            print("Student Record Updated Successfully!")
            return
    print("Student Not Found")
def delete_student():
    roll = input("Enter Roll Number to Delete: ")
    for student in students:
        if student["Roll Number"] == roll:
            students.remove(student)
            print("Student Deleted Successfully!")
            return
    print("Student Not Found")
def average_marks():
    if len(students) == 0:
        print("No Student Record Available")
    else:
        total = 0
        for student in students:
            total = total + student["Marks"]
        average = total / len(students)
        print("Average Marks:", average)
while True:
    print("\n STUDENT DATABASE MENU ")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Average Marks")
    print("7. Exit")
    choice = input("Enter Your Choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        average_marks()
    elif choice == "7":
        print("Thank you for using Student Database!")
        break
    else:
        print("Invalid Choice!")
