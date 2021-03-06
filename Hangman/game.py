import random
import security

#function that return a word randomly choosen in word_list.txt
def choose_word_ia():
    with open("word_list.txt", "r") as word_list:
        words = word_list.read().strip().split("\n")
    return random.choice(words).upper()

def choose_word_player():
    return security.input_word("Enter your word: ")

def initialize_player_w(secret_w, gessed):
    toDisp = ["_"] * len(secret_w)
    for letter in gessed:
        for i in range(len(secret_w)):
            if(secret_w[i] == letter):
                toDisp[i] = letter
    return " ".join(toDisp)

def word_diff(secret_w, player_w):
    player_w = player_w.replace(" ", "")
    if(player_w == secret_w):
        return False
    else:
        return True

def play_again():
    choice = input("Your choice: ")
    if(choice == "y" or choice == "yes"):
        return True
    else:
        return False
