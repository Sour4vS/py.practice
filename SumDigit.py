num = int(input("enter 4 or 5 digit number :"))
total = 0
while num>0:
    digit  = num%10
    total+=digit
    num = num//10

print(total)
