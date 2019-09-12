# All string functions

a = "Hello World "
print(a)  # Printing
print(a[1]) # Accessing element at a particular position
print(a[2:5]) # Slicing
print(a[-5:-2]) # Negative Slicing
print(len(a)) # Length
a="HEllo  World       "
print(a.strip()) # Removing Trailing Spaces
print(a.lower())
print(a.replace("H", "J"))
print(a.split(","))
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 21
txt = "My name is Shubham, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

