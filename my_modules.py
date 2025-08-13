name = "vijay"
email ="vijay@gmail.com"
def add (a,b):
    return a+b
def sub (a,b):
    return a-b
def info_new(name,email=email):
    return f"Hello{name} your email is {email}"

#other vendeer
name = "kumar"
email ="kumar@gmail.com"
def add (a,b):
    return a+b
def sub (a,b):
    return a-b
def info_new(name,email=email):
    return f"Hello{name} your email is {email}"

#builtin modules
import random
print(random.random())
print(random.randint(1,10))
print(random.randrange(10000))
list_lottery = ["lot1","lot2","lot3"]
print(random.choice(list_lottery))

list_users = ["user1","user2","user3"]
print(random.choices(list_users, k=2))

#webapp
import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response)

#modules.py
import math
print(math.sqrt(25))

from math import sqrt
print(math.sqrt(25))

import math as m
print(math.sqrt(25))

#client.py
import my_modules

print(my_modules)


name = "kumar"
email = "kumar@gmail.com"
print(my_modules.add(2,3))
print(my_modules.info(name,email))
print(my_modules.info_new(name="ram",email="ram@gmail.com"))

#c2
from my_modules import *
print((2,3))
print(info(name,email))
print(info_new(name="ram",email="ram@gmail.com"))
#c3
from my_modules import email,name,add
print(email)
print(name)
print(add(2,3))

#c4
from my_modules import email,name
from other_vendor_module import name,email
print(name)
print(email)
print(name)
print(email)

#c5
import my_modules
import other_vendor_module
print(my_modules.name)
