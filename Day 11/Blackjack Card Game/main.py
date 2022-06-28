import random
from art import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)


def calculate_sum(listt):
  if sum(listt)==21 and len(listt)==2:
    return 0
  if sum(listt)>21 and 11 in listt:
    listt.remove(11)
    listt.append(1)
  return sum(listt)


def compare(user_score,computer_score):
  if user_score == computer_score:
    print("DRAW")
  elif user_score==0:
    print("Win you have a blackjack")
  elif computer_score==0:
    print("LOSE computer has a blackjack")
  elif user_score>21:
    print("You Lose,")
  elif computer_score< user_score:
        print(" You WIN")      
  else:
        print("YOU LOSE")
    
def blackjack():
    print(logo)
    user=[]
    computer=[]
    game_over=False
    for i in range(2):
        user.append(deal_card())
        computer.append(deal_card())

    while not game_over:
        user_score=calculate_sum(user)
        computer_score=calculate_sum(computer)
        print(user,"is your cards")
        print(computer,"is computer's card")
    
        if user_score==0 or computer_score==0 or user_score>21:
            game_over=True
            
        else:
            for_other_card=input("Enter 'y' for other card").lower()
            if for_other_card=="y":
                user.append(deal_card())
            else :
                game_over=True
    while computer_score<17 and computer_score !=0:
        computer.append(deal_card())
        computer_score=calculate_sum(computer)

    print(f"User score:  {user_score}   User Cards: {user}")
    print(f"Computer score:  {computer_score}   Computer Cards: {computer}")
    compare(user_score,computer_score)
blackjack()
stop=True
while stop:
    should_continue=input("Enter 'y' to start again or 'n' to stop: ").lower()
    if should_continue=='y':
        blackjack()
    else: 
        print("Thanks for playing.")
        stop=False

