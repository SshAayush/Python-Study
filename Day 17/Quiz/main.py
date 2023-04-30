from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_q = question["text"]
    new_a = question["answer"]
    new_question = Question(text = new_q, answer = new_a)
    
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()
