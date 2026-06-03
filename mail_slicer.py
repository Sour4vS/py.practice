email = input("enter the mail id..")

index = email.index("@")
user_name = email[:index]
domain = email[index+1:]

print(f"Your username is {user_name} and domain is {domain}")
