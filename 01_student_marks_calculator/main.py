# Student Marks and Average Calculator
# Uses variables, input/output, type conversion, and arithmetic operators.

student_name = input("Enter student name: ")
mark1 = float(input("Enter marks for subject 1: "))
mark2 = float(input("Enter marks for subject 2: "))
mark3 = float(input("Enter marks for subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("\\n--- Student Marks Report ---")
print("Student name:", student_name)
print("Total marks:", total)
print("Average marks:", average)
