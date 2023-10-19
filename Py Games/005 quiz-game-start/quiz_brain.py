class Quiz:
    def __init__(self, question_list, question_num=0, score=0):
        self.num = question_num
        self.list = question_list
        self.score = score

    def still_have_questions(self):
        if self.num < len(self.list):
            return True
        else:
            print("You've completed the quiz")
            print(f"Your Finale score is : {self.score}/{self.num}")
            return False

    def check_answer(self, answers):
        checker = self.list[self.num]

        if answers == checker.answer:
            print("you got it")
            self.score += 1
            self.num += 1
            print(f"Your current score is : {self.score}/{self.num}")
            print()
        else:
            print('incorrect')
            self.num += 1
            print(f"Your current score is : {self.score}/{self.num}")
            print()

    def next_question(self):
        current_q = self.list[self.num]  # current_q = Question(text, answer)
        answer = input(f"Q.{self.num} {current_q.text} (True / False): ")
        return answer
