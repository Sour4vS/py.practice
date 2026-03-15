import random
def guess(x):
    random_no = random.randint(1,x)
    guess =0
    while guess!= random_no:
        guess = int(input(f"guess the number from 1 to {x}: "))
        if guess == random_no:
            print(f"yes ..the number is {random_no}")
            break
        elif guess > random_no:
            print("guessed number is higher")
        else :
            print("guessed number is lower")
guess(10)
