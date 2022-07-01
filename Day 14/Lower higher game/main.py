from replit import clear
from game_data import data
from art import logo ,vs
import random

def random_player(data):
    return random.choice(data)


def who_win(user_ask,player_A,player_B):
    if player_A['follower_count']> player_B['follower_count']:
        return user_ask == 'a'    
    else:
        return user_ask=="b"

def higher_lower():
    print(logo)
    score=0
    player_B=random_player(data)
    end_the_game=True
    while end_the_game:
        player_A= player_B
        player_B=random_player(data)
        while player_A==player_B:
            player_B=random_player(data)

        print(f"Compare A:  {player_A['name']} , a {player_A['description']} , from {player_A['country']}")
        print(vs)

        print(f"Against B:  {player_B['name']} , a {player_B['description']} , from {player_B['country']}")
        # print(player_A['follower_count'],"A")
        # print(player_B['follower_count'],"B")
        user_ask=input("Who has more Followers? Type 'A' or 'B':     ").lower()
        clear()
        print(logo)
        if who_win(user_ask,player_A,player_B):
            score+=1
            print(f"You're right. ")
        else:
            end_the_game=False
            print(f"Sorry, That's wrong. Your Final Scores are {score}")

higher_lower()