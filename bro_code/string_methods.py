username = input("enter the username: ")
if len(username) < 5 and username.isalpha() :
    print(f"the {username} is valid")

else:
    print(f"the {username} is invalid")
          