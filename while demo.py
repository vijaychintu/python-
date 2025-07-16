#while demo
count = 1
while count <= 5:
    print("count",count)
    count += 1

    #if  you don't know number of iterations before hand, use while loop
    #password validaion
    password = "Secret"
    user_password = ""

    while user_password != password:
        user_password = input("enter password:")

print("access granted")

# drink water till bottle is empty
water_in_bottle = 10
print("Drinking water")
while water_in_bottle > 0:
    print("Took a Sip,Remaining sip:",water_in_bottle-1)
    water_in_bottle -= 1