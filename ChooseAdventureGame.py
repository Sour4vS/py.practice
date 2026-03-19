name =  input("enter your name :")
enter = input(f"welcome {name} to the adventure! type yes to enter... ").lower().strip()
if enter=="yes":
    answer = input("you are at the end of the road. where you want to go? left or right?").lower().strip()
    if answer =="left":
        answer = input(
            "You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")

        if answer == "swim":
            print("You swam acrross and were eaten by an alligator.")
        elif answer == "walk":
            print("You walked for many miles, ran out of water and you lost the game.")
        else:
            print('Not a valid option. You lose.')
    elif answer =="right":
        answer = input(
            "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

        if answer == "back":
            print("You go back and lose.")
        elif answer == "cross":
            answer = input(
                "You cross the bridge and got a box full of gold..you won! ")
            quit()
        else:
            print("type valid option")
    else:
        print("choose valid option")
elif enter=="no":
    print("exiting....")
