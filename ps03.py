=== Student Information Input ===
name = input("Enter the Student's name: ")
marks = int(input("Enter the Marks (0-100): "))
attendance = int(input("Enter the Attendance percentage (0-100): "))

=== Grade Determination ===
#This section is already using if-elif-else, no changes needed.
if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'F'


=== Bonus Eligibility and Student Status ===
# Bonus eligibility using ternary operator (no change needed)
bonus = "Yes" if attendance >= 75 else "No"

# Student Status using ternary operator (no change needed)
status = "Pass" if marks >= 60 else "Fail"


=== Result Output ===
print("\nStudent Report")
print(f"Name: {name}")
print(f"Grade: {grade}")
print(f"Attendance: {attendance}%")
print(f"Bonus Eligibility: {bonus}")
print(f"Status: {status}")

=== Bonus Message (if-elif-else) ===
if grade == 'A':
    print("Excellent work! Keep it up!")
elif grade == 'B':
    print("Great job! Aim for an A next time!")
elif grade == 'C':
    print("Good effort! Try to improve further.")
elif grade == 'D':
    print("You passed, but there's room for improvement.")
else:  # grade == 'F'
    print("Unfortunately, you failed. Work harder next time.")
