import random


def deal_card(cards):
  return random.choice(cards)




def calculate_sum(listt):
  summ=0
  for i in listt:
    summ+=i
  return summ

def blackjack(user,computer):
  user=[]
  computer=[]
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  
  for i in range(2):
    user.append(deal_card(cards))
    computer.append(deal_card(cards))
  user_score=calculate_sum(user)
  computer_score=calculate_sum(computer)

  print(user,"is user")
  print(computer,"is computer")
  if (11 in user) and (10 in user):
    print("User have Blacked jack ACE +10 \n User Win")
    return
  elif (11 in computer) and (10 in computer):
    print("Computer have Blacked jack ACE +10 \n You LOSE")
    return
  elif user_score >21:
    if 11 in user:
      user_score-=10
    if calculate_sum(user) >21 or (11 not in user):
      print("LOSE")
      return
  for_other_card=input("enter yes for other card")
  if for_other_card=="yes":
    user.append(deal_card(cards))
    blackjack()
  else :
    while computer_score<17:
      computer.append(deal_card(card))
    if compute_score > 21 :
      print("You Win")
      return
    elif computer_score == user_score:
      print("DRAW")
      return
    elif computer_score> user_score:
      print("Computer Win, You Lose")
      return
    else:
      print("YOU WIN")
        


blackjack()