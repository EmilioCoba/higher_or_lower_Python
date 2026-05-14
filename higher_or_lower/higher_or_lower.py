import art 
import game_data
import random

logo = art.logo
vs_art = art.vs
data = game_data.data

# check if the same account is pulled twice
def check_if_same_personality(first_instagram_account,second_instagram_account):
    return first_instagram_account==second_instagram_account
       
# returns the instagram account
def get_instagram():
    return random.choice(data)

# the print statements collected all here
def print_data(logo,first_instagram_account,second_instagram_account,vs_art):
    print("\n"*20)
    print(logo)
    print(f"Compare A: {first_instagram_account['name']}, a {first_instagram_account['description']}, from {first_instagram_account['country']}.")
    print("\n"+vs_art+"\n")
    print(f"Compare B: {second_instagram_account['name']}, a {second_instagram_account['description']}, from {second_instagram_account['country']}.")

def find_correct_answer(first_instagram_account,second_instagram_account):
    if first_instagram_account['follower_count']>second_instagram_account['follower_count']:
        return "a"
    return "b"
    


# main game logic
def higher_or_lower():
    play_again=True
    while play_again:
        continue_game=True
        score=0
        first_instagram_account=get_instagram()
        while continue_game:
            second_instagram_account=get_instagram()
            while check_if_same_personality(first_instagram_account,second_instagram_account) or first_instagram_account['follower_count']==second_instagram_account['follower_count']:
                second_instagram_account=get_instagram()
            
            print_data(logo,first_instagram_account,second_instagram_account,vs_art)
            answer=input("Who has more followers? Type 'A' or 'B': ").lower()
            while answer not in["a","b"]:
                print_data(logo,first_instagram_account,second_instagram_account,vs_art)
                answer=input("Invalid answer! Who has more followers? Type 'A' or 'B': ").lower()
            correct_answer=find_correct_answer(first_instagram_account,second_instagram_account)
            if answer==correct_answer:
                score+=1
                if correct_answer=="b":
                        first_instagram_account=second_instagram_account
            continue_game=answer==correct_answer
        
        print("\n"*20)
        print(f"Sorry that's wrong!\n{first_instagram_account['name']} has {first_instagram_account['follower_count']} million followers.\n{second_instagram_account['name']} has {second_instagram_account['follower_count']} million followers.")
        print(f"Your score was: {score}")
        replay=input("Do you want to play again? Type 'y' or 'n':").lower()
        while replay not in ["y","n"]:
            replay=input("Invalid answer!\nDo you want to play again? Type 'y' or 'n':").lower()
        if replay=='n' :
            play_again=False
        
        

higher_or_lower()