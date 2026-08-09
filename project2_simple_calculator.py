# Project 2 - Simple Calculator
print("===== Simple Calculator =====")
# Get two numbers from the user
first_number = float(input("Enter First Number: "))
second_number = float(input("Enter Second Number: "))
# Perform arithmetic operations
addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number
# Assignment operation
addition += 10
# Perform comparison operations
greater = first_number > second_number
smaller = first_number < second_number
equal = first_number == second_number
# Display calculation results
print("\n===== Results =====")
print("Addition (+10 Bonus):", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
# Display comparison results
print("\n===== Comparison Results =====")
print("First Number > Second Number:", greater)
print("First Number < Second Number:", smaller)
print("Both Numbers Equal:", equal)
print("\nThank you for using the Simple Calculator!")
