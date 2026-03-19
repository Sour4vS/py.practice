print("welcome to the game!")
user = input("are you ready to play? type yes to countinue : ").lower()
if user != "yes":
    quit()
score = 0
count = 0
answer = input("full form of CPU? ").lower()
if answer == "central processing unit":
    print("correct!")
    score += 2
    count += 1
else:
    print("incorrect..")
    score-=1

answer = input("full form of RAM? ").lower()
if answer == "random access memory":
    print("correct!")
    score += 2
    count += 1
else:
    print("incorrect..")
    score -= 1

answer = input("full form of GPU? ").lower()
if answer == "graphics processing unit":
    print("correct!")
    score += 2
    count += 1
else:
    print("incorrect")
    score -= 1

print(f"your final score out of {count} is:", score)
print("your percentage is"+str((count/3)*100)+"%")







