name = input("Enter the Student's name: ")
marks = int(input("Enter the Marks (0-100): "))
attendance = int(input("Enter the Attendance percentage (0-100): "))

# Determine grade using if-elif-else
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

# Check bonus eligibility using if-else
if attendance >= 75:
    bonus = True
else:
    bonus = False

# Use a ternary operator to determine student status
status = "Pass" if marks >= 60 else "Fail"

# Output the result
print("\nStudent Report")
print(f"Name: {name}")
print(f"Grade: {grade}")
print(f"Attendance: {attendance}%")
print(f"Bonus Eligibility: {'Yes' if bonus else 'No'}")
print(f"Status: {status}")

# Bonus message using case (match-case in Python 3.10+)
match grade:
    case 'A':
        print("Excellent work! Keep it up!")
    case 'B':
        print("Great job! Aim for an A next time!")
    case 'C':
        print("Good effort! Try to improve further.")
    case 'D':
        print("You passed, but there's room for improvement.")
    case 'F':
        print("Unfortunately, you failed. Work harder next time.")
