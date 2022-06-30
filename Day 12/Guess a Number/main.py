from art import logo
import random



def check_guess(guess,actual_number,number_of_turns):
    if guess>actual_number:
      print("TOO high")
      return number_of_turns-1
    elif guess < actual_number:
      print("TOO low")
      return number_of_turns-1
    else:
      return "win"


def check_level(level):
  if level =="low":
    turns= 10
    
  elif level =="hard":
    turns=5
  return turns


def guess_a_number():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I am thinking number from 1-100.")
  actual_number=random.randint(1,100)
  level=input("Enter level 'low' or 'hard': ").lower()
  turns=check_level(level)
  while True:
    guess=int(input("Enter a number you guess:  "))
    turns=check_guess(guess,actual_number,turns)
    if turns=="win":
      print(f"You win, You Guess the right number which is {guess}. ")
      break
    elif turns ==0:
      print("lose")
      break
    print(f"GUESS again you have {turns} remaining")



guess_a_number()
