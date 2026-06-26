mylist = [23,35,67,81,101]
search_element = int(input("enter the element to search :"))
found = False
for i in range(len(mylist)):
    if mylist[i]==search_element:
        print('element found at index',i)
        found = True
        break
if not found:
 print("element is not present in the list")
