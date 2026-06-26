mylist = [23,35,67,81,101]
left = 0
right = len(mylist)-1

while left<right:
    mylist[left],mylist[right]=mylist[right], mylist[left]
    left+=1
    right-=1

print("reveresed list is :",mylist)
    
