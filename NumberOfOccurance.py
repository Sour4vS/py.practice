mylist = [2,5,4,6,2,4,3,2,8]
count =0
num = int(input("enter the number to check :"))
for x in mylist:
    if x ==num:
        count+=1
print(f"count of occurance of {num} is {count}!")
