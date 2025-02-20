from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz_list = QuizBrain(question_bank)

while quiz_list.still_has_questions():
    quiz_list.next_question()

quiz_list.final_statement()