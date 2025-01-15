import random

# Python Program: Quiz on Multiplication Tables

def run_quiz(current_score):
    score = current_score
    correct_answers = []  
    incorrect_answers = []  
    
    for question_number in range(1, total_questions + 1):
        num1 = random.randint(1, 10)  
        num2 = random.randint(1, 10)  

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
            correct_answers.append(f"{num1} x {num2} = {answer}")  
        else:
            print(f"Wrong. The correct answer is {num1 * num2}.")
            incorrect_answers.append(f"{num1} x {num2} = {num1 * num2}")  
    
    return score, correct_answers, incorrect_answers


print("Welcome to the Multiplication Quiz!")
print("You will be asked to solve 5 multiplication problems.")

total_questions = 5
score = 0
total_score = 0  # Track overall score across retries
total_possible_score = total_questions  # Total score for each attempt

while True:
    score, correct_answers, incorrect_answers = run_quiz(score)
    total_score += score  # Add score from each round to the total score

    print("\nSummary of Results:")
    print("\nCorrectly answered questions:")
    if correct_answers:
        for item in correct_answers:
            print(item)
    else:
        print("No correct answers.")
    
    print("\nIncorrectly answered questions:")
    if incorrect_answers:
        for item in incorrect_answers:
            print(item)
    else:
        print("No incorrect answers.")
    
    print(f"\nQuiz Complete!")
    print(f"Your total score: {total_score}/{total_possible_score * ((total_score // total_questions) + 1)}")

    print("\nWould you like to try again? (yes/no)")
    retry = input("Enter your choice: ").strip().lower()
    while retry not in ['yes', 'no']:
        print("Invalid response. Please enter 'yes' or 'no'.")
        retry = input("Enter your choice: ").strip().lower()

    if retry == "no":
        print("Thank you for playing the quiz. Goodbye!")
        break
