a = 10
b = 11
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print("with functions")

a = 20
b = 30
def arithmetic():
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a%b)
arithmetic()

a = 100
b = 200
arithmetic()

def arithmetic(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a%b)
    print(a)
    print(b)
arithmetic(10,20)
arithmetic(20,10)


def login(username,password):
    if username == "vijay" and password == "pass123":
        print("login successful")
    else:
        print("login failed")

login("vijay","pass123")
login("pass123","vijay")

def emp_info(emp_name,emp_email,emp_location):
    print(f"hi{emp_name},your email is {emp_email} and your work locaion is {emp_location}")
emp_info("vijay","agurlavijaykumar21@gmail.com","hyderabad")

def emp_info(emp_name,emp_email,emp_location = "hyderbad"):
    print(f"hi{emp_name},your email is {emp_email} and your work locaion is {emp_location}")
emp_info("vijay","agurlavijaykumar21@gmail.com")

def emp_info(emp_name,emp_email,emp_location= "hyderbad"):
    print(f"hi{emp_name},your email is {emp_email} and your work locaion is {emp_location}")
emp_info("vijay","agurlavijaykumar21@gmail.com","pune")


def emp_info(emp_name,emp_email,emp_location,address = "india"):
    print(f"hi{emp_name},your email is {emp_email} and your work locaion is {emp_location} and your actual address is {address}")
emp_info("vijay","agurlavijaykumar21@gmail.com","hyderabad","bangalore")

def emp_info(emp_name,emp_email,emp_location,address = "india",mobile = "987654321"):
    print(f"hi{emp_name},your email is {emp_email} and your work locaion is {emp_location} and your actual address is {address}and your mobile {mobile}")
emp_info(emp_email="agurlavijaykumar21@gmail.com",emp_location="hyderabad",emp_name="vijay",mobile="987654321")

def add_all(*numbers):
    total = 0
    for i in numbers:
        total = total + i
        
    print(f"the total is: {total}")
    
add_all(1,2,3)
add_all(10,20,30)

def profile(**info):
    print(info)
profile(name="vijay",email="agurlavijaykumar21@gmail.com",mobile=987654321,rating=4.5)

def cred_trans(**trans):
    print(trans)
    total = 0
    for i in trans:

        total = total +  trans[i]
    print(f"you have done {len(trans)}and transactions total value is {total}")
    for i in trans:
        print(i)
cred_trans(jan=1000,feb=2000,mar=3000,apr=4000)


def cred_trans(*trans,**info):
    print(trans)
    print(info)
    total = 0
    for i in trans:
        total = total + i
    print(f"hi{info['name']}, you have  done {len(trans)} transactions for a total amount of {total}")
    cred_trans(1000,2000,3000,4000,name = "vijay",email = "agurlavijaykumar21@gmail.com ")
    cred_trans(5000,6000,7000,8000,name = "ajay",email = "agurlaajaykumar21@gmail.com ")
    
    def add(a,b):
        return a+b
    print(add(3,4))
    
def add (a,b,opr):
    if opr == "add":
        return a+b
    elif opr == "sub":
        return a-b
    else:
        return "invalid operator"
    print("check the output")
    
print(add(2,3,'add'))
print(add(2,3,'sub'))

def add(b,c):
    print(b)
    print(c)
add(10,20)
print(add(10,20))


#function composition 

def add(a,b):
    return a+b
def sub(c,d,e):
    return add(c,d) -e
print(sub(3,4,5))

print(dir(__builtins__))

def add(a,b):
    return a+b
print(add(3,4))

sum = lambda a,b: a+b
print(sum(3,4))

print((lambda a,b: a+b) (10,20))
print((lambda a,b: a+b) (100,200))

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
print(is_even(6))

print((lambda n: n % 2 == 0) (6))
print((lambda n: n % 2 == 0 )(5))

def square_list(numbers):
    square_list = []
    for n in numbers:
        square_list.append(n*n)
    return square_list
print(square_list([1,2,3,4,5]))

print(map(lambda n:n*n, [1,2,3,4,5]))
print(list(map(lambda n:n*n, [1,2,3,4,5])))


def even_list(numbers):
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
    return even_numbers
print(even_list([1,2,3,4,5,6,7,8,9,10]))

print(filter(lambda n: n % 2 == 0, [1,2,3,4,5,6,7,8,9,10]))

def multiply_list(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result
print(multiply_list([1,2,3,4,5,6]))

from functools import reduce
print(reduce(lambda x,y: x*y,[1,2,3,4,5]))

print