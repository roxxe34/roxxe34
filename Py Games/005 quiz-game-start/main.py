from data import question_data
from question_model import Question
from quiz_brain import Quiz

question_list = []
for i in question_data:
    new_question = Question(i["text"], i['answer'])
    question_list.append(new_question)

question_num = 0

ask = Quiz(question_list, question_num)

while ask.still_have_questions():
    answer = ask.next_question()
    ask.check_answer(answer)

# while question_num <= len(question_list):
#     ask = Quiz(question_list, question_num)
#     check_answer = question_list[question_num]
#     value = check_answer.answer
#     answer = ask.next_question()
#     if answer == value:
#         print("correct")
#         question_num += 1
#     else:
#         print("incorrect")
#         question_num += 1
