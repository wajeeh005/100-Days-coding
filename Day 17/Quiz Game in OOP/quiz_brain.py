
class QuizBrain:
    def __init__(self,q_list):
        self.question_no=0
        self.score=0
        self.question_list=q_list

    def still_have_question(self):
        if self.question_no<len(self.question_list):
            return True
        return False

    def next_question(self):
        current_question=self.question_list[self.question_no]
        self.question_no+=1
        answer=input(f"Q.{self.question_no}: {current_question.text} (TRUE/FALSE):  ")
        self.check_answer(answer,current_question.answer)
    
    def check_answer(self,answer,correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You got the right answer.")
            self.score+=1
        else:
            print("You are wrong")
            print(f"The right answer is {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_no}.\n ")


    