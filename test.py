# synax
# variable_name = value
# =-->Assignment operator

value_num = 10
value_rating = 4.2
value_name= "vijay"
new_name = "vijay"

new_rating = 4.2
print(id(value_num)) # unique identity i.e memory address
print(id(value_rating)) # unique identity i.e memory address
print(id(value_name)) # unique identity i.e memory address
print(id(new_rating)) # unique identity i.e memory address
print(id(new_name)) # unique identity i.e memory address


list1 = [1,2,3]
list2 = [1,2,3]
list3= [4,5,6]
print(id(list1)) # unique identity i.e memory address
print(id(list2)) # unique identity i.e memory address
print(id(list3)) # unique identity i.e memory address


print(type(value_num))
print(type(value_rating))
print(type(value_name))


msg = "python is amazing"
print(msg)

x = "python"
y = "is"
z ="amazing"
print(x+y+z)

version = 3
version_old = 2
print(x+y+z)
print(version+version_old)
 
 # print python is amazing 3
print(version,msg)

#many values to multiple variables
x,y,z = "python", "is" ,"amazing"
print(x)
print(y)
print(z)
print(x,y,z)

x = y = z = "pyhon"
print(x,y,z)

product_brand = "Levis"
product_rating = 4.5
product_price= 4000
air_bag_present = True