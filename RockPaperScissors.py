import random

def is_win(player, opponent):
    if (player=="r" and opponent=="s") or \
       (player=="p" and opponent=="r") or \
       (player=="s" and opponent=="p"):
        return True
    return False


def play():
    user = input("enter the choice: r for rock, p for paper and s for scissors: ")
    computer = random.choice(['r','p','s'])

    if user == computer:
        print("its a tie!")

    elif is_win(user, computer):
        print("you won!")

    else:
        print("you lose")


while True:
    play()
