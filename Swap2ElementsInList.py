print("-----first methord-----")

mylist = [60, 35, 40, 52,65]

pos1=1
pos2= 3

first = mylist.pop(pos1)
second = mylist.pop(pos2-1)

mylist.insert(pos1,second)
mylist.insert(pos2,first)

print(mylist)



print("-----second methord-----")
mylist = [50, 55, 40, 32,15]
pos1,pos2 =1,3

mylist[pos1],mylist[pos2]=mylist[pos2],mylist[pos1]
print(mylist)

