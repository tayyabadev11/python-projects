# Project Title
print(" SIMPLE CALCULATOR")
#  (Input + Type Casting)
first_number = float(input("Enter First Number: "))
second_number = float(input("Enter Second Number: "))
# (Arithmetic Operators)
addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number
#  (Assignment Operator)
addition += 10
# (Comparison Operators)
greater = first_number > second_number
smaller = first_number < second_number
equal = first_number == second_number
# Display Result
print("\n RESULT ")
print("Addition (+10 Bonus):", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("\n Comparison Result")
print("First Number > Second Number :", greater)
print("First Number < Second Number :", smaller)
print("Both Numbers Equal :", equal)
print("\nThank you for using the Simple Calculator!")