import random

def roll():
    min =1
    max =6
    roll = random.randint(min,max)
    return roll

while True:
    players = input("enter number of players from 2 to 4 :")
    if players.isdigit():
        players = int(players)
        if 2<= players <=4:
            break
        else:
            print("enter numbers between 2 and 4..")
    else:
        print("enter valid amount..")


max_score = 50
player_score =[0 for _ in range(players)]

while max(player_score) < max_score:
    for player_indx in range(players):
        print("Player number", player_indx + 1, "turn has just started! \n")
        print("Your total score is:", player_score[player_indx])
        current_score =0
        while True:
            should_role = input("do you need to roll?(y)")
            if should_role.lower() !="y":
                break
            value =roll()
            if value ==1:
                print("You rolled a 1! Turn done!")
                current_score =0
                break
            else:
                current_score +=value
                print("you rolled a: ",value)
            print("your current score is :",current_score)
        player_score[player_indx] += current_score
        print("Your total score is:", player_score[player_indx])
        
max_score= max(player_score)
winning_idx = player_score.index(max_score)
print ("Player number", winning_idx + 1,"is the winner with a score of:", max_score)
