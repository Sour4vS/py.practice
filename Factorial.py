num =int(input("enter the number :"))
fact =1
if num < 0:
    print("negative number doesnt have factorial")
elif num==0:
    print("fatcorial is 1")
else:
    for i in range (1 , num+1):
        fact = fact*i
    print(f"factorial of {num} is {fact}")
   
