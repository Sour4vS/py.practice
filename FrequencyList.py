li = [1,2,2,3,1,4]

freq ={}
for num in li:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
print(freq)
