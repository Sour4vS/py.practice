mylist = ['apple','orange','apple','banana']
n = 2
count = 0
word = "apple"
for i in range(0,len(mylist)-1):
    if mylist[i]==word:
        count=count+1
        if count ==n:
            mylist.pop(i)
print(mylist)
