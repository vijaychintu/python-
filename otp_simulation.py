import random

otp = random.randint(1000, 9999)
print(otp)

count = 3

while count > 0:
    user_otp = int(input("Enter OTP: "))

    if len(str(user_otp)) < 4:
        print("OTP must be a 4-digit number only.")
        continue

    if otp == user_otp:
        print("Correct OTP")
        break
    else:
        print("Incorrect OTP. Try again.")
        count -= 1
else:
    print("Max attempts done, try after 24 hours.")
1