username = input("enter username")
if len(username) >= 4:
    print("actual given",username)
    print("fromated output",username.lower())
    if username.lower().find("@") != -1:
        print("valid email")
    else:
        print("invalid email")
else:

    print("username should be at least 4 characters long")

pan = input("enter pan number")
formatted_pan = pan.upper()
print("formatted pan number", formatted_pan)

mobile = input("enter mobile number:")
if mobile.startswith("+86"):
    print("redirect to china")

elif mobile.startswith("+91"):
    print("redirect to india")

else:
    print("calling not possible")

email = input("Enter email: ")

if email.endswith("@gmail.com"):
    print("Synchronizing account to new Gmail")
else:
    print("Synchronization only available for Gmail")
