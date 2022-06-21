import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice=[rock,paper,scissors]
user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user >= 3 or user < 0:
    print("you lose you enter an invalid statement")
    
else:
    print(choice[user])
    computer =random.randint(0,2)
    if computer >= 3 or computer < 0:
        print("you lose you enter an invalid statement")
    else:
        print(choice[computer])

        if user==0 and computer== 2:
            print("User Win")
        elif user==2 and computer== 1:
            print("User Win")
        elif user==1 and computer== 0:
            print("User Win")
        elif user== computer:
            print("draw")

        else:
            print("You Lose")
