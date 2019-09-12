# Math and Random Modules
# Using the built-in functions on Numbers perform following operations
# a) Round of the given floating point number. Example:
# n=0.543 then round it next decimal number, i.e n=1.0 Use round() function
import math
from math import sqrt
from random import random, uniform, randint, choice

n = int(input("Enter a number : "))
print("Round : %f" % float(round(n)))

# b) Find out the square root of a given number. (Use sqrt(x) function)

print("Square Root : %d" % sqrt(round(n)))

# c) Generate random number between 0, and 1 ( use  random() function)

print("Random no between 1 & 0 : %f" % random())

# d) Generate random number between 10 and  500. (Use uniform() function)

print("Random no between 10 & 500 : %f" % uniform(10, 500))

# e) Explore all Math and Random module functions  on a given number/ List.

print("------- All Maths Function -------")
print("math.pi : %f" % math.pi)
print("math.e : %f" % math.e)
print("math.radians(n) : %f" % math.radians(n))
print("math.sin(n) : %f" % math.sin(n))
print("math.cos(n) : %f" % math.cos(n))
print("math.tan(n) : %f" % math.tan(n))
print("math.log(n) : %f" % math.log(n))
print("math.pow(2,3) : %f" % math.pow(2, 3))
print("math.ceil(2.323) : %d" % math.ceil(2.323))
print("-------  -------")

print("------- All Random Function -------")
print("random.random() %f" % random())
print("random.randint(1,100) %d" % randint(1, 100))
print("random.choice([12,23,45,67,65,43]) %d" % choice([12, 23, 45, 67, 65, 43]))
print("-------  -------")
