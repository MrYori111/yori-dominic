# Python Program: Quiz on Multiplication Tables

print("Welcome to the Multiplication Quiz!")
print("You will be asked to solve 5 multiplication problems.")

total_questions = 5
score = 0


for question_number in range(1, total_questions + 1):
    num1 = question_number
    num2 = question_number + 1

    print(f"\nQuestion {question_number}:")
    print(f"What is {num1} x {num2}?")

    try:
        answer = int(input("Your answer: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        answer = -1

    if answer == num1 * num2:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong. The correct answer is {num1 * num2}.")


print("\nQuiz Complete!")
print(f"Your score: {score}/{total_questions}")


print("\nWould you like to try again? (yes/no)")
while True:
    retry = input("Enter your choice: ").strip().lower()
    if retry == "yes":

        score = 0
        print("\nRestarting the quiz!")
        for question_number in range(1, total_questions + 1):
            num1 = question_number
            num2 = question_number + 1
            print(f"\nQuestion {question_number}:")
            print(f"What is {num1} x {num2}?")
            try:
                answer = int(input("Your answer: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                answer = -1
            if answer == num1 * num2:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong. The correct answer is {num1 * num2}.")
        print("\nQuiz Complete!")
        print(f"Your score: {score}/{total_questions}")
        print("\nWould you like to try again? (yes/no)")
    elif retry == "no":
        print("Thank you for playing the quiz. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
