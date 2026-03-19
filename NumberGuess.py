import random

num = input("enter a number :")
if num.isdigit():
    num = int(num)
    if num<=0:
        print("print number greater than 0..")
        quit()
else:
    print("enter a number please :")
    quit()
random_number =  random.randint(0,num)


while True:
    guess = input("Guess the number :")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("please enter a number next time :")
        continue

    if guess == random_number:
        print("correct")
        break
    elif guess>random_number:
            print("you guessed above the number")
    else:
            print("you guessed below the number ")

print(f"random no is:{random_number}")


