import json

def load_questions(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data['questions']

def save_result(user_name, score):
    result = {"user_name": user_name, "score": score}
    with open("quiz_results.json", 'a') as file:
        json.dump(result, file)
        file.write('\n')

def take_quiz(questions):
    score = 0
    total_questions = len(questions)
    for i, question_data in enumerate(questions, start=1):
        print(f"Question {i}: {question_data['question']}")
        user_answer = input("Your answer: ").strip()
        if user_answer.lower() == question_data['answer'].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    return score

def main():
    user_name = input("Enter your name: ")
    questions = load_questions("quiz_questions.json")
    score = take_quiz(questions)
    print(f"\n{user_name}, your score is: {score}/{len(questions)}")
    save_result(user_name, score)

if __name__ == "__main__":
    main()