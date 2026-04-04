li = [0, 1, 0, 3, 12]
result = []
zeros = 0

for num in li:
    if num==0:
        zeros+=1
    else:
        result.append(num)

result.extend([0] * zeros)
print(result)
