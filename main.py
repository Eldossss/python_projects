from art import log , vska
from art import vska
from data import data_of_users
import random
import os
#Display art
print(log)
score = 0
game_should_continue = True
#Making account  at position B become the next at positon A.
account_b = random.choice(data_of_users)
while game_should_continue:

 #generate random account from game data.
 #Format the account into printabel format
 def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr} from {account_country}"

 def check_answer(guess,a_followers,b_followers):
    if a_followers > b_followers:
        return guess == "A"
    else:
        return guess == "B"
 account_a = account_b
 account_b = random.choice(data_of_users)
 if (account_a == account_b):
    account_b = random.choice(data_of_users)
 print(f"Compare A :{format_data(account_a)}.")
 print(vska)
 print(f"Against B :{format_data(account_b)}.")


#Ask user for a guess
 guess = input("Who has more followers ?   Type 'A' or 'B' : ")

#Check if user is correct
#Get follower count of each account
 a_follower_count = account_a["follower_count"]
 b_follower_count = account_b["follower_count"]
#Use if statmenet to check if user is correct
 os.system('cls')
 is_correct = check_answer(guess,a_follower_count,b_follower_count)
#Give user feedback on their guess
#Score keeping
 if is_correct:
    score += 1
    print(f"You're right.Current score: {score}.")
 else:
    game_should_continue = False
    print(f"Sorry,that's not right.Final score: {score}")



