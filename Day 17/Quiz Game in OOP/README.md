# Quiz Game in OOP

## Steps to  follow

1. First make a data file which contain a list of questions. Questions are listed in dictionary which have two key values QUESTION TEXT and ANSWER

2. Make a question Model file which contain the class Question and their attributes (question_text , answer ).

3. Make a Question Brain file which contain a class in which all functionality of our quiz performed. Like it get list f question from data.py and have following methods.

    **sill_have_question()** to check any question left.

    **next_question()** for next question.

    **check_answer()** check answer is correct or not.

4. You have to traveres through all questions and in the end give the final score.


## Example
### For Correct Answer

Q.1: The HTML5 standard was published in 2014. (TRUE/FALSE):  true

You got the right answer.

Your current score is 1/1.


### For Wrong Answer

Q.5: Linus Torvalds created Linux and Git. (TRUE/FALSE):  false

You are wrong

The right answer is True.

Your current score is 4/5.


## At the END of quiz

You have completed the Quiz.

Your final scores are quiz 9/10 .