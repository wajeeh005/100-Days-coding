from winsound import PlaySound

from sklearn.metrics import SCORERS
from game_data import data
from art import logo ,vs
import random


print(logo)
def who_win(user_ask,player_A,player_B):
    if user_ask =="a":
        if player_A['follower_count']> player_B['follower_count']:
            print("A win")
            return True
    elif user_ask=="b":
        if player_B['follower_count']> player_A['follower_count']:
            print("B win")
            return True
    return False


def random_player(data):
    return random.choice(data)
def higher_lower(score1):
    score=score1
    player_A= random_player(data)
    player_B=random_player(data)
    print(f"Compare A:  {player_A['name']} , a {player_A['description']} , from {player_A['country']}")
    print(vs)

    print(f"Against B:  {player_B['name']} , a {player_B['description']} , from {player_B['country']}")

    user_ask=input("Who has more Followers? Type 'A' or 'B':     ").lower()
    print(player_A['follower_count'],"A")
    print(player_B['follower_count'],"B")
    if who_win(user_ask,player_A,player_B):
        score+=1
        higher_lower(score)
    return scoring(score)

def scoring(score):
    score+=1
    return print(score)

score=0
higher_lower(score)