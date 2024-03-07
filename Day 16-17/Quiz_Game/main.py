from question_model import Question
from quiz_bank import QuizBank
from data import question_data

# Creating a Question Bank
question_bank = []
for question in question_data:
  question_text = question["question"]
  question_answer = question["correct_answer"]
  new_question = Question(question_text, question_answer)
  question_bank.append(new_question)

quiz = QuizBank(question_bank)

# Looping until the quiz has ended
while quiz.still_has_questions():
  quiz.new_question()

print(f"The quiz has ended.\nYour final score is {quiz.score}/{quiz.question_number}.")
