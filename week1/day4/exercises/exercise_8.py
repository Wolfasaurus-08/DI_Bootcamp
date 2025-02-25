def ask_questions(data):
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = []
    
    for item in data:
        user_answer = input(item['question'] + " ")
        if user_answer.lower() == item['answer'].lower():
            correct_answers += 1
        else:
            incorrect_answers += 1
            wrong_answers.append({
                "question": item['question'],
                "user_answer": user_answer,
                "correct_answer": item['answer']
            })
            
    return correct_answers, incorrect_answers, wrong_answers

def inform_user(correct_answers, incorrect_answers):
    print(f"You got {correct_answers} correct answers and {incorrect_answers} incorrect answers.")

def bonus_display(wrong_answers):
    if wrong_answers:
        print("\nYou answered the following questions incorrectly:")
        for item in wrong_answers:
            print(f"Question: {item['question']}\nYour Answer: {item['user_answer']}\nCorrect Answer: {item['correct_answer']}\n")
    
    if len(wrong_answers) > 3:
        print("You had more than 3 wrong answers. Would you like to play again? (yes/no)")
        play_again = input()
        if play_again.lower() == "yes":
            run_quiz(data)

def run_quiz(data):
    correct_answers, incorrect_answers, wrong_answers = ask_questions(data)
    inform_user(correct_answers, incorrect_answers)
    bonus_display(wrong_answers)

# Run the quiz
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

run_quiz(data)
