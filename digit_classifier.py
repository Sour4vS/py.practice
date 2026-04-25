n = 50782
count_odd  =0
count_even =0
even_num = ""
odd_num = ""
while n>0:
    digit = n%10
    if digit%2==0:
        count_even+=1
        even_num += str(digit)+" "
    else:
        count_odd+=1
        odd_num += str(digit)+" "
    n = n//10
print("Even count =", count_even)
print("even digits:",even_num)

print("Odd count =", count_odd)
print("odd digits:",odd_num)
