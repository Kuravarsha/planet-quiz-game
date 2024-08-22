# Function to ask a question and return if the answer is correct
def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    
    while True:
        try:
            user_answer = int(input("Enter the number of your answer: "))
            if 1 <= user_answer <= len(options):
                break
            else:
                print("Please select a valid option number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if options[user_answer - 1] == correct_answer:
        print("Correct!\n")
        return True
    else:
        print(f"Incorrect. The correct answer was: {correct_answer}\n")
        return False

# Main function to run the quiz
def run_quiz():
    questions = [
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Earth", "Venus", "Mercury", "Mars"],
            "correct_answer": "Mercury"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "correct_answer": "Mars"
        },
        {
            "question": "Which is the largest planet in our solar system?",
            "options": ["Earth", "Saturn", "Jupiter", "Neptune"],
            "correct_answer": "Jupiter"
        },
        {
            "question": "Which planet is known for its rings?",
            "options": ["Venus", "Mars", "Saturn", "Uranus"],
            "correct_answer": "Saturn"
        },
        {
            "question": "Which planet is known as the Earth's twin?",
            "options": ["Mars", "Venus", "Jupiter", "Mercury"],
            "correct_answer": "Venus"
        },
        {
            "question": "Which planet is the smallest in our solar system?",
            "options": ["Mars", "Venus", "Mercury", "Pluto"],
            "correct_answer": "Mercury"
        },
        {
            "question": "Which planet is farthest from the Sun?",
            "options": ["Neptune", "Uranus", "Saturn", "Pluto"],
            "correct_answer": "Neptune"
        },
        {
            "question": "Which planet has the Great Red Spot?",
            "options": ["Mars", "Jupiter", "Saturn", "Neptune"],
            "correct_answer": "Jupiter"
        },
        {
            "question": "Which planet is known as the 'Morning Star' or 'Evening Star'?",
            "options": ["Mercury", "Venus", "Mars", "Jupiter"],
            "correct_answer": "Venus"
        },
        {
            "question": "Which planet has the most moons?",
            "options": ["Earth", "Mars", "Saturn", "Jupiter"],
            "correct_answer": "Jupiter"
        }
    ]
    
    score = 0

    for q in questions:
        if ask_question(q["question"], q["options"], q["correct_answer"]):
            score += 1

    print(f"Quiz Complete! Your final score is: {score} out of {len(questions)}")

# Run the quiz
if __name__ == "__main__":
    run_quiz()